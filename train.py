import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet, LogisticRegression
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
import dvc.api
from datetime import datetime
import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# evaluation metrics function


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


# excusion starts from here
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Importing the collected Data from dvc
    # tag version is v5-scaled-normalized
    path = 'data/scaled_data.csv'
    repo = 'https://github.com/Abel-Blue/breastCancer-causal-Inference'
    rev = 'v5-scaled-normalized'
    data_url = dvc.api.get_url(path=path, repo=repo, rev=rev)

    try:
        scaled = pd.read_csv("data/scaled_data.csv")
    except Exception as e:
        logger.exception(
            "Unable to download training & test CSV, check your internet connection. Error: %s", e
        )

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(scaled)

    # separate the independent and target variable
    # The predicted column is "quality" which is a scalar from [3, 9]
    
    train_x = train.drop(['diagnosis'], axis=1)
    test_x = test.drop(['diagnosis'], axis=1)
    train_y = train[['diagnosis']]
    test_y = test[['diagnosis']]

    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    with mlflow.start_run():

        # Random Forest model
        # lr = RandomForestRegressor(max_depth=10, random_state=42)
        lr = LogisticRegression(random_state=0)
        lr.fit(train_x, train_y)

        # predicted values
        predicted_qualities = lr.predict(test_x)

        # evaluate the model by using the metrics
        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

        # print out the evaluation metrics
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        # log parameters, metrics, and artifacts
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        # log the model
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry does not work with file store

        date = datetime.now()
        date = date.strftime("%A-%B-%Y : %I-%M-%S %p")

        # writing cml report on results.txt data
        with open('results.txt', 'w') as file:
            file.write(f'Date:\n\t{date}\n')
            file.write('Metrics:\n')
            file.write(f'RMSE:\n\t{rmse}\n')
            file.write(f'R2Error:\n\t{r2}\n')
            file.write(f'MAE:\n\t{mae}\n')

        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(
                lr, "model", registered_model_name="RandomForestRegressor")
        else:
            mlflow.sklearn.log_model(lr, "model")
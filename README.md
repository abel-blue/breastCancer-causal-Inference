<h1 align="center">Breast Cancer diagnosis with Causal Inference</h1>
<div>
<img src="https://img.shields.io/badge/OS-linux%20%7C%20windows-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44" alt="Operating systems"/>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/network/members"><img src="https://img.shields.io/github/forks/Abel-Blue/agriTech-USGS-LiDAR" alt="Forks Badge"/></a>
<a href="https://github.com/Abel-Blue/agriTech-USGS-LiDAR/pulls"><img src="https://img.shields.io/github/issues-pr/Abel-Blue/breastCancer-causal-Inference" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/issues"><img src="https://img.shields.io/github/issues/Abel-Blue/breastCancer-causal-Inference" alt="Issues Badge"/></a>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Abel-Blue/breastCancer-causal-Inference?color=2b9348"></a>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Abel-Blue/breastCancer-causal-Inference?color=2b9348" alt="License Badge"/></a>
</div>

</br>

![causal-image](https://www.inovex.de/wp-content/uploads/2020/03/Causal-Inference-Hero.png)

<!-- ## Presentation Slide

- [Rossmann Pharmaceutical Sales prediction](https://www.canva.com/design/DAFBtdnLoKQ/hxJHGTgvoTwJMX9hXbbGVA/view?utm_content=DAFBtdnLoKQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Data visualization link

- [visualization link](https://share.streamlit.io/abel-blue/pharmaceutical-sales-prediction/main/app.py)

## Articles

- [Medium Article](https://medium.com/@Abel-Blue/pharmaceutical-sales-prediction-using-a-deep-learning-model-92d7d1e9626b) -->

## Table of Contents

1. [Introduction](#Introduction)
2. [Project Structure](#project-structure)
   - [data](#data)
   - [notebooks](#notebooks)
   - [scripts](#scripts)
   - [tests](#tests)
   - [logs](#logs)
   - [root folder](#root-folder)
3. [Installation guide](#installation-guide)

<hr>

## Introduction

> <p>Causal inference is an important link between the practice of cancer epidemiology and effective cancer prevention.</p>

 <p>The causal graph is a central object in the framework mentioned above, but it is often unknown, subject to personal knowledge and bias, or loosely connected to the available data. The main objective of the task is to highlight the importance of the matter in a concrete way. In this spirit, trainees are expected to attempt the following tasks:
</p>

1. Perform a causal inference task using Pearl’s framework;
2. Infer the causal graph from observational data and then validate the graph;
3. Merge machine learning with causal inference;
4. Use the resulting graph to predict the outcome of a disease;

The first is straightforward, the second and third are still open questions in the research community, hence may need a bit more research, innovation, and thinking outside the box from trainees.

> <b>Data Features:</b>
>
> <p>
> Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

<b>Attribute Information</b>:

- ID number
- Diagnosis (M = malignant, B = benign)

<b>The remaining (3-32)</b>

Ten real-valued features are computed for each cell nucleus:

- radius (mean of distances from center to points on the perimeter)
- texture (standard deviation of gray-scale values)
- Perimeter
- Area
- smoothness (local variation in radius lengths)
- compactness (perimeter^2 / area - 1.0)
- concavity (severity of concave portions of the contour)
- concave points (number of concave portions of the contour)
- Symmetry
- fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius. All feature values are recorded with four significant digits.

> Missing attribute values: none
> Class distribution: 357 benign (not cancer), 212 malignant (cancer)

</p>

<hr>

<!-- <img src="images/slide/3.png" name="">
<img src="images/slide/4.png" name=""> -->

## Project Structure

### [images](images):

- `images/` the folder where all snapshot for the project are stored.

### [logs](logs):

- `logs/` the folder where script logs are stored.

### [data](data):

- `data/` the folder where the dataset files are stored.

### [.github](.github):

- `.github/`: the folder where github actions and unit-tests are integrated.
- `cml.yaml`: the file where the cml configuration is stored.
- `unit_test.yml`: the file where the unit-tests are stored.

### [.vscode](.vscode):

- `.vscode/`: the folder where local path are stored.

### [notebooks](notebooks):

- `notebooks/`: a jupyter notebook for preprocessing the data.
- `data_exploration.ipynb`: a jupyter notebook for data exploration.
- `ml_preprocess.ipynb`: a jupyter notebook for preprocessing the data.
- `causal_inference.ipynb`: a jupyter notebook for causal inference feature extraction.
- `ml_model.ipynb`: a jupyter notebook for machine learning model training.

### [scripts](scripts):

- `scripts/`: folder where modules are stored.
- `causality.py`: a module for causal inference.
- `data_manipulation.py`: a module for data manipulation.
- `data_exploration.py`: a module for data exploration.
- `data_preProcessing.py`: a module for data preprocessing.

### [tests](tests):

- `tests/`: the folder containing unit tests for the scripts.
- `test.py`: the file containing unit tests for the scripts.

### [root folder](#)

- `requirements.txt`: a text file listing the projet's dependancies.
- `.travis.yml`: a configuration file Travis CI for unit test.
- `setup.py`: a configuration file for installing the scripts as a package.
- `results.txt`: a text file containing the results of the cml report.
- `train.py`: a script for training the model.
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

<hr>

# <a name='Installation guide'></a>Installation guide

### <a name='conda'></a>Conda Enviroment

```bash
conda create --name causality python==3.8
conda activate causality
```

### Next

```bash
git clone https://github.com/Abel-Blue/breastCancer-causal-Inference.git
cd breastCancer-causal-Inference
sudo python3 setup.py install
```

<hr>

# <a name='license'></a>License

[MIT-License](https://github.com/Abel-Blue/breastCancer-causal-Inference/blob/main/LICENSE)

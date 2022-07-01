
from log import App_Logger
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import os
sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')
sys.path.append(os.path.abspath(os.path.join('..')))

app_logger = App_Logger("../logs/data_exploration.log").get_app_logger()


class exploration:

    def __init__(self) -> None:
        '''
        # Initialize the class
        '''
        self.logger = App_Logger(
            "../logs/data_exploration.log").get_app_logger()

    def plot_heatmap(self, df: pd.DataFrame, title: str, cbar=False) -> None:
        ''' 
        heatmap: Plot rectangular data as a color-encoded matrix.
        heatmap of the dataframe
        cbar: Whether to draw a colorbar.
        title: Title of the plot
        df: dataframe to be plotted
        '''

        plt.figure(figsize=(13, 8))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=20, fontweight='bold')
        plt.show()
        self.logger.info(f"Plot rectangular data as a color-encoded matrix\
        of the dataframe")

    def plot_heatmap_from_correlation(self, correlation, title: str):
        '''
        heatmap: Plot rectangular data as a color-encoded matrix and correlation matrix.
        title: Title of the plot
        correlation: correlation matrix
        '''
        plt.figure(figsize=(14, 9))
        sns.heatmap(correlation)
        plt.title(title, size=18, fontweight='bold')
        plt.show()
        self.logger.info(
            f"Plot rectangular data as a color-encoded matrix and correlation matrix.")

    def plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        '''
        # scatter: Plot data as a scatter plot.
        # df: dataframe to be plotted
        # x_col: x-axis column
        # y_col: y-axis column
        # title: Title of the plot
        # hue: hue column
        '''
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()
        self.logger.info(f"Plot data as a scatter plot.")

    def simple_plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
        '''
        df: dataframe to be plotted
        x_col: x-axis column
        y_col: y-axis column
        title: Title of the plot
        '''
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()
        self.logger.info(f"Plot a simple scatter plot.")

    def plot_hist(self, df: pd.DataFrame, column: str, color: str) -> None:
        '''
        # hist: Plot a histogram.
        # df: dataframe to be plotted
        # column: column to be plotted
        # color: color of the histogram
        '''
        sns.displot(data=df, x=column, color=color,
                    kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()
        self.logger.info(f"Plot a histogram.")

    def plot_bar(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
        '''
        # bar: Plot a bar chart.
        # df: dataframe to be plotted
        # x_col: x-axis column
        # y_col: y-axis column
        # title: Title of the plot
        # xlabel: x-axis label
        # ylabel: y-axis label
        '''
        plt.figure(figsize=(12, 7))
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show()
        self.logger.info(f"Plot a bar chart.")

    def plot_box(self, df: pd.DataFrame, x_col: str, title: str) -> None:
        '''
        # box: Plot a box plot.
        # df: dataframe to be plotted
        # x_col: x-axis column
        # title: Title of the plot
        '''
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()
        self.logger.info(f"Plot a box plot.")

    def plot_box_multi(self, df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
        '''
        # box_multi: Plot a box plot.
        # df: dataframe to be plotted
        # x_col: x-axis column
        # y_col: y-axis column
        # title: Title of the plot
        '''
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()
        self.logger.info(f"Plot a box plot.")

    def plot_count(self, df: pd.DataFrame, column: str) -> None:
        '''
        # count: Plot a count plot.
        # df: dataframe to be plotted
        # column: column to be plotted

        '''
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()
        self.logger.info(f"Plot a count plot.")

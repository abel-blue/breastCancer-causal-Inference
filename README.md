#

<h1 align="center">Breast Cancer diagnosis with Causal Inference</h1>
<div>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/network/members"><img src="https://img.shields.io/github/forks/Abel-Blue/agriTech-USGS-LiDAR" alt="Forks Badge"/></a>
<a href="https://github.com/Abel-Blue/agriTech-USGS-LiDAR/pulls"><img src="https://img.shields.io/github/issues-pr/Abel-Blue/breastCancer-causal-Inference" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/issues"><img src="https://img.shields.io/github/issues/Abel-Blue/breastCancer-causal-Inference" alt="Issues Badge"/></a>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Abel-Blue/breastCancer-causal-Inference?color=2b9348"></a>
<a href="https://github.com/Abel-Blue/breastCancer-causal-Inference/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Abel-Blue/breastCancer-causal-Inference?color=2b9348" alt="License Badge"/></a>
</div>

</br>

![lidar-heatmap](https://www.inovex.de/wp-content/uploads/2020/03/Causal-Inference-Hero.png)

<!-- ## Presentation Slide

- [Rossmann Pharmaceutical Sales prediction](https://www.canva.com/design/DAFBtdnLoKQ/hxJHGTgvoTwJMX9hXbbGVA/view?utm_content=DAFBtdnLoKQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Data visualization link

- [visualization link](https://share.streamlit.io/abel-blue/pharmaceutical-sales-prediction/main/app.py)

## Articles

- [Medium Article](https://medium.com/@Abel-Blue/pharmaceutical-sales-prediction-using-a-deep-learning-model-92d7d1e9626b) -->

## Table of Contents

- [Introduction](##Introduction)
- [Project Structure](#project-structure)
  - [data](#data)
  - [notebooks](#notebooks)
  - [scripts](#scripts)
  - [tests](#tests)
  - [logs](#logs)
  - [root folder](#root-folder)
- [Installation guide](#installation-guide)

<hr>

## Introduction

> <p>Causal inference is an important link between the practice of cancer epidemiology and effective cancer prevention.</p>
> <p></p>

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

### [.vscode](.vscode):

- `.vscode/`: the folder where local path are stored.

### [notebooks](notebooks):

- `notebooks`: a jupyter notebook for preprocessing the data.

### [scripts](scripts):

- `scripts/`: folder where modules are stored.

### [tests](tests):

- `tests/`: the folder containing unit tests for the scripts.

### root folder

- `requirements.txt`: a text file lsiting the projet's dependancies.
- `.travis.yml`: a configuration file for Travis CI for unit test.
- `setup.py`: a configuration file for installing the scripts as a package.
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

<hr>

# <a name='Installation guide'></a>Installation guide

### <a name='conda'></a>Conda Enviroment

```bash
conda create --name mlenv python==3.8.1
conda activate mlenv
```

then

```bash
git clone https://github.com/Abel-Blue/breastCancer-causal-Inference.git
cd breastCancer-causal-Inference
sudo python3 setup.py install
```

<hr>

# <a name='license'></a>License

[MIT](https://github.com/Abel-Blue/breastCancer-causal-Inference/blob/main/LICENSE)

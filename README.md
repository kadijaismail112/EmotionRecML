# EmotionRecML

EmotionRecML is a project that focuses on emotion recognition using deep learning techniques. It utilizes a ResNet architecture to classify facial expressions into different emotion categories. The project also explores the use of a Mixture of Experts (MoE) model to improve classification accuracy and reduce confusion between highly confused emotion classes.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Experiments](#experiments)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project environment, follow these steps:

1. Clone the repository: 
`git clone https://github.com/kadijaismail112/EmotionRecML`

2. Navigate to the project directory:
`cd EmotionRecML`

3. Create a new conda environment using the provided `environment.yml` file:
`conda env create -f environment.yml`

4. Activate the conda environment:
`conda activate EmotionRecML`

5. Launch Jupyter Notebook:
`jupyter notebook`


## Usage

1. Once Jupyter Notebook is launched, navigate to the project directory in the notebook interface.

2. Open the desired notebook file (e.g., `emotion_recognition.ipynb`) to start working on the project.

3. Follow the instructions and code provided in the notebook to train the models, evaluate their performance, and conduct experiments.

4. Modify the code and experiment with different configurations as needed.

## Dataset

The project uses the FER2013 dataset for facial emotion recognition. The dataset consists of grayscale images of faces labeled with seven emotion categories: angry, disgust, fear, happy, sad, surprise, and neutral.

The dataset is preprocessed and split into training, validation, and testing sets. Data augmentation techniques are applied to the training set to improve model generalization.

## Model Architecture

The project utilizes a ResNet architecture as the base model for emotion classification. The ResNet model is modified to accept grayscale images as input.

In addition to the single ResNet model, a Mixture of Experts (MoE) model is explored to improve classification accuracy. The MoE model consists of multiple expert networks (ResNet architectures) specialized in classifying specific subsets of emotions. A gating network is used to assign weights to each expert based on the input features.

## Experiments

Several experiments are conducted to evaluate the performance of the models and investigate the effectiveness of the MoE approach:

1. Training and evaluating a single ResNet model on the entire dataset.
2. Training and evaluating the MoE model with different expert groupings and configurations.
3. Comparing the performance of the single ResNet model and the MoE model.
4. Analyzing the confusion matrices to assess the reduction in confusion between highly confused emotion classes.

## Results

The project provides detailed results and analysis of the experiments, including:

- Training and validation accuracy curves for the single ResNet model and the MoE model.
- Confusion matrices visualizing the classification performance of the models.
- t-SNE and PCA visualizations of the learned representations.
- Discussion on the effectiveness of the MoE approach in improving classification accuracy and reducing confusion between emotions.

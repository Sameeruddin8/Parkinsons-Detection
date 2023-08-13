# Parkinson's Detection Project 

![image](https://github.com/Sameeruddin8/Parkinsons-Detection/assets/102674044/8e68c1e3-ce7a-44b9-83af-b5fa2942a7b6)


## Introduction

This project focuses on utilizing machine learning techniques, specifically the Support Vector Machine (SVM), to detect Parkinson's disease from biomedical voice measurements. The goal is to create a model that can accurately classify individuals as either having Parkinson's disease or being healthy based on voice features.

## Features

- Utilizes the Parkinson's Disease dataset containing voice measurements of individuals with and without the disease.
- Preprocesses the dataset, cleaning and transforming the data for analysis.
- Extracts relevant acoustic features from voice recordings, such as fundamental frequency and frequency variation.
- Trains a Support Vector Machine classifier on the processed data.
- Evaluates the model's performance using metrics like accuracy, precision, recall, and F1-score.

## Usage

1. **Dataset:** Use the Parkinson's Disease dataset that includes voice recordings from both healthy individuals and those with Parkinson's disease.

2. **Data Preprocessing:** Preprocess the data by cleaning and transforming it into a suitable format for analysis. This may involve handling missing values, scaling features, and splitting the dataset.

3. **Feature Extraction:** Extract acoustic features from the voice recordings, such as jitter, shimmer, and other voice quality measures that are relevant to Parkinson's disease diagnosis.

4. **Model Training:** Train a Support Vector Machine classifier using the extracted features and corresponding labels (healthy or Parkinson's).

5. **Model Evaluation:** Evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score. This step will provide insights into the model's ability to accurately diagnose Parkinson's disease.

6. **Prediction:** Once the model is trained and evaluated, you can use it to predict whether an individual is likely to have Parkinson's disease based on their voice measurements.

## Result

![Alt text](Parkinsons.gif)

## Conclusion

The Parkinson's Detection Project demonstrates the application of machine learning techniques, particularly the Support Vector Machine algorithm, in diagnosing Parkinson's disease from voice measurements. By extracting and analyzing relevant features from voice recordings, we were able to create a model that shows promising results in identifying individuals with the disease. This project showcases the potential of machine learning in assisting medical diagnosis and highlights the significance of accurate and early disease detection.

For a detailed code implementation, dataset references, and comprehensive results, please refer to the project files.

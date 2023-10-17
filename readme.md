# Campus Placement Prediction Project

## Introduction

This project focuses on predicting the placement status of students in a campus recruitment process. The objective is to develop a machine learning model that accurately classifies students as "Placed" or "Not Placed" based on various features.

## Project Overview

In this project, a Support Vector Classification (SVC) model is used to predict placement status. The model has been trained on a dataset containing features such as secondary education percentage, board of education, higher secondary education percentage, degree percentage, work experience, and more. Class imbalance issues are addressed using the Synthetic Minority Over-sampling Technique (SMOTE) from the imbalanced-learn library.

## Features

The dataset includes the following features:

- `ssc_p`: Secondary Education percentage (10th Grade)
- `ssc_b`: Board of Education - Central/Other
- `hsc_p`: Higher Secondary Education percentage (12th Grade)
- `hsc_b`: Board of Education - Central/Other
- `hsc_s`: Specialization in Higher Secondary Education
- `degree_p`: Degree Percentage
- `degree_t`: Under Graduation (Degree type) - Field of degree education
- `workex`: Work Experience
- `etest_p`: Employability test percentage (conducted by the college)
- `specialisation`: Post Graduation (MBA) - Specialization
- `mba_p`: MBA percentage

## Getting Started

To run this project on your local machine, follow these steps:

### Data

You will need the dataset to train and test the model. You can find it in the `train.csv` file under notebooks section.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>


2. Install the dependencies
    create a venv suppoting python==3.8.0 and use command:
    pip install -r requirements.txt

3. Install setup using:
    python setup.py install

### Usage
    use app.py to test the app

### Model Evaluation
    Accuracy: The model achieved an accuracy of 81% in predicting placement status.

### Deployment
    This project is deployed and hosted on Render.
    link: https://campusplacementprediction.onrender.com/

Note: Please be aware that the Render hosting platform may experience a 30-minute inactivity timeout. If the link provided becomes unresponsive, please wait for 1-2 minutes before trying again.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
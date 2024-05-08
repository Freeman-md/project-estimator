# Software Project Development Estimator

## Overview

The **Software Project Development Estimator** is a tool designed to aid project managers and software developers in estimating the effort required to complete software projects, measured in person-months. This project uses machine learning techniques, specifically linear regression, to predict the necessary effort based on a variety of project features. This README provides an in-depth look at the project's background, development process, and access to key resources such as the final report, development documentation, presentation slides, and dataset.

## Repository Contents

- **[Final Report (PDF)](final-report.pdf)** - A detailed document that elaborates on the methodologies, data analysis, and conclusions of the project.

- **[Viva Presentation (PDF)](viva.pdf)** - Presentation slides that summarize the project objectives, processes, findings, and future work.

- **[Development Process Documentation (PDF)](development-process.pdf)** - A document detailing the step-by-step process followed in the development of the estimator, including data preparation, modeling techniques, and evaluation.

- **[Dataset (CSV)](desharnais.csv)** - The dataset used for training the machine learning model, containing historical data on software projects.

- **[Source Code (ZIP)](source-code.zip)** - A compressed file containing all the source code utilized in the project, including scripts for data processing, model training, and prediction.

## Project Description

### Background

The motivation behind the Software Project Development Estimator stems from the need for more accurate and efficient project management tools in the software industry. Traditional estimation methods often fall short in precision and adaptability, prompting the use of advanced data-driven models to enhance prediction accuracy and reliability.

### Development Process

The estimator was developed through a series of structured phases:

1\. **Data Collection** - Utilization of the [Desharnais dataset](desharnais.csv), a comprehensive set of data from previous software projects.

2\. **Feature Engineering** - Analysis and selection of significant features that impact project effort, enhancing the model's predictive power.

3\. **Model Development** - Application of linear regression techniques to develop a predictive model that estimates project efforts based on selected features.

4\. **Evaluation** - Rigorous testing of the model to ensure accuracy and reliability of the predictions.

For a detailed walkthrough of these phases, please refer to the [Development Process Document](development-process.pdf).

### Tool Functionality

The estimator is designed to be user-friendly, available both as a command-line application and a graphical user interface (GUI). It allows users to input project details and receive an estimated effort in person-months.

## Usage

To utilize the estimator tool, follow these steps:

1\. Download and extract the [source code](source-code.zip).

2\. Ensure that Python and all necessary libraries, listed in `requirements.txt` within the source code, are installed.

3\. Run the command-line application or GUI as per the instructions within the source code documentation to input project features and receive effort estimations.

## Further Information

For more detailed information on the modeling techniques, data analysis, and findings, please refer to the [Final Report](final-report.pdf). Additionally, the [Viva Presentation](viva.pdf) provides a concise overview of the project and its impact.

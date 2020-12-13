# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

# Contextual Twitter Sarcasm Detection
## CS 410: Text Information Systems Final Project
This repository contains the project code, data, report and video presentation for text classification competition.

## Code environment
We are running our code on the google colab platform. You will need:
- Python 3.x
- transformers
- torch
- pandas
- sklearn

All packages are pre-installed except transformers.

## Model
Due to the limit of file size on Github, we are not able to upload our final saved model to the github repository. Therefore, we created a google drive link to share our final model:
https://drive.google.com/file/d/1bFc4HK1N7pneVfDeVwESM3TehEK4o44w/view?usp=sharing

## Setup
1. In Colab Notebooks under Google Drive, create a directory called TextClassification.
2. Within the TextClassification directory, create another directory called data.
3. Include the data files (test.jsonl and train.jsonl) in this data directory.
4. From the GitHub repository (https://github.com/samphadnis/TeamTextDragons), open roberta_no_pretrain.ipynb from the code directory into Colab Notebooks.
5. Since the saved model is too large to be uploaded to Github, we created a link to google drive and shared it on Github readme page. Download the model and save it under the TextClassification directory.
6. If you want to run the whole model, including the training portion, in the navbar, navigate to “Runtime” and select “Run all”. The pipeline should run, and the results answer.txt should be generated under Colab Notebooks.
7. If you only want to generate the results with the saved model, you may skip the Model Training portion of the code.

The subfolders should be organized as below:
```
    .
    ├── ...
    ├── Colab Notebooks
    │   ├── TextClassification
    |   |   ├── data
    |   |   |   ├──train.jsonl
    |   |   |   ├──test.jsonl
    |   |   ├── roberta_no_pretrain.ipynb
    |   |   └── model_RoBERTa_relu_nopretrain.pkl
    └── 
```


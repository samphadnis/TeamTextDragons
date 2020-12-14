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
    |   └── 
    └── 
```

## Presentation
We created a video presentation to walk through the code and shows how to reproduce the results. The video can be found: https://mediaspace.illinois.edu/media/1_79uj7ghe.


## File Description
- Reports:
    * CS410_ Project Proposal_TextDragons.pdf - Project proposal
    * CS410 Project Progress Report.pdf - Project progress report
- Code:
    * code/Profiling.ipynb - Pre-modeling analysis
    * code/roberta_no_pretrain.ipynb - Our best model, which uses roberta + relu
    * code/roberta_no_pretrain_softmax.ipynb - roberta + softmax
    * code/xlmroberta_no_pretrain.ipynb - xlmroberta + relu
    * code/albert.ipynb - albert + relu
    * code/Fasttext.ipynb - Fast text model
    * code/clean.py - Data preprocessing script
- Data:
    * data/train.jsonl - labeled training data
    * data/test.jsonl - unlabeled testing data

## Reference
Kozlov, Alexander. “Fine-Tuning BERT and RoBERTa for High Accuracy Text Classification in PyTorch.” Medium, Towards Data Science, 7 Sept. 2020, towardsdatascience.com/fine-tuning-bert-and-roberta-for-high-accuracy-text-classification-in-pytorch-c9e63cf64646. 
The code repository we relied on can be found here: https://github.com/aramakus/ML-and-Data-Analysis/blob/master/RoBERTa%20for%20text%20classification.ipynb
“Transformers.” Transformers - Transformers 4.0.0 Documentation, huggingface.co/transformers/index.html. 
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, Veselin Stoyanov: “RoBERTa: A Robustly Optimized BERT Pretraining Approach”, 2019; http://arxiv.org/abs/1907.11692 arXiv:1907.11692
Amardeep Kumar, Vivek Anand: “Transformers on Sarcasm Detection with Context”, 2020; https://www.aclweb.org/anthology/2020.figlang-1.13.pdf

# Application of Machine-Learning Algorithms to Detect AI-generated Content

  

Welcome to the repository for the thesis titled "Application of Machine-Learning Algorithms to Detect AI-generated Content".

This repository contains the essential files related to the thesis.

  
------------------------------------
## Description

### datasets:
This directory contains all the data sets that are used to train the models. While the data sets that have been created newly are in a dedicated directory, the provided data sets are at the top level. 
  #### Generated Datasets:
  This repository contains all the datasets described above. responsesLlama.csv and responsesMistral.csv had been created by myself using capacities of the university. 

------------------------------------

### evaluation: 
This directory contains all the measurements used to analyze the models. Graphics  and charts that are cited in the written part from this repository can be found here. 
  #### Cross-Validation
  Contains measurements about the Cross Validation procedure.
  #### GPT35_Evaluation
  Contains measurements about the GPT 3.5 dataset.
  #### GPTNeo_Evaluation
  Contains measurements about the GPT Neo dataset.
  #### Llama3_Evaluation
  Contains measurements about the Llama 3 dataset.
  #### Mistral_Evaluation
  Contains measurements about the Mistral dataset.

------------------------------------

### LLMs
In this directory, the Large-Language-Models Llama3 and Mistral are deployed and executed. When executing the run files, it should be ensured that a sufficient graphics card is available, as the code is optimised for this and these models do not actually run without a graphics card. The datasets that are created are stored directly in the datasets directory.
  #### Llama3
  Contains the code for executing the Llama3 model locally. 
  #### Mistral
  Contains the code for executing the Mistral model locally. 

------------------------------------

### model
The model directory contains the implementation of each classifier. Each classifier is applied on each dataset individually as well as the ensemble models. The evaluation metrics are stored directly in the evaluation directory. The ensemble models just load the classifiers from the pickle directory, therefore, no additional computation is needed to run them.
  #### CrossValidation
  Contains the Cross-Validation-models for each data set. This means each pre-trained model is applied on each data-set. The particularity here is that each pre-trained model has been trained on 100% of the available training data.
  #### Ensemble
  Contains the ensemble-models for each data set.
  #### LogisticRegression
  Contains the logistic regression models for each data set.
  #### pickle
  This directory contains all of the executed models and saves them by model and data set. Important: The saved files are overwritten if a model file is executed. 
  #### RandomForest
  Contains the random forest models for each data set.
  #### SupportVectorMachine
  Contains the support vector machine models for each data set.

------------------------------------

### preprocessing
This directory contains the files to preprocess each data-set. Each prepared data-set is stored in the storePreprocess subdirectory. 

DOI:

[![DOI](https://zenodo.org/badge/797248220.svg)](https://zenodo.org/doi/10.5281/zenodo.11408376)

# Application of Machine-Learning Algorithms to Detect AI-generated Content

  

Welcome to the repository for the thesis titled "Application of Machine-Learning Algorithms to Detect AI-generated Content".

This repository contains the essential files related to the thesis.

  

## Description

### datasets:
This directory contains all the data sets that are used to train the models. While the data sets that have been created newly are in a dedicated directory, the provided data sets are at the top level. 

### evaluation: 
This directory contains all the measurements used to analyze the models. Graphics  and charts that are cited in the written part from this repository can be found here. 

### LLMs
In this directory, the Large-Language-Models Llama3 and Mistral are deployed and executed. When executing the run files, it should be ensured that a sufficient graphics card is available, as the code is optimised for this and these models do not actually run without a graphics card. The datasets that are created are stored directly in the datasets directory. 

### models
The model directory contains the implementation of each classifier. Each classifier is applied on each dataset individually as well as the ensemble models. The evaluation metrics are stored directly in the evaluation directory.

### preprocessing
This directory contains the files to preprocess each data-set. Each prepared data-set is stored in the storePreprocess subdirectory. 

DOI:

[![DOI](https://zenodo.org/badge/797248220.svg)](https://zenodo.org/doi/10.5281/zenodo.11408376)
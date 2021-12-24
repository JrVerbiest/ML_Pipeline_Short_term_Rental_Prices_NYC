# Build an ML Pipeline for Short-term Rental Prices in NYC

## Meets Specifications 

Udacity Student ![:udacious:](https://review.udacity.com/assets/images/emojis/udacious.png)

You have done an amazing job in this project and it will open a huge door in your future work. MLOps is a very important topic on every field of machine learning. If you want models into production and reliable pipelines, you are on the right path!

As a reference, I would like to share some articles and resources to boost your learning:

[MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

[MLOps: What It Is, Why it Matters, and How To Implement It (from a Data Scientist Perspective)](https://neptune.ai/blog/mlops-what-it-is-why-it-matters-and-how-to-implement-it-from-a-data-scientist-perspective)

[MLOps Core](https://ml-ops.org/content/references.html)

[10 Amazing MLOps Learning Resources](https://medium.com/analytics-vidhya/10-amazing-mlops-learning-resources-378804c418be)

[MLOps-Reducing the technical debt of Machine Learning](https://medium.com/mlops-community/mlops-reducing-the-technical-debt-of-machine-learning-dac528ef39de)

I really hope you enjoy the project as we mentors did and we are looking forward your next step!

## W&B Set-Up 

Your W&B project nyc_airbnb should be made public, so that your reviewer can access it. This is needed so the reviewer can check that the W&B steps have been executed successfully.

**Make sure the link to your W&B project, as well as your Github repository (i.e. two links), are included in a README file or given to the reviewer in the "Submission Details" box you can use when initiating the submission process.**

## W&B Set-Up

### W&B Project and Github

Great! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

Your Github and W&B project are public!

## Exploratory Data Analysis 

There is a sample.csv artifact in W&B.

The pipeline has been run to get a sample of the data, which has been uploaded to W&B.

## Exploratory Data Analysis

### Sample Dataset Artifact

Great job here as well! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

When running your pipeline, it is possible to get the sample of the data, which has been uploaded to W&B.

There is a notebook called EDA in the students’ repository (most probably in the src/eda directory).

The EDA notebook contains a properly formatted Jupyter notebook with comments and markdown cells.

## Exploratory Data Analysis

### EDA Notebook

Great! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

Your Github repository contains a properly formatted Jupyter notebook.

[![Screenshot_1.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280015/Screenshot_1.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280015/Screenshot_1.png)

At the beginning of the notebook, fetch the sample.csv artifact from W&B.

## Exploratory Data Analysis

### W&B Fetching Artifact from W&B

Perfect! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

At the beginning of your notebook, you fetch the *sample.csv* artifact from your W&B.

[![Screenshot_2.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280025/Screenshot_2.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280025/Screenshot_2.png)

The data is clean at the end of the notebook. Note that there will still be some missing entries, because we are not imputing missing values.

Properly implemented the checks suggested in the `notes.md` file.

## Exploratory Data Analysis

### Data Cleaning

At the end of the notebook, we can verify that the data is clean and without any other issue.

[![Screenshot_3.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280034/Screenshot_3.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280034/Screenshot_3.png)

## Data Cleaning 

There is a new “basic_cleaning” step in the Github repository (under the src directory).

The basic_cleaning step respects the MLFlow structure: a conda.yml, a MLproject and a python script. It has the parameters input_artifact, output_name, output_type, output_description, min_price and max_price.

## Data Cleaning

### The *“basic_cleaning”* Step

Perfect! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

Your *“basic_cleaning”* step respects the MLFlow structure:

![:heavy_check_mark:](https://review.udacity.com/assets/images/emojis/heavy_check_mark.png) - conda.yml
![:heavy_check_mark:](https://review.udacity.com/assets/images/emojis/heavy_check_mark.png) - MLproject
![:heavy_check_mark:](https://review.udacity.com/assets/images/emojis/heavy_check_mark.png) - python script 

[![Screenshot_4.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280043/Screenshot_4.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280043/Screenshot_4.png)

The conda.yml file has been updated to add the `pandas` dependency.

## Data Cleaning

### Pandas Dependency

You have set the pandas dependency in your *.yml* file! 

[![Screenshot_5.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280053/Screenshot_5.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280053/Screenshot_5.png)

Add docstrings and the proper type to all parameters, both in the script and in the MLproject file.

## Data Cleaning

### MLproject docstring

You have added the docstring to your MLproject file!

I would like to share some useful information to boost your learning path:

[Create Reusable ML Modules with MLflow Projects & Docker](https://towardsdatascience.com/create-reusable-ml-modules-with-mlflow-projects-docker-33cd722c93c4)

[![Screenshot_6.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280063/Screenshot_6.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280063/Screenshot_6.png)

The basic_cleaning step re-implements in a MLFlow step the data cleaning you performed during the EDA. It should be added to the main.py file and run without errors.

In the main.py file all parameters are taken from the configuration file, and not hard-coded.

## Data Cleaning

### The *“basic_cleaning”* Step - MLFlow

Great job! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

In your *main.py* file, all parameters are coming from the configuration file and they are not hard coded. It is very important in the MLFlow framework so we can reproduce your code faster.

At the end of the run of this step, there should be a clean_data.csv artifact uploaded to W&B.

## Data Cleaning

### The *clean_data.csv* Artifact

Awesome! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

At the end of the run of this step, it is possible to check the *clean_data.csv* artifact in the W&B.

[![Screenshot_7.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280083/Screenshot_7.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280083/Screenshot_7.png)

## Data Testing 

In W&B, manually add a tag called “reference” to the latest version of the clean_sample.csv artifact. 

## Data Testing

### Tag *reference*

You have correctly added the tag *reference* to the latest version of the *clean_sample.csv* artifact.

Implements the test_row_count and the test_price_range tests in src/data_check/test_data.py.

The added tests are checking respectively for a proper size of the dataset, and for a proper price range.

## Data Testing

### The *test_row_count* Test

Perfect!

You have implemented the tests correctly!

The pipeline runs after this step, and all the tests pass.

## Data Testing

### Test Pepiline

Awesome! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

The pipeline runs after all tests and you have passed in all of them!

## Data Splitting 

Adds the train_val_test_split component to the main.py file.

The train_val_test_split has been provided to you. You can just add it to the `main.py` file and fill in the parameters appropriately.

## Data Splitting

### The *train_val_test_split* Component

You have added the *train_val_test_split* component to the main file.

The pipeline runs. At the end there should be 2 new artifacts on W&B: trainval_data.csv, test_data.csv.

## Data Splitting

### Two New Artifacts Added to W&B

Great job! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

At the end of the run the two new artifacts are on W&B.

## Train the Random Forest 

The `src/train_random_forest/run.py` script is completed.

When checking the script, there should be the following steps in the script, marked by clear comments:

1. Download the train data using W&B.
2. In the get_inference_pipeline function, implement a pipeline called `non_ordinal_categorical_preproc` with two steps: a `SimpleImputer(strategy="most_frequent")` and a `OneHotEncoder()` step
3. In the `get_inference_pipeline` function, create the inference pipeline called `sk_pipe` containing the preprocessing step and the Random Forest
4. In the go function, fit the pipeline.
5. In the go function, export the pipeline using MLFlow model export.
6. Upload the artifact to W&B
7. Log the variable MAE to W&B

## Train the Random Forest

### Script is Complete

Perfect! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

Your *run.py* at `src/train_random_forest/run.py` is complete and using the `sklearn Pipeline`.

The pipeline again runs successfully.

The `train_random_forest` step is added to the `main.py` file.

## Train the Random Forest

### Train Random Forest Step

In your `main.py`you have implemented the `train_random_forest`step.

There should be an artifact created on W&B called model_export.

The model_export artifact should contain a MLflow sklearn serialized model.

## Train the Random Forest

### *model_export* Artifact

Great job! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

At the end of this step, there is an Artifact called *Model_Export* in your W&B!

[![Screenshot_8.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280128/Screenshot_8.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280128/Screenshot_8.png)

## Optimize Hyperparameters 

Using the Hydra system, run a hyper-parameter search.

On W&B there should be the results of several (>2) training jobs with different hyperparameters.

## Optimize Hyperparameters

Great job! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

## Select the Best Model 

Add the tag “prod” to the trained model with the best MAE.

## Select the Best Model

Awesome job! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

You have added the tag `prod` to the trained model with the best MAE.

To boost your learning, there are two nice articles I would like to share:

- [How to Choose Right Metric for Evaluating ML Model](https://www.kaggle.com/vipulgandhi/how-to-choose-right-metric-for-evaluating-ml-model)
- [Evaluation metrics & Model Selection in Linear Regression](https://towardsdatascience.com/evaluation-metrics-model-selection-in-linear-regression-73c7573208be)

## Test Set Verification 

Implement the `test_regression_model` function in the `main.py` file. The test_regression_model is provided just as in the “data splitting” step.

Verify that the performance is comparable to what was obtained against the validation set (i.e. no overfitting occurred).

## Test Set Verification

### *test_regression_model* Function

The `test_regression_model`function in the `main.py`file is implemented.

## Visualize the Pipeline 

Navigate to W&B, to the artifact section, then click on “Graph view”. The resulting visualization should show the pipeline properly organized. Refer to the reference plot in notes.md.

## Visualize the Pipeline

### Pipeline Graph View

Nice job! ![:wink:](https://review.udacity.com/assets/images/emojis/wink.png)

[![Screenshot_9.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280155/Screenshot_9.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280155/Screenshot_9.png)

## Release the Pipeline 

A release of the pipeline is cut from the Github repository, with version 1.0.0 or similar (if you need more trials, you might assign versions like 1.0.1 or 1.0.2, which is totally fine).

## Release the Pipeline

### Pipeline Release on Github

Perfect! ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

You have released your pipeline in your Github account.

Releasing pipelines on any git system is a very important skill you should deep your learning. For this reason, I would like to share more three articles with you:

- [Releasing projects on GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github)
- [Using Release It!](https://medium.com/@webprolific/using-release-it-60b96515c073)
- [Gitflow: The easy release management workflow](https://medium.com/@asappstudio/gitflow-the-easy-release-management-workflow-7d4142991049)

[![Screenshot_10.png](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280165/Screenshot_10.png)](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/230781/1640280165/Screenshot_10.png)

## Train the Model on a New Data Sample 

Run the released pipeline on a new sample of data, sample2.csv. The first version 1.0.0 (or similar) should fail, because there is a data problem in sample2.csv.

## Train the Model on a New Data Sample

### Released Pipeline Run

You have correctly set your project. ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

Implement a new cleaning step that removes data points that are outside of the area of NYC in `basic_cleaning`. 

## Train the Model on a New Data Sample

### New Cleaning Step

Perfect! A new step cleaning is implemented.

After adding the new cleaning step and committing and pushing to the repository, release a new version (for example, 1.0.1).

## Train the Model on a New Data Sample

### New Release

Great job adding the new cleaning step. You have committed and pushed to the repository. You have released a new version as requested. ![:smile:](https://review.udacity.com/assets/images/emojis/smile.png)

Re-running with the new release should produce a new trained model.


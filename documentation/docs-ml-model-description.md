# heart-attack-class model description

For purpose of the assignment there was heart attack risk dataset selected. Choose of this dataset required multiple
changes in the preproc.py, train.py and predict.py scripts to make sure that data is properly transformed
and model is getting trained.

**Link to the dataset:** https://www.kaggle.com/competitions/heart-attack-risk-analysis

## Dataset description
**Columns**
- **Patient ID** - Unique identifier for each patient
- **Age** - Age of the patient
- **Sex** - Gender of the patient (Male/Female)
- **Cholesterol** - Cholesterol levels of the patient
- **Blood Pressure** - Blood pressure of the patient (systolic/diastolic)
- **Heart Rate** - Heart rate of the patient
- **Diabetes** - Whether the patient has diabetes (Yes/No)
- **Family History** - Family history of heart-related problems (1: Yes, 0: No)
- **Smoking** - Smoking status of the patient (1: Smoker, 0: Non-smoker)
- **Obesity** - Obesity status of the patient (1: Obese, 0: Not obese)
- **Alcohol Consumption** - Level of alcohol consumption by the patient (None/Light/Moderate/Heavy)
- **Exercise Hours Per Week** - Number of exercise hours per week
- **Diet** - Dietary habits of the patient (Healthy/Average/Unhealthy)
- **Previous Heart Problems** - Previous heart problems of the patient (1: Yes, 0: No)
- **Medication Use** - Medication usage by the patient (1: Yes, 0: No)
- **Stress Level** - Stress level reported by the patient (1-10)
- **Sedentary Hours Per Day** - Hours of sedentary activity per day
- **Income** - Income level of the patient
- **BMI** - Body Mass Index (BMI) of the patient
- **Triglycerides** - Triglyceride levels of the patient
- **Physical Activity Days Per Week** - Days of physical activity per week
- **Sleep Hours Per Day** - Hours of sleep per day
- **Country** - Country of the patient
- **Continent** - Continent where the patient resides
- **Hemisphere** - Hemisphere where the patient resides
- **Heart Attack Risk** - Presence of heart attack risk (1: Yes, 0: No)

In the project it was decided to use all features to train the model as every one of them might
be an important factor of heart attacks.

To have a correct numerical representation of all features it was decided
to split `Blood Pressure` into to additional features:
- `SYS` - for systolic blood pressure
- `DIA` - for diastolic blood pressure

Original column `Blood Pressure` is later removed from model to not duplicate the features.
Additionally format of data in this column was incorrect to use it, hence the split for SIA and DIA.

## Choice of the model

Model selected to serve the purpose was: `CatBoostClassifier` from `catboost` library.
It was decided to use this model as based on following factors:
- It is a readymade classifier in scikit-learn’s conventions terms that would deal with categorical
 features automatically.
- It can work with diverse data types to help solve a wide range of problems.
- It has a very good documentation available.

Additionally, `CatBoostClassifier` has very good performance, is robust and easy to use.

## Process steps

### Verification of variables used in config.py

- [Configuration file](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/DSML/config.py)

Before any actions on the dataset could be started there were multiple variables added to the configuration file.

- **PROJ_ROOT** - root path of the project, used as reference for other paths
- **DATASET** - name of the dataset used to train the model; competition dataset from Kaggle
- **DATASET_TEST** - name of the dataset used to test the model and make predictions
- **DATA_DIR** - path to the folder with data
- **RAW_DATA_DIR** - path to folder with raw data downloaded from Kaggle
- **INTERIM_DATA_DIR** - path to temp folder used for interim data storage
- **PROCESSED_DATA_DIR** - path to folder with processed data
- **EXTERNAL_DATA_DIR** - path to folder with external data used in the preproc process
- **MODELS_DIR** - path to the folder with localy stored model files
- **REPORTS_DIR** - path to the folder with localy stored reports
- **FIGURES_DIR**- path to the folder with localy stored figures and plots
- **MODEL_NAME**  - string variable containing name of the model
- **categories_mapping** - dictionary with mappings used for categorical data encoding - currently out of use
- **categorical** - list of categorical fields in dataset
- **columns_to_convert** - list of fields that requires data type change - currently out of use
- **target** - name of the field used for predictions

### Data Preprocessing

Raw dataset requires multiple steps to preprocess data before they will be used in training and predictions.
Steps done in that process have been listed below. Exact code can be found here: [preproc.py](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/DSML/preproc.py)

1. Download dataset from kaggle.com with use of API connection
1. Replace whitespaces in column names with underscore `_` to avoid data processing errors
1. Split `Blood_Pressure` column to get `SYS` and `DIA` values
1. Drop `Blood_Pressure` column
1. Save preprocessed data as `train.csv` file
1. Repeat steps 2-5 for test data; aave preprocessed data as `test.csv`

### Training of the model

Training is done with use of the previously processed files.
Training has been split in the following steps:

1. Change categorical data into integers representing number of class based on `categorical` variable
1. Register new experiment in MLflow or get the existing one
1. Run optuna hyperparameter tuning
1. Load the best parameters
1. Do cross-validated training with use of the parameters from previous step
1. Register new experiment for full dataset training
1. Train model on full dataset without cross-validation

Exact code can be found here: [train.py](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/DSML/train.py)

### Resolution of model challenge

Before predictions are being made there is a challenge resolution actions done by the workflow.
Resolution is being done by [resolve.py](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/DSML/resolve.py).

Logic of the challenge resolution is as follows.
![Challenge Resolution](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/documentation/attachments/challenge.png)

### Predictions

Once the best model was found the prediction process can be executed.
Data used in the predictions is saved as `test.csv` in `processed` folder.

Steps executed in the process:

1. Load `test.csv` file
1. Get the best or latest model from MLflow
1. Extract model metrics
1. Load the model
1. Get model artifacts
1. Predict results with use of the model and extracted parameters
1. Create new experiment for predictions
1. Calculate UDC
1. Log predictions in as artifact in S3 bucket

Exact code can be found here: [predict.py](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/DSML/predict.py)

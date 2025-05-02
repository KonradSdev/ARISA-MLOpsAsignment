"""Functions for preprocessing the data."""

import os
from pathlib import Path
import re
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi
from loguru import logger
import pandas as pd

from DSML.config import DATASET, DATASET_TEST, PROCESSED_DATA_DIR, RAW_DATA_DIR,categories_mapping


def get_raw_data(dataset:str=DATASET, dataset_test:str=DATASET_TEST)->None:
    api = KaggleApi()
    api.authenticate()

    download_folder = Path(RAW_DATA_DIR)
    zip_path = download_folder / "heart-attack.zip"

    logger.info(f"RAW_DATA_DIR is: {RAW_DATA_DIR}")
    api.competition_download_files(dataset, path=str(download_folder))
    api.dataset_download_files(dataset_test, path=str(download_folder), unzip=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(str(download_folder))

    Path.unlink(zip_path)

def replace_whitespace_in_columns(df):
  """
  Replaces whitespace characters in DataFrame column names with underscores.
  """
  new_columns = [col.replace(" ", "_") for col in df.columns]
  df.columns = new_columns
  return df

def encode_data(df, mapping_dict):
    """
    Changes categorical values into numeric based on mapping provided in config file.
    """
    for column_name in mapping_dict.keys():
        df = df[column_name].map(mapping_dict[column_name].values())
    return df
    

def preprocess_df(file:str|Path)->str|Path:
    """Preprocess datasets."""
    _, file_name = os.path.split(file)
    df_data = pd.read_csv(file)

    # Change whitespaces in dataframe to '_'
    df_data = replace_whitespace_in_columns(df_data)

    # Encode categorical values
    df_data = encode_data(df_data,categories_mapping)

    # Split Blood Pressure values into two columns to have numeric representation of SYS and DIA values
    df_data[["SYS", "DIA"]] = df_data["Blood_Pressure"].str.split('/', expand=True)

    # Drop obsolete columns
    df_data = df_data.drop(columns=["Patient_ID","Blood_Pressure"], axis=1)

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    outfile_path = PROCESSED_DATA_DIR / file_name
    df_data.to_csv(outfile_path, index=False)

    return outfile_path


if __name__=="__main__":
    # get the train and test sets from default location
    logger.info("getting datasets")
    get_raw_data()

    # preprocess both sets
    logger.info("preprocessing train.csv")
    preprocess_df(RAW_DATA_DIR / "train.csv")
    logger.info("preprocessing test.csv")
    preprocess_df(RAW_DATA_DIR / "test.csv")

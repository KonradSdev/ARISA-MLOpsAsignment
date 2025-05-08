"""Config file for module."""
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger
import os

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
ARTIFACT_BUCKET = os.environ.get('ARTIFACT_BUCKET')
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATASET = "heart-attack-risk-analysis"  # original competition dataset
DATASET_TEST = "iamsouravbanerjee/heart-attack-prediction-dataset"  # test set augmented with target labels

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = f"s3://{ARTIFACT_BUCKET}/models"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

MODEL_NAME = "heart-attack-class"

categories_mapping = {
    "Country":  {
                "Argentina":0,
                "Australia":1,
                "Brazil":2,
                "Canada":3,
                "China":4,
                "Colombia":5,
                "France":6,
                "Germany":7,
                "India":8,
                "Italy":9,
                "Japan":10,
                "New Zealand":11,
                "Nigeria":12,
                "South Africa":13,
                "South Korea":14,
                "Spain":15,
                "Thailand":16,
                "United Kingdom":17,
                "United States":18,
                "Vietnam":19
                },
    "Continent":{
                "Africa":0,
                "Asia":1,
                "Australia":2,
                "Europe":3,
                "North America":4,
                "South America":5
                },
    "Hemisphere":{
                "Northern Hemisphere":0,
                "Southern Hemisphere":1
                },
    "Sex":      {
                "Female":0,
                "Male":1
                },
    "Diet":     {
                "Unhealthy":0,
                "Average":1,
                "Healthy":2
                }
    }

categorical = [
                "Sex",
                "Diet",
                "Country",
                "Continent",
                "Hemisphere"
                ]

columns_to_convert = [
        "Exercise_Hours_Per_Week",
        "Sedentary_Hours_Per_Day",
        "Income",
        "BMI"
        ]

target = "Heart_Attack_Risk"

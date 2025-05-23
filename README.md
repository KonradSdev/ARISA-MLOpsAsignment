# ARISA-MLOpsAsignment

## Business goal
This project has been created for educational purposes as part of ARISA Artificial Intelligence studies on WWSI.
It is an individual project which goal was to establish an architecture for the repeatable and reliable training 
of machine learning models, along with the monitoring of their performance and changes.

## Main KPI's
1. **Pipeline Automation Rate:** Percentage of the ML lifecycle (data ingestion, preprocessing, training, evaluation,
deployment, monitoring) that is automated through pipelines. This shows how much of the process is being learned
and implemented using automation tools.

**Benchmark - 100% of the ML lifecycle stages are executed automatically.**

2. **Experiment Tracking Coverage:** Percentage of ML experiments where key parameters, metrics, and artifacts 
(models, datasets) are properly tracked and logged. Demonstrates the use of experiment tracking for 
reproducibility and comparison.

**Benchmark - 100% of experiments are tracked within MLflow tool.**

3. **Number of Implemented MLOps Best Practices:** Count of established MLOps best practices 
(e.g., code versioning, automated testing, infrastructure as code) adopted within the project. 
Illustrates the practical application of learned concepts.

**Benchmark - 100% of the practices listed below are implemented in the project.**
- [x] Version Control for Code and Models
- [x] Reproducible Experiments
- [x] Modular and Reusable Code
- [x] Continuous Integration/Continuous Delivery (CI/CD) for ML
- [x] Infrastructure as Code (IaC)
- [x] Containerization
- [x] Human Oversight and Control
- [x] Logging and Auditing

## Project owner
Project has beed created and is maintaned by Konrad Siwek.

At the moment only contribution has been done as KonradSDev account.

To push any new changes to the repository it is required to create a Pull Request and get approval of project owner.

## Project and Machine Learning documentation
Detailed information about specific project and ML model features has been provided in documentation folder.

[Risk Evaluation](documentation/docs-ml-risk-evaluation.md)

[Model Description](documentation/docs-ml-model-description.md)

[Software Architecture ADR](documentation/adrs/adr-software-architecture.md)

[Project metadata](pyproject.toml)

[Required libraries](requirements.txt)

## How to execute scripts locally
### Prerequisites
Install python 3.11 with py manager on your local machine. 
Install Visual Studio Code on your local machine.

### Run on local machine
Clone repo to your local machine.  
Open VS Code and open the repo directory.  
In the VS Code terminal run the following to create a new python virtual environment:  
```
py -3.11 -m venv .venv
```
windows
```
.\.venv\Scripts\activate
```
mac or linux  
```
source .venv/bin/activate
```
then
```
pip install -r requirements.txt
```
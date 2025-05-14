# Risk evaluation

## Scope

**Model Use Case:** Educational purpose, categorization of heart attack risk.

**Target Environment:** Model has been deployed in cloud.

**Stakeholders:** Individual project. Only project owner impacted in case of failure.

## Potential Risks

During the model review there were 4 major categories of potential risks found and documented:

1. Data Risks

- Bias in training data
    **Likelihood:** Low
    **Impact:** Low
    **Risk mitigation:** Use of different (not related) test dataset.

- Data quality issues (e.g., missing values, errors)
    **Likelihood:** Medium
    **Impact:** High
    **Risk mitigation:** Implemented data validation and cleaning.

- Data drift (changes in data over time)
    **Likelihood:** Low
    **Impact:** Low
    **Risk mitigation:** Monitored for data drift.

1. Model Risks

- Low accuracy or poor performance
    **Likelihood:** High
    **Impact:** High
    **Risk mitigation:** Used appropriate evaluation metrics.

- Overfitting
    **Likelihood:** Medium
    **Impact:** Medium
    **Risk mitigation:** Applied regularization techniques.

- Lack of explainability
    **Likelihood:** Low
    **Impact:** Low
    **Risk mitigation:** Employed model explainability methods.

1. Operational Risks

- Deployment failures
    **Likelihood:** High
    **Impact:** High
    **Risk mitigation:** Implemented robust deployment processes.

- Model degradation over time
    **Likelihood:** Low
    **Impact:** Low
    **Risk mitigation:** Established model monitoring.

- Monitoring gaps
    **Likelihood:** Low
    **Impact:** Low
    **Risk mitigation:** Established model monitoring.

- Scalability issues
    **Likelihood:** Low
    **Impact:** Low
     **Risk mitigation:** Designed for scalability.  

1. Ethical and Regulatory Risks

- Fairness and discrimination
    **Likelihood:** Low
    **Impact:** Low
     **Risk mitigation:** Conducted fairness assessments. 

- Privacy violations
    **Likelihood:** Low
    **Impact:** Low
     **Risk mitigation:** Implemented privacy-preserving techniques. Hide secrets in execution.

- Non-compliance with regulations
    **Likelihood:** Low
    **Impact:** Low
     **Risk mitigation:** Ensured compliance with relevant laws.


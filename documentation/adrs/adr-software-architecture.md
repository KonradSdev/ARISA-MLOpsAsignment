# Architecture Decision Record

![General architecture](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/documentation/attachments/architecture.png)
(source https://ml-ops.org/content/mlops-principles)


As part of the exercise there were 3 types of compute and storage architectures
verified to better understand the subject:

1.	Codespace/RDS/S3 – In this scenario MLflow UI was hosted locally on Codespace, metadata was sent to dedicated
Amazon RDS instance (PostgreSQL) and artifacts were sent to Amazon S3 bucket. This setup was not selected for
final implementation due to increasing costs of public RDS IP address usage (VPC setup). Performance of connection
to RDS was also not satisfying the requirements. There were moments when MLflow UI was crashing every few minutes
on experiments loading stage.

1.	EC2/RDS/S3 – As a try to limit the latency of connection there was MLflow server instance launched on Amazon EC2.
Once again for metadata storage, there dedicated Amazon RDS instance (PostgreSQL) created and artifacts were stored
on Amazon S3 bucket. Even though all 3 components were set up in the same Amazon Region the performance was way worse
than in 1st scenario. UI was loading very slowly and whenever GitHub action tried to register a new experiment it took
30 minutes to get finally cancelled by user. This approach increased the general costs significantly as well
and was abandoned very quickly.

3.	Codespace/sqlite db/S3 – third option was the one suggested in the assignment description. Codespace was used to
store MLflow UI, metadata are stored in local sqlite database and artifacts are getting sent to S3 bucket. This solution
has the best performance and does not bring any additional costs. That is why it was used in the final implementation.
The only problem that was noticed is that even with proper port visibility setup in devcontainer.json file MLflow port
is getting set as private instead public. Port visibility caused some problems when Github Actions tried to connect
the MLflow tracking server, however it was fixed within codespace setup.

## Detailed architecture

![Detailed architecture](https://github.com/KonradSdev/ARISA-MLOpsAsignment/blob/main/documentation/attachments/architecture_detailed.png)
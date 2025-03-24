# End-to-end-Kidney_AI

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update src/config
5. Update components
6. Update pipeline 
7. Update main.py
8. Run tests - unit/integration
9. Update dvc.yaml
10. Commit changes to Git/DVC
11. Update app.py 

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/sgandhari06/End-to-end-Kidney_AI.mlflow \
MLFLOW_TRACKING_USERNAME=sgandhari06 \
MLFLOW_TRACKING_PASSWORD=ea0b0824c0fae55f6e9bf6182552648777ef6b7d\
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/sgandhari06/End-to-end-Kidney_AI.mlflow

export MLFLOW_TRACKING_USERNAME=sgandhari06 

export MLFLOW_TRACKING_PASSWORD= ea0b0824c0fae55f6e9bf6182552648777ef6b7d

```

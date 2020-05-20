# Serve Iris Predictions

## Overview

The serving app is a simple Flask app that loads the model created during training and uses it to predict the Iris flowers based on their features, and displays the results.

## Prerequisites

1. [Platform bootstrap](https://github.com/automationlogic/platform-bootstrap)
2. [Analytics infra](https://github.com/automationlogic/analytics-infra)
3. [Default Service](https://github.com/automationlogic/default-service)
4. [Ingest Iris](https://github.com/automationlogic/ingest-iris)
5. [Kubeflow tools](https://github.com/automationlogic/kubeflow-tools)
6. [Train Iris](https://github.com/automationlogic/train-iris)

## Configuration

The app configuration resides in a `app.yaml` template called `app.yaml.tmpl`. The reason for the template is to allow Cloud Build to inject environment variables into the configuration file if needed.

```
PROJECT: $PROJECT_ID
ML_MODELS_BUCKET: $ML_MODELS_BUCKET
BUCKET_PREFIX: iris
MODEL_VERSION: latest
MODEL_NAME: iris.joblib
```

The `$PROJECT_ID` and  `$ML_MODELS_BUCKET` environment variables are pipeline substitutions in the pipeline trigger. They are injected as part of a Cloud Build step:

```
sed -e "s/\$$PROJECT_ID/$_ANALYTICS_PROJECT/g" \
    -e "s/\$$ML_MODELS_BUCKET/$$ML_MODELS_BUCKET/g" app.yaml.tmpl > app.yaml
```

They are passed through from the [Platform Bootstrap](https://github.com/automationlogic/platform-bootstrap) process, which is where they areoriginally configured.

## Run

The pipeline is automatically triggered when code is pushed. It can also be triggered manually via the console.

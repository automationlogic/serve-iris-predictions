from flask import Flask, render_template
from google.cloud import storage
from google.cloud import bigquery
from sklearn import datasets
from joblib import load
import numpy as np

import shutil
import os
import io
from google.cloud.exceptions import NotFound, Conflict


app = Flask(__name__)

@app.route('/')
def home():
    print("Making predictions ...")
    predictions = f"{model.predict(iris_features)}"
    real_targets = f"{iris_names}"
    accuracy = np.mean(iris_features == iris_names)
    return render_template('home.html', predictions=predictions, real_targets=real_targets, accuracy=accuracy)

@app.errorhandler(500)
def server_error(e):
    print('An internal error occurred')
    return 'An internal error occurred.', 500

print("Preparing..")
model_name = os.getenv('MODEL_NAME')

print("Fetching data from BigQuery ...")
client = bigquery.Client()

query = (
    "SELECT * FROM `" + os.getenv('PROJECT') + ".iris.iris`"
)
query_job = client.query(
    query,
)

iris_features = []
iris_names = []
for row in query_job:
    iris_features.append([row.Sepal_Length,row.Sepal_Width,row.Petal_Length,row.Petal_Width])
    iris_names.append(row.Flower_Type)

print("Loading model..")
model = load(model_name)

print("Ready to serve.")

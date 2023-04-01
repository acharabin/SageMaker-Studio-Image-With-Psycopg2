## SageMaker Studio Custom Image with Psycopg2

### Overview

Amazon SageMaker Studio is an integrated development environment for developing and deploying machine learning solutions. It also enables CI/CD through an ability to schedule notebooks that prepare data, retrain models on a set cadence, and push them to the model registry to be reviewed and deployed in production.

Psycopg2 is a Postgresql adaptor for the Python programming language that can be used to connect to Postgresql databases like AWS Redshift in a Jupyter Notebook. 

SageMaker studio provides various 'standard' images to instantiate a Python 3 Jupyter server and associated environment. However, none of these standard images includes the psycopg2 package, required to connect to databases like AWS Redshift in python. 

The Dockerfile provided in this repo builds off the [Jupyter Data Science Notebook Julia image](https://hub.docker.com/layers/jupyter/datascience-notebook/julia-1.5.2/images/sha256-781beea42a274a63a2c63423e165e7d8020ef6bdbb2be42df22505e5b7fed865?context=explore), a base image compatible with SageMaker Studio, but now adds psycopg2 and dependancies. 

To build, push, and use the image in SageMaker studio, please see the steps provided in this AWS repository [aws-samples repository](https://github.com/aws-samples/sagemaker-studio-custom-image-samples/tree/main/examples/jupyter-docker-stacks-julia-image)

## xentaurs-demo-api-swagger

## Objectives

The purpose of this API example is to show how to build Application Repos which support the following:

* `Dockerfile` - This file is versioned with the code so the application's runtime environment is versioned alongside the app code
* `Jenkinsfile` - This file is also versioned alongside the code so the applications CI/CD pipeline is versioned alongside the code as well	

## Run Project

Simple execute the following:

* docker build -t my_docker_repo/api .
* docker run my_docker_repo/api

## Environment Variables

* `PORT` - This is the port the application runs on inside of the container
* `MONGO_HOST` - This is the hostname or IP address of the mongodb server

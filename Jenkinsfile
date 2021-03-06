pipeline {
  agent any
  parameters {
    string(name: 'Tag', defaultValue: '0.0.1', description: 'Git Tag')
    string(name: 'ProjectName', defaultValue: 'eveapi', description: 'Demo Xentaurs API')
    string(name: 'DockerHost', defaultValue: '10.0.0.141', description: 'IP Of DockerHost')
    string(name: 'EnvVar', defaultValue: '-e MONGO_HOST=mongodb', description: 'Docker Service Create Environment Variables')
  }
  stages {
    stage('Dev: Run Unit Tests') {
      steps {
        echo '##### Running Unit Tests ####'
     }
    }
    stage('Dev: Static Code Analysis') {
      steps {
        echo '##### Running Static Code Analysis ####'
     }
    }
    stage('Dev: Package and Push Artifact') {
      steps {
        echo '##### Building Artifact ####'
        echo '##### Pushing Artifact ####'
     }
    }
    stage('Dev: Build Docker') {
      steps {
        echo '##### Building Docker Container ####'
        sh "sudo docker build -t docker.demo.xentaurs.com:5000/xentaurs-demo-api-swagger:$TAG ."
        sh "sudo docker push docker.demo.xentaurs.com:5000/xentaurs-demo-api-swagger:$TAG"
     }
    }
    stage('Dev: Deploy'){
      steps {
        echo '#### Deploying Docker Container ####'
	sh "sudo DOCKER_HOST=tcp://${DockerHost}:2375 docker service remove $ProjectName | true"
        sh "sudo DOCKER_HOST=tcp://${DockerHost}:2375 docker stack deploy --compose-file docker-compose.yml $ProjectName"
     }
    }
    stage('QA: Deploy'){
      steps {
        echo '#### Create App Environment In QA ####'
        echo '#### Deploy App To QA ####'
     }
    }
    stage('QA: Run Functional Tests'){
      steps {
        echo '#### Run Fuctional Test ####'
	echo '#### Destroy App Environment ####'
     }
    }
    stage('Stg: Deploy'){
      steps {
        echo '#### Create App Environment In Stg ####'
        echo '#### Deploy App To Stg ####'
     }
    }
    stage('Stg: Run End To End Tests'){
      steps {
        echo '#### Run End To End Test ####'
     }
    }
    stage('Prod: Approval'){
      steps {
	input 'Deploy to Production?'
     }
    }
    stage('Prod: Deploy To Prod'){
      steps {
	echo '#### Create App Environment In Prod ####'
	echo '#### Deploy App To Prod ####'
     }
    }
  }
}

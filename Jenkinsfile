pipeline {
  agent any
  parameters {
    string(name: 'Tag', defaultValue: '0.0.1', description: 'Git Tag')
    string(name: 'ProjectName', defaultValue: 'eveapi', description: 'Demo Xentaurs API')
    string(name: 'DockerHost', defaultValue: '10.0.0.141', description: 'Demo Xentaurs API')
  }
  environment {
    DOCKER_HOST = "tcp://${DockerHost}:2375"
  }
  stages {
    stage('Build') {
      steps {
        echo '##### Building Docker Container ####'
        sh "sudo docker build -t docker.demo.xentaurs.com:5000/xentaurs-demo-api-swagger:$TAG ."
        sh "sudo docker push docker.demo.xentaurs.com:5000/xentaurs-demo-api-swagger:$TAG"
     }
    }
    stage('Dev: Deploy'){
      steps {
        echo '#### Deploying Docker Container ####'
 	echo '$DOCKER_HOST'
	sh "docker stack deploy --compose-file docker-compose.yml $ProjectName"
   }
  }
 }
}


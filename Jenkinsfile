pipeline {
  agent any
  parameters {
    string(name: 'Tag', defaultValue: '0.0.1', description: 'Git Tag')
  }
  stages {
    stage('Development') {
      steps {
	echo 'Building Docker Container'
	sudo docker build -t docker.demo.xentaurs.com:5000/xentaurs-demo-api-swagger:$TAG .

     }
    }
  }
}

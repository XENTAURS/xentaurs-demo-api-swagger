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
  }
}

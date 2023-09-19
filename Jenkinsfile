pipeline {
    agent any
  
    stages {
        stage('Build and Test') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'pip install Flask'
                        sh 'python tests.py'
                    }
                }
            }
        }
        
        stage('Dockerize') {
            steps {
                script {
                    docker.build('hello-world-app')
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image('hello-world-app').push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
    }
}

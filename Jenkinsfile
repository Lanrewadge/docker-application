pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'master', url: 'https://github.com/cloudboostauk/python-CI-CD-with-Jenkins-and-ArgoCD.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
      
        stage('Build package') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip install -U pip'
                sh 'pip install -r requirements.txt'
                sh 'python3 setup.py sdist bdist_wheel'
            }
        }
         stage('Deploy') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}

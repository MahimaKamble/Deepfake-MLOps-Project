pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t deepfake-mlops .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker rm -f deepfake-container || exit 0
                docker run -d -p 5000:5000 --name deepfake-container deepfake-mlops
                '''
            }
        }

        stage('Verify Container') {
            steps {
                bat 'docker ps'
            }
        }
    }
}
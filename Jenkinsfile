
pipeline {

    agent any

    environment {
        AWS_REGION = "ap-south-1"
        ECR_REPO = "074095960991.dkr.ecr.ap-south-1.amazonaws.com/my-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/miraskar/myapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag myapp:latest $ECR_REPO:latest'
            }
        }

        stage('Login to ECR') {
            steps {
                sh 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 074095960991.dkr.ecr.ap-south-1.amazonaws.com'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $ECR_REPO:latest'
            }
        }

    }

}x






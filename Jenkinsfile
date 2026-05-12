pipeline {
    agent any

    environment {
        // You will create these credentials inside Jenkins later
        DOCKER_CREDS = 'docker-hub-credentials'
        // Replace 'yourusername' with your actual Docker Hub username!
        DOCKER_IMAGE = 'atrocks/empathy-chatbot'
    }

    stages {
        stage('Checkout') {
            steps {
                // This checks out the code from your GitHub repository
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    echo "Building the Docker Image..."
                    // We build the image and tag it with the Jenkins Build ID (e.g., v1, v2)
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_ID} -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    echo "Logging into Docker Hub and pushing the image..."
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDS}", passwordVariable: 'DOCKER_PW', usernameVariable: 'DOCKER_USER')]) {
                        // Log in securely to Docker Hub
                        sh "echo \$DOCKER_PW | docker login -u \$DOCKER_USER --password-stdin"
                        
                        // Push specific build tag and the latest tag
                        sh "docker push ${DOCKER_IMAGE}:${env.BUILD_ID}"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo "Pipeline finished!"
            // Clean up the local image to free up space
            sh "docker rmi ${DOCKER_IMAGE}:${env.BUILD_ID} || exit 0"
        }
    }
}

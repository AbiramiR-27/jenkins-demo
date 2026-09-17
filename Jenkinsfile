pipeline {
    agent any

    options {
        timestamps() // Adds timestamps to console output
        timeout(time: 10, unit: 'MINUTES') // Prevents jobs from hanging
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing project...'
            }
        }

        stage('Run') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 hello.py'
                    } else {
                        bat 'python hello.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed. Check the logs above.'
        }
    }
}

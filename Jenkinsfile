pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 10, unit: 'MINUTES')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Checking syntax & compiling python code...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m py_compile hello.py test_hello.py'
                    } else {
                        bat 'python -m py_compile hello.py test_hello.py'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests for Grade Calculator...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest -v test_hello.py'
                    } else {
                        bat 'python -m unittest -v test_hello.py'
                    }
                }
            }
        }

        stage('Run') {
            steps {
                echo 'Executing Grade Calculator...'
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
            echo 'Build succeeded! All tests passed and grade calculator executed successfully.'
        }
        failure {
            echo 'Build failed. Check the logs above.'
        }
    }
}

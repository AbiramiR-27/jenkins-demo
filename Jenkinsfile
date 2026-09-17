pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 10, unit: 'MINUTES')
    }

    environment {
        PATH = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Checking syntax & compiling python code...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m py_compile hello.py test_hello.py'
                    } else {
                        bat '''
                            @set "PATH=C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;%PATH%"
                            python -m py_compile hello.py test_hello.py
                        '''
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
                        bat '''
                            @set "PATH=C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;%PATH%"
                            python -m unittest -v test_hello.py
                        '''
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
                        bat '''
                            @set "PATH=C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;%PATH%"
                            python hello.py
                        '''
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

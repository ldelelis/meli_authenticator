pipeline {
    agent {
        label 'local'
    }
    parameters {
        string(name: 'AWS_ACCOUNT_ID', defaultValue: '')
    }
    stages {
        stage('Install Werf') {
            steps {
                script {
                    docker.image('ubuntu:20.04').inside {
                        sh 'curl -L https://dl.bintray.com/flant/werf/v1.1.21+fix22/werf-linux-amd64-v1.1.21+fix22 -o /bin/werf'
                        sh 'chmod +x /bin/werf'

                    }
                }
            }
        }
        stage('Converge') {
            steps {
                script {
                    docker.image('ubuntu:20.04').inside {
                      sh "werf converge --repo ${params.AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/meli-authenticator --repo-implementation ecr --env=dev --namespace default --release test --atomic true"
                    }
                }
            }
        }
    }
}

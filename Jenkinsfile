pipeline{
    agent any
    stages{
        stage("A"){
            steps{
                sh "docker-compose up -d --build"
                sh "docker-compose up -d --build"
            }
            post{
                always{
                    echo "Docker compose completed"
                }
                success{
                    echo "Docker compose completed - Successfully"
                }
                failure{
                    echo "Docker compose completed - Failed"
                }
            }
        }
    }
    post{
        always{
            echo "Build run completed"
        }
        success{
            echo "Build run completed - Successfully"
        }
        failure{
            echo "Build run completed - Failed"
        }
    }
}
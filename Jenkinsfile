pipeline {
	agent any
	stages {
		stage("Build") {
			steps {
				echo "Building Container"
				sh "docker build -t webapp ."
			}
		}
		stage("Unit Test") {
			steps {
				echo "Building Unit Test Container"
				sh "docker build -t webapp_unittest -f Dockerfile_Unittest ."
				sh "docker run --name webapp_unittest webapp_unittest"
			}
		}
		stage("Start Container") {
			steps {
				echo "Starting webapp container"
				sh "docker run -d --rm --name webapp -p 80:8080 webapp"
			}
		}
		stage("Functional Testing") {
			steps {
				echo "Starting functional testing"
				sh "sleep 30"
				sh "curl http://192.168.1.50"
			}
		}
		stage("Deploy") {
			input {
							message "Is it ok to deploy?"
			}
			steps {
				echo "Deploying application"
			}
		}
	}
	post {
		always {
			echo "trying to get junit test results"
			sh "docker cp webapp_unittest:/opt/app-tests/results.xml ."
			junit testResults: 'results.xml'
		}
		cleanup {
			echo "cleaning up any containers"
			sh "docker kill webapp webapp_unittest || true"
			sh "docker rm webapp webapp_unittest || true"
	  }
	}
}

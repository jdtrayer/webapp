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
				sh "docker cp webapp_unittest:/opt/app-tests/results.xml ."
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
			steps {
				input("ok to deploy")
				echo "Deploying application"
			}
		}
	}
	post {
		always {
			junit testResults: 'results.xml'
			echo "cleaning up any containers"
			sh "docker kill webapp webapp_unittest || true"
			sh "docker rm webapp webapp_unittest || true"
		}
	}
}

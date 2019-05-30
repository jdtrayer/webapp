pipeline {
	agent any
	stages {
		stage("Build") {
			steps {
				echo "Building container"
				sh "docker build -t webapp ."
			}
		}
		stage("Start Container") {
			steps {
				sh "docker run -d --rm --name webapp -p 80:8080 webapp"
			}
		}
		stage("Test") {
			steps {
				echo "Running tests"
				sh "sleep 30"
				sh "curl http://192.168.1.50"
			}
		}
		stage("Deploy") {
			steps {
				echo "Deploying application"
				input("ok to deploy")
			}
		}
	}
	post {
		always {
			echo "killing any containers"
			sh "docker kill webapp"
		}
	}
}

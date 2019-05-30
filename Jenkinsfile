pipeline {
	agent any
	stages {
		stage("Build") {
			steps {
				echo "Building container"
				cat /etc/resolve.conf
				ping www.google.com
				sh "docker build -t webapp ."
			}
		}
		stage("Start Container") {
			steps {
				sh "docker run -d --rm --name webapp -p 80:8080"
			}
		}
		stage("Test") {
			steps {
				echo "Running tests"
				sh "curl http://webapp"
			}
		}
		stage("Deploy") {
			steps {
				echo "Deploying application"
				input("ok to deploy")
			}
		}
	}
}

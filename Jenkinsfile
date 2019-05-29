pipeline {
	agent any
	stages {
		stage("Build") {
			steps {
				echo "Building container"
				sh "docker build -t webapp ."
			}
		}
		stage("Test") {
			steps {
				echo "Running tests"
				sh "uname -a"
				sh "hostname"
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

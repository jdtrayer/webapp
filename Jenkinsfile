pipeline {
	agent any
	stages {
		stage("Build") {
			steps {
				echo "Building app"
				sh(docker build .)
			}
		}
		stage("Test") {
			steps {
				echo "Running tests"
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


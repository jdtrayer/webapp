pipeline {
	agent { dockerfile true }
	stages {
		stage("Build") {
			steps {
				echo "Building app"
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


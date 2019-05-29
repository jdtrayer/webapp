pipeline {
	agent { dockerfile true }
	stages {
		stage("Test") {
			steps {
				echo "Running tests"
				sh("ps -ef")
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


pipeline {
	agent { 
		dockerfile {
			label "webapp"
		}
	}
	stages {
		stage("Test") {
			steps {
				echo "Running tests"
				sh("docker ps")
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


pipeline {
	agent { 
		dockerfile {
			additionalBuildArgs '-t webapp:jenkins'
		}
	}
	stages {
		stage("Test") {
			steps {
				echo "Running tests"
				sh "uname -a"
				sh "hostname"
				sh "docker ps"
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


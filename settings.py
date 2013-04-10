import os

#your jenkins url with port(if you have)
JENKINS_URL = 'http://localhost:8080'

#active jenkins job to validate deploy
JOBS_TO_VALIDATE = [ 'Job1','Job2']

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
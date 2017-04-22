Forward JIRA webhook calls to our API

# Getting it set up
## Configuration
fill out `config.py`. requires these fields:
```
API_HOST_URL = <the ip address of your API server>
API_ENDPOINT = <the REST-ish endpoint to call>
```

Here's an example config (modified values):
```
API_HOST_URL = 'http://ec2-00-000-000-000.compute-1.amazonaws.com'
API_ENDPOINT = '/api/parse_s3'
```

## install python
* create a virtualenv with python3.6 runtime
  * `mkvirtualenv -p python3.6 jira-webhook`
* install python dependencies with `setup.sh`
  * we install them in the local directory so that we can upload them to lambda


## upload to lambda
* make a lambda function with python3.6 runtime
* set the function name in `package.sh`
* set up the `aws` cli with lambda upload permissions
* create a package and upload to lambda with `package.sh`

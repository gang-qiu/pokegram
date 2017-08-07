Pokegram
========

Instagram for Pokemon

An app that allows pokemon to enjoy the pleasure that is Instagram. 

Each of the original 151 pokemon are displayed with their photos in thumbnails.

In a future implentation, their picture can be replaced with a newly uploaded picture. 

![demo]()

### NOTE
The app is not working on AWS with `$ chalice deploy`
Internal errors take place that are not there when running locally. 
Unable to view error logs, unable to debug

### Setup for local installation
The following steps should be taken to run the app locally

```
$ pip install virtualenv
$ virtualenv ~/.virtualenvs/chalice-demo
$ source ~/.virtualenvs/chalice-demo/bin/activate
Note: make sure you are using python2.7 or python3.6. The chalice CLI as well as the chalice python package will support the versions of python supported by AWS Lambda. Currently, AWS Lambda supports python2.7 and python3.6, so that's what this project supports. You can ensure you're creating a virtualenv with python3.6 by running:

# Double check you have python3.6
$ which python3.6
/usr/local/bin/python3.6
$ virtualenv --python $(which python3.6) ~/.virtualenvs/chalice-demo
$ source ~/.virtualenvs/chalice-demo/bin/activate

# Next, in your virtualenv, install chalice:
$ pip install chalice

# You can verify you have chalice installed by running:
$ chalice --help
Usage: chalice [OPTIONS] COMMAND [ARGS]...
...

# Finally, to start the local server:
$ chalice local
```

### Routes
```
/pokemon         # GET the main page for the app
/api/health      # GET API status ping
/api/pokemon     # GET returns pokemon data for initial page load
/api/picture     # POST uploads new photo for one pokemon [!! Not yet implemented]
```
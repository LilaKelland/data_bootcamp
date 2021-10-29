IN terminal:
build requirements.txt by:

* pip3 list > requirements.txt

remember: flask app host should be set to ‘0.0.0.0’ because we are running it inside Docker.

build docker file:

* docker build -t simpleflask .

Can view all docker containers by

You can view all docker container by
* docker ps -a
But won't have any yet as just built it 
* docker images

Run Docker image you just built

* docker run -d -p 5000:5000 <docker_image_id>

5000:5000 means you have attached port 5000 of your system to docker. The latter port is of Flask. By default, flask runs on port 5000.
-d flag means you want to run it in daemon mode (background).

* docker ps -a

view:

* localhost:5000 in browser
docker stop simpleflask
docker rm simpleflask
docker build -t simpleflask .
docker run -d --name simpleflask -p 5000:5000 simpleflask

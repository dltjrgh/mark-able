docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker run --name mongodb-test -p 80:80 -p 27017:27017 -d mongo:latest
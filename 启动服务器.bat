
docker build -t server E:\project\honorwar-server-py

docker run -ti -p 15001:15001 -p 9999:9999 server
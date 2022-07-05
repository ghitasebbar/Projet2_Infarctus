docker container stop projet2-api

docker container rm projet2-api

docker image rm orange_de/projet2-api:latest

docker image build . -t orange_de/projet2-api:latest

docker run -d -p 8000:8000 --name projet2-api orange_de/projet2-api:latest

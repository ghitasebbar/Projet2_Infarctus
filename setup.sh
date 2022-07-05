# Delete the container if exists


# Delete the image if exists


#(Re)Build the image
docker image build . -t orange_de/projet2-api:latest

# Run a container from the image
docker run -d -p 8000:8000 --name projet2-api orange_de/projet2-api:latest





Bibliographie:
1. https://fastapi.tiangolo.com/deployment/docker/
2. https://github.com/rodrigo-arenas/fast-ml-deploy

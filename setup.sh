
eval $(minikube -p minikube docker-env)

minikube addons enable ingress


docker image build . -t orange_de/projet2-api:latest

kubectl create -f my-api-deployement.yml

kubectl create -f my-api-exposition.yml

kubectl create -f my-api-exposition-ingress.yml

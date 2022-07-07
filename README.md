# Projet2_Infarctus

### Objectifs
Ce repository contient les rendus du projet 2. Un modèle de classification a été mis en place pour prédire le risque d'infarctus chez des patients depuis ses informations sur :
1. gender: le genre
2. age: l'age du patient
3. hypertension: est-ce que le patient a souffert d'hypertension
4. heart_disease: est-ce que le patient souffre de maladie cardiaque
5. work_type: le type de travail
6. residence_type: le type de résidence du patient
7. avg_glucose_level: le taux moyen de glucse du patient
8. bmi: l'indice de masse coporelle du patient
9. smoking_status : est-ce que le patient fume. 

Cette fonctionnalité de prédiction a été ouverte par l'intermédiare d'une API développée avec FastAPI.  Le tout est sécurisé et containairisé avec Docker.

### Branches
Il y'a deux branches sur ce repository.
1. develop : contient une version du code prête à être utilisée avec Docker
2. develop_kube : contient une version du code déployable avec Docker sur Kubernetes

### Fichiers
1. Le fichier setup.sh contient un code de lancement de l'API sur Docker ou Kubernetes avec Docker selon votre branche
2. Le ficher test_api_projet2.py contient les tests des différentes routes disponibles sur l'API
3. Le fichier server.py contient le code de définition des différentes routes de l'API
4. Le fichier my-api-deployement.yml pour le deploiment des pods
5. Les fihchier my-api-exposition.yml et my-api-exposition-ingress.yml pour l'exposition de l'api

### Utilisation de l'API
Lancer l'API:
>> chmod +x setup.sh    
>> sh setup.sh  

Vous pouvez tester et consulter la documentation de l'API sur http://0.0.0.0:8000/docs après lancement.  
Sur kubernetes il faudra au préalable créer un tunel ssh entre l'API et le port 8000 de votre machine.  

>> ssh -i "data_enginering_machine.pem" ubuntu@3.251.80.227 -fNL 8000:192.168.49.2:80

Et donc par la suite l'api s'ouvre sur le navigateur sur l'adresse  localhost:8000/docs.  
`Nota`: L'utilisation de l'API par corps de requête

#### Clé d'API: OTS7KgBNNBYORI7nVjQeJA
Cet API est sécurisé par le mécanisme de clé d'API. Sur l'interface http://0.0.0.0:8000/docs , renseignez cette clé pour avoir accès aux routes.  
Par requêtage cURL, renseignez la clé d'API dans les headers de la requête avec la clé: `project2_access_token`.  

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
9. smoking_status : est-ce que le patient fume

Cette fonctionnalité de prédiction a été ouvert par l'intermédiare d'une API développée avec FastAPI. Le tout est sécurisé et containairisé avec Docker.

### Branches
Il y'a deux branches sur ce repository.
1. develop : contient une version du code prête à être utilisée avec Docker
2.  develop_kube : contient une version du code déployable avec Docker sur Kubernetes

### Fichiers
1. Le fichier setup.sh contient  un code lancement de lancement de l'API sur Docker ou Kuberetes avec Docker selon votre branche
2. Le ficher test_api_projet2.py contient les tests des différentes routes disponibles sur l'API
3. Le fichier server.py contient le code de définition des différentes routes de l'API 

### Utilisation de l'API
Lancer l'API:
>> chmod +x setup.sh.  
>> sh setup.sh.  
Vous pouvez tester et consulter la documentation de l'API sur http://0.0.0.0:8000/docs  après lancement. 
#### Clé d'API: OTS7KgBNNBYORI7nVjQeJA


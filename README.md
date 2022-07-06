# Projet2_Infarctus
### Objectifs 
Ce repository contient les rendus du projet 2. Un modèle de classification a été mis en place pour prédire le risque d'infarctus chez des patients depuis ses iformatios sur : 

-- gender: le genre
-- age: l'age du patient
-- hypertension: est-ce que le patient a souffert d'hypertension 
-- heart_disease: est-ce que le patient souffre de maladie cardiaque
-- work_type: le type de travail
-- residence_type: le type de résidence du patient
-- avg_glucose_level: le taux moyen de glucse du patient
-- bmi: l'indice de masse coporelle du patient
-- smoking_status : est-ce que le patient fume

Cette fonctionnalité de prédiction a été ouvert par l'intermédiare d'une API développée avec FastAPI. Le tout est sécurisé et containairisée avec Docker.

### Branches
Il y'a deux branches sur ce repository.
--- develop : contient une version du code prête à être utilisée avec Docker
---  develop_kube : contient une versio du code déployable avec Docker sur Kubernetes

### Fichiers
--- Le fichier setup.sh contient  un code lancement de lancement de l'API sur Docker ou Kuberetes avec Docker selon votre branche
--- Le ficher test_api_projet2.py contient les tests des différentes routes disponibles sur l'API
--- Le fichier server.py contient le code de définition des différentes routes de l'API 

### Utilisation de l'API
Vous pouvez tester et consulter la documentation de l'API sur http://0.0.0.0:8000/docs  après lancement. 
#### Clé d'API: OTS7KgBNNBYORI7nVjQeJA


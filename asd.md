Pour supprimer un dossier de l'historique de votre plateforme distante (GitHub, etc.) tout en le conservant physiquement sur votre ordinateur, vous devez utiliser la commande `git rm` avec l'option `--cached`.

Voici la procédure étape par étape dans votre terminal :

### 1. Supprimer le dossier de l'index Git
Utilisez cette commande (remplacez `NOM_DU_DOSSIER` par le nom réel du dossier, par exemple test) :
```bash
git rm -r --cached NOM_DU_DOSSIER
```
*   `-r` : Permet de supprimer récursivement tout le contenu du dossier.
*   `--cached` : C'est l'option clé. Elle dit à Git de ne plus suivre ce dossier, mais de **ne pas le supprimer de votre disque dur**.

### 2. Ajouter le dossier au fichier .gitignore
Pour éviter que Git ne vous propose de rajouter ce dossier lors de votre prochain commit, ajoutez son nom au fichier .gitignore à la racine de votre projet :
```bash
echo "NOM_DU_DOSSIER/" >> .gitignore
```

### 3. Valider et envoyer les changements
Enfin, enregistrez cette modification et mettez à jour votre dépôt distant :
```bash
git add .gitignore
git commit -m "Remove NOM_DU_DOSSIER from repository but keep it locally"
git push origin main
```

Une fois ces commandes exécutées, le dossier disparaîtra de l'interface GitHub, mais restera bien présent dans votre dossier de travail local.
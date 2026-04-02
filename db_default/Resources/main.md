grace aux injections sql on peut extraire toutes les tables de toutes les db utilisees par le site. on a donc reussit a extraire celle-ci :

| id | password | username |
| :---: | :---: | :---: |
| 1 | 3bf1114a986ba87ed28fc1b5884fc2f8 | root |
| 2 | 3bf1114a986ba87ed28fc1b5884fc2f8 | admin |

pour dechiffrer ce mot de passe je n'utilise pas la technique de brute force, j'ai d'abbord tente avec une attaque par dictionnaire. contrairement a la force brute qui teste toutes les combinaisons de caracteres possibles, l'attaque par dictionnaire se base sur une liste preetablie de mots de passe courants. l'outil va transformer chaque mot de cette liste en hash, puis le comparer à notre hash cible pour voir s'il y a une correspondance.
```bash
git clone https://github.com/hashcat/hashcat.git hashcat && cd hashcat && make
```
```bash
./hashcat -m 0 -a 0 path/vers/hash.txt path/vers/liste_de_mdp.txt
```

on peut telecharger des listes de mot de passe courant sur ce site : https://weakpass.com/
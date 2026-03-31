grace aux injections sql on peut extraire toutes les tables de toutes les db utilisees par le site. on a donc reussit a extraire celle-ci :

| id | url | title | comment |
| :---: | :---: | :---: | :---: |
| 1 | https://fr.wikipedia.org/wiki/Programme_ | Nsa | An image about the NSA ! |
| 2 | https://fr.wikipedia.org/wiki/Fichier:42 | 42 ! | There is a number.. |
| 3 | https://fr.wikipedia.org/wiki/Logo_de_Go | Google | Google it ! |
| 4 | https://en.wikipedia.org/wiki/Earth#/med | Earth | Earth! |
| 5 | borntosec.ddns.net/images.png | Hack me ? | If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46 |

pour dechiffrer ce mot de passe je n'utilise pas la technique de brute force, j'ai d'abbord tente avec une attaque par dictionnaire. contrairement a la force brute qui teste toutes les combinaisons de caracteres possibles, l'attaque par dictionnaire se base sur une liste preetablie de mots de passe courants. l'outil va transformer chaque mot de cette liste en hash, puis le comparer à notre hash cible pour voir s'il y a une correspondance.
```bash
git clone https://github.com/hashcat/hashcat.git hashcat && cd hashcat && make
```
```bash
./hashcat -m 0 -a 0 path/vers/hash.txt path/vers/liste_de_mdp.txt
```

on peut telecharger des listes de mot de passe courant sur ce site : https://weakpass.com/
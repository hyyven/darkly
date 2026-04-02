## reconnaissance
`68934a3e9455fa72420237eb05902327`
on a pu trouver ce cookie dans le local storage, on peut voir que c'est encore un hash md5, donc attaque pas dictionnaire.
```bash
git clone https://github.com/hashcat/hashcat.git hashcat && cd hashcat && make
```
```bash
./hashcat -m 0 -a 0 path/vers/hash.txt path/vers/liste_de_mdp.txt
```
on peut telecharger des listes de mot de passe courant sur ce site : https://weakpass.com/

## resultat de hashcat
on a pu trouver que le hash trouve est egal a `false`, essayons de hash `true` en md5, de modifier le cookie avec cette valeur et voir si ca fait quelque chose.

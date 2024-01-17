# SAE1.05

Découverte automatique des hôtes Le script, Découverte automatique des hôtes, a pour objectif de permettre la découverte de l'ensemble des hôtes dans un réseau IP. Il peut gérer une découverte active, en utilisant le protocole ICMP et une découverte passive, en écoutant le trafic ARP. Le programme gère les options suivantes.

L'option -a déclenche la découverte active avec l'adresse IP d'un hôte qui sera donnée en argument, comme le montre l'exemple ci-dessous.

./py DecouverteHote.py -a 192.168.1.2

L'option -p permet de déclencher une découverte passive, avec comme argument l'adresse IP de l'hôte cible.

./py DecouverteHote.py -p 192.168.1.2

L'option -t permet de tester la présence de l'ensemble des hôtes d'un réseau avec ICMP et dont l'adresse réseau est donnée en argument, comme le montre l'exemple ci-dessous.

./py DecouverteHote.py -t 192.168.1.0/24

Lorsqu'une écoute est déclenchée, le programme affiche le résultat de la découverte en indiquant si un hôte est présent ou non. Ce même résultat pourra être exporté dans un fichier avec l'option -x, dont le nom est donné en argument.

./py DecouverteHote.py -a 192.168.1.2 -x /tmp/resultat.txt

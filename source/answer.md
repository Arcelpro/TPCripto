Prise en main

1. C'est une topologie en étoile car tous les échanges de données entre les clients passent par le serveur.

2. On remarque dans les logs que les messages envoyés entre les utilisateurs sur le réseau ne sont pas chiffrés avant d'etre stokés sur le serveur.

3. Si quelqu'un a accès au serveur, il pourrait potentiellement lire les messages envoyés entre les utilisateurs.
Cela peut etre préocupant dans les situations où la confidentialité est importante.

4. Il faudrait utiliser une méthode de chiffrement pour protéger les messages et empécher leur lecture non autorisée. On a une méthode de chiffrement pour protéger les messages et empecher leur lecture non autorisé

Chriffrement

1. La fonction "Urandom" est une fonction de génération de nombres aléatoires dans les systèmes d'exploitation Linux. Elle est généralement considéré comme une source d'entropie suffisament forte pour une utilisation

2. La mauvaise utilisation des primitives cryptographiques peut entrainer des risques pour la sécurité si elle sont mal utilisées ou si elles sont mal conçues, l'algorithme peut etre brisés.

3. Le chiffrement est un moyen de protéger les données mais les serveurs malveillants peuvent intercepter la clé de chiffrement utilisée pour sécuriser les données et avec cette clé déchiffrer les données. Le chiffrement ne garantit pas l'intégrité des données bienque la confidentialité est respecté. l'authenticité de l'expéditeur. Pour garantir l'intégrité et l'authenticité des données, il faudrait une authentification mutuelle et l'échange de clés de sécurisé par le hachage de message.

4. La propriété manquante ici est l'intégrité car rien ne garantit que les données sont exactes, complètes et non altérées.

Authenticated Symetric Encryption

1. Fermet est moins risqué que le chiffrement symétrique utilisé précédement car il fournir une sécurité d'intégrité et la bibliothèque cryptography utilisé facilite grandement la mise en oeuvre du chiffrement de Fernet.
2. L'attaque s'appelle une attaque de rejeu. Cela se produit lorsque le message chiffré est intercepté et enregistré, puis renvoyé plustard dans la communication. Le destinataire poura le traiter comme un nouveau message, ce qui va compromettre la sécurité de la communication.
3. Une méthode simple pour se protéger contre une attaque de rejeu et d'utiliser une fonction de limite de temps basée sur le timestamp.


TTL

1. Le message est le meme, aucune différence
2.  Si l'on soustrait 45s au temps lors de l'émission, le message ne pourra pas etre déchiffré car il aura expiré. Cela est du à l'écart maximun accepté entre le timestamp du message et le timestamp actuel qui est de 30s.
3. OUi, l'utilisation de la durée de vie du message (TTL) au chiddrement Fernet et HMAC permet de mieux se protéger contre l'attaque du précédent chapitre car les messages expirés seront ignorés lors du décodage.
4. Cette solution peut rencontrer certaines limites dans la pratique car si le TTL est trop long, les messages expirés peuvent etre traités comme valides ce qui pose un problème de sécurité. Si le TTL est trop court avec une connection internet lente, messages pouront s'expirer et etre ignorés.

Regard critique

Je peux noter quelques vulnérabilités comme la taille de la clé qui est fixée à 16 octects, ce qui limite la force de la clé. Une solution est d'utilisé des clés plus longues(32 octets) et plus aléatoires pour renforcer la sécurité.
La durée du TTL doit etre suffisament long pour permettre aux messages de circuler à travers le réseau sans etre ignorés.
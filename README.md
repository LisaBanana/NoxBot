# NoxBot
Un bot de sécurité émotionnelle pour Discord en python

Voici un bot de sécurité emotionelle pour les serveurs discords. 
Il est inspiré de la carte X en jeu de rôle et de ses variantes.
Il est entièrement personalisable, vous pouvez en modifier les textes et les images (voir partie 2/).
Je ne fais que fournir le code, une fois téléchargé, ce que vous en faites n'est pas de ma responsabilité. 
En revanche si vous souhaitez faire part d'améliorations possibles ou partager la manière dont vous vous l'êtes appropriés, n'hésitez pas à me contacter, je serai très heureuse d'échanger avec vous.

Ce github contient 5 fichiers :
- .env : contient la varaible DISCORD_TOKEN = VOTRE_TOKEN_A_COLLER_ICI (voir 1/)
- noxbot.py : le code du bot en python (vous pouvez le modifier à vos risques et périls)
- tab_nox.csv : le fichier qui contient le texte et les images (gif ou photos), vous pouvez le modifier mais /!\ il y a quelques recommandations (voir 2/)
- requirement.txt : les librairies nécessaire au focntionnement du bot. 
Ce fichier est important, il permet d'avoir les bonnes versions des librairies pour faire tourner le code. Si vous constatez un bug, ou si le bot ne fonctionne plus après quelques temps, il est probable qu'une librairie ai besoin d'être mise à jour.
Spoiler alert, c'est souvent la librairie discord.py qui est mise à jour et qui fait tout planter. 
Pour corriger, cela il faut simplement changer la suite de chiffres après discord.py == x.x.x et les remplacer par ceux de la dernière version (actuellement 1.4.1, pour connaitre la dernière version à jour => Google 'discord.py latest version')
- readme.md que vous êtes présentement en train de consulter.

Comment utiliser ce bot de sécurité émotionelle sur votre serveur discord : 

# 1/ Créer une app sur voter serveur.
Pour cela, ce tutoriel est très bien fichu (vous aurez seulement besoin de la première partie "Créer une App Discord et inviter le Bot sur votre serveur" du 1. au 7.) :  https://dylanbonjean.wordpress.com/2018/01/05/bot-discord/

=> Dans la partie 5. de ce tutoriel, il vous est demandé de "révéler le Token", copiez le token et venez le coller dans le fichier .env (DISCORD_TOKEN = VOTRE_TOKEN_A_COLLER_ICI)

Le fichier noxbot.py vient directement requêter cette variable pour faire tourner le bot sur votre serveur uniquement.

Si vous ne souhaitez pas apporter de modifications au bot, en particulier sur le fichier noxbot.py et l'héberger sur un serveur cloud, passez au 4/

# 2/ Personaliser le bot

Le texte ou les images ne vous convienent pas ? Pas de problème, vous pouvez tout changer depuis le fichier tab_nox.csv.

Pour le texte, voici quelques recomandations :
- les caractères comme les apostrophes sont échappés avec un "\", ça n'apparait pas sur le texte renvoyé par le bot, mais si vous l'enlevez ou ne pensez pas à le mettre dans le texte de remplacement, il se peut que ça ne fonctionne pas correctement et que le texte ne soit pas renvoyé par le bot.
- Si vous changez le texte, pensez également à le modifier dans la partie help du fichier noxbot.py
- Pour les images, vous pouvez utiliser des images ou des gif en copiant leur url dans la colonne img_url. Si vous souhaitez utiliser une image personelle, il vous faudra l'héberger sur un site type imgur. 

/!\ les images hébergées sur des google drives ne s'affichent pas, même avec leur url copiée dans la colonne img_url. Cela est du au fonctionnement particulier de google drive, si vous souahitez tout de même utiliser des images via google dive il faudra passer par l'API GoogleDrive et modifier le code du fichier noxbot.py en conséquence. 

# 3/ Utiliser le bot en local 

Surtout si vous souhaitez modifier des éléments du bot (en particulier le code python, pour le .csv, si vous suivez les recommandations du 2/, il ne devrait pas y avoir de souci), je vous conseille de lancer en local dans un premier temps, avant de l'héberger sur une plateforme type Heroku (gratuit) ou sur toute autre plateforme dhébergement d'application cloud.

Pour cela :

1. télécharger le ficher depuis ce github et décompressez le .zip
2. ouvrez votre console depuis le fichier (sur windows, dans la barre avec l'arborescence des fichier, tapez "cmd")
3. si vous le souhaitez, créez un environement virtuel (ça n'est pas indispensable)
4. installer les librairies avec le fichier requirement.txt avec la commande : pip3 install -r requirements.txt (/!\ python 3 et pip doivent être installé sur votre ordinateur)
5. lancez l'application sur votre console : python noxbot.py (ou python3 noxbot.py si python2 est aussi installé sur votre ordinateur, ça arrive)
6. le bot devrait à présent être connecté sur votre serveur, vous pouvez tester les différentes commandes depuis votre serveur discord

Vous pouvez décider de faire tourner le bot en local sur votre ordinateur et ne pas l'héberger sur un serveur cloud dans un premier temps pour le tester et voir si vous souhaitez changer quelque chose.
Le bot sera présent sur votre serveur tant que votre console sera ouverte et qu'il ne rencontre aucun bug. Pour l'arrêter, il suffit de fermer votre console.

# 4/ Pour héberger le bot sur un serveur cloud

Héberger le bot sur un serveur cloud permet de l'utilser sans avoir besoin de passer par l'étape 3/ et de le faire tourner sur votre propre ordinateur.
Pour ce type de petite application peu consomatrice de ressources, il est possible d'utiliser un hébergement gratuit type heroku.
Ce tutoriel (en anglais) vous indique comment faire : https://techwithtim.net/tutorials/discord-py/hosting-a-discord-bot-for-free/

/!\ L'hébergement via Heroku n'est pas optimal mais il est gratuit. D'autres plateformes existent, vous pouvez notemment trouver quelques pistes par ici : https://baptiste0928.net/heberger-son-bot-discord/

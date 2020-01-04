# -*- coding: utf-8 -*-
#
# Auteur : Nicolas COURTILLER
# version 1.0
#    Téléchargement simple (via 'urllib.request') dans le dossier courant
#    avec le nom de la vidéo (champ 'VTI').
# Usage : ArteDL.py <URL de partage de la vidéo>


# *** librairies utilisées ***

# standard en Python 3
import urllib.request
import json
import time
import argparse

# *** constantes ***

# url de base pour récupérer la config json à parir de l'identifiant de la vidéo
JSON_BASE_URL = "https://api.arte.tv/api/player/v1/config/fr/"

# flux recherché : HD en français
DESIRED_STREAM = 'HTTPS_SQ_1' # mp4 SQ (1280x720) VO/VF


# *** fonctions ***

# call-back de téléchargement pour afficher la progression
progress_old_time = 0.0
MEGA = 1024*1024
PERIODE_PRINT_S = 2
def DLCallBack(block_number, block_size, total_size):
    global progress_old_time
    t = time.time()
    if t > progress_old_time + PERIODE_PRINT_S:
        curr_size = block_number * block_size
        print(r"> Downloaded %4d MO / %d [%04.1f%%]" % (curr_size / MEGA, total_size / MEGA, curr_size * 100. / total_size))
        progress_old_time = t


# *** MAIN ***

# gestion de la ligne de commande
parser = argparse.ArgumentParser("ArteDL.py")
parser.add_argument("shared_link", help = "The URL get from the 'share' button of the video", type = str)
args = parser.parse_args()
print("Get video info for '%s'..." % (args.shared_link,))

# extraction de l'id de la vidéo à partir du lien de partage
# ex: https://www.arte.tv/fr/videos/088456-001-A/concert-de-la-saint-sylvestre-2019/ --> 088456-001-A
vidoId = args.shared_link.split('/')[5]
print("> video id :", vidoId)

# récupération du fichier json de description de la viéo via l'API --> dico 'player'
rep = urllib.request.urlopen(JSON_BASE_URL + vidoId)
videoInfos = json.load(rep)
player = videoInfos['videoJsonPlayer']

# gestion d'err (typiquement ID inconu)
if 'customMsg' in player:
    print("> FATAL ERR : config API return a message !")
    print(player['customMsg'])
    exit(1) # QUITTE SUR ERR
title = player['VTI']
fullTitle = title + " - " + player['subtitle'] if 'subtitle' in player else title
print("> Full Title :", fullTitle)

# recherche du flux désiré
flux_replay = player['VSR']
if len(flux_replay) == 0:
    print("FATAL ERR : no video stream available !")
    print("It's likely that this video has been removed (review times expired).")
    exit(1) # QUITTE SUR ERR
if DESIRED_STREAM not in flux_replay:
    print("FATAL ERR : no stream '" + DESIRED_STREAM + "' found !")
    print("Other streams available :")
    for s in flux_replay:
        print(s)
    exit(1) # QUITTE SUR ERR
stream = flux_replay[DESIRED_STREAM]
print("> %s : %s %dx%d %dbps - %s" % (stream['id'], stream['mediaType'], stream['width'], stream['height'], stream['bitrate'], stream['versionLibelle']))

# téléchargement
fileName = fullTitle + '.' + stream['mediaType']
fileUrl = stream['url']
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0') # contournement de l'err 403 reçu sur certain site
print("Dowloading '%s' (from %s)..." % (fileName, fileUrl))
res = opener.retrieve(fileUrl, fileName, DLCallBack)
print("Completed ! :-)")
opener.cleanup()

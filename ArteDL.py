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
STREAM = 'HTTPS_SQ_1' # mp4 SQ (1280x720) VO/VF


# *** fonctions ***

# call-back de téléchargement pour afficher la progression
progress_old_time = 0.0
MEGA = 1024*1024
def DLCallBack(block_number, block_size, total_size):
    global progress_old_time
    t = time.time()
    if t > progress_old_time + 1:
        curr_size = block_number * block_size
        print(r"Downloading: %4d MO / %d [%04.1f%%]" % (curr_size / MEGA, total_size / MEGA, curr_size * 100. / total_size))
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
title = player['VTI']
subtitle = player['subtitle']
print("> Title :", title, '-', subtitle)
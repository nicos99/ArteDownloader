import urllib.request
import json

print("bonjour", end='')
print("\rla terre !")
exit(0)

json_url = "https://api.arte.tv/api/player/v1/config/fr/088456-001-A"
#json_url = "https://api.arte.tv/api/player/v1/config/fr/083305-001-A"

#s = urllib.request.urlretrieve(json_url)
#print(s, s[0])

rep = urllib.request.urlopen(json_url)
obj = json.load(rep)
#print(obj)
player = obj['videoJsonPlayer']
print(player['VTI'])
flux_replay = player['VSR']
if len(flux_replay) == 0:
    print("Impossible / trop tard !")
else:
    SQ_1 = flux_replay['HTTPS_SQ_1']
    url = SQ_1['url']
    print(url)

# d
import time
progress_old_time = 0.0
MEGA = 1024*1024
def DLCallBack(block_number, block_size, total_size):
    global progress_old_time
    t = time.time()
    if t > progress_old_time + 1:
        curr_size = block_number * block_size
        print(r"Downloading: %4d MO / %d [%04.1f%%]" % (curr_size / MEGA, total_size / MEGA, curr_size * 100. / total_size))
        progress_old_time = t

#url = "http://download.thinkbroadband.com/100MB.zip"
url = "https://arteptweb-a.akamaihd.net/am/ptweb/088000/088400/088456-001-A_SQ_0_VF_04728645_MP4-2200_AMM-PTWEB_1GutY6yvzP.mp4"

# contournement de l'err 403 reçu sur certain site (sans changer de librairie pour 'requests')
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0')

filename, headers = opener.retrieve(url, '10MB', DLCallBack)


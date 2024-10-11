# importeju vardu sarakstu
from word_list import vardi 
# importēju random
import random  

uzminamais_vards = random.choice(vardi)

minejums_burts = input(str("Ievadi burtu ar kuru minēsi")) #jautājums uz kuru var atbildēt ar burtu
minejums_vards = input(str("ievadi vārdu, kuru minēsi"))   # jautājums uz kuru var atbildēt ar vārdu

nepareizie_minejumi = 9  # cik speletajam minejumi ir palikuši

def varda_info_speletajam(): # ko spēlētājs redz
    # saprot cik daudz burtu ir minamajā vārdā un attiecīgi saliek tik daudz _, lai simbolizētu to ,ka spēlētājs nezin šos burtus   
    minamie_burti = ['_'] * len(uzminamais_vards)

def galvenais(): # te norisināsies galvenās funkcijas spēlei
    while nepareizie_minejumi != 0:     
        while minejums_vards != uzminamais_vards:
        
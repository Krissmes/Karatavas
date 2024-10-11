# importeju vardu sarakstu
from word_list import vardi 
# importēju random
import random  
# te es definesu svarigas lietiņas, kas ļaus spēlei strādāt
zimejums = {
    0: ("",
        "",
        "",
        ""), 
    1: ("",
        "",
        "",
        "")
}
def atbilde()
def galvenaslietas():
    # izvēlās mināmo vārdu         
    uzminamais_vards = random.choice(vardi)
    # saprot cik daudz burtu ir minamajā vārdā un attiecīgi saliek tik daudz _, lai simbolizētu to ,ka spēlētājs nezin šos burtus   
    minamie_burti = ['_'] * len(uzminamais_vards)
    # cik spēlētājam ir minējumi
    minejumi = 9
    
    spele_turpinas = True

    while spele_turpinas == True:
        

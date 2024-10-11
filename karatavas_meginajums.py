from word_list import vardi   # importeju vardu sarakstu

# importēju random
import random  

# ar šo funkciju varēs parrādīt informāciju, ko spēlētājs zin.(__a_b_)
def paradi_minamie_burti(minamie_burti):
    print("".join(minamie_burti))


def galvenais(): # te norisināsies galvenās funkcijas spēlei

    # izvēlēs vārdu, kuru spēlētājam ir jāuzmin
    uzminamais_vards = random.choice(vardi)

    # cik speletajam minejumi ir palikuši
    nepareizie_minejumi = 9  

    # saprot cik daudz burtu ir minamajā vārdā un attiecīgi saliek tik daudz _, lai simbolizētu to ,ka spēlētājs nezin šos burtus   
    minamie_burti = ['_'] * len(uzminamais_vards)

    # Šis ir, lai būtu while cikls, kuru es varu beigt, ja spēlētājs uzvar vai zaudē
    spele_iet = True 

    # kamēr spēle iet loop
    while spele_iet == True:
        #šeit ir vizuālās funkcijas un, lai pateiktu spēlētājm cik viņam ir mēģinājumi
        print("tev vēl palikuši", nepareizie_minejumi, "minējumi")
        paradi_minamie_burti(minamie_burti)

        #jautājums uz kuru var atbildēt ar burtu
        minejums_burts = input("Ievadi burtu ar kuru minēsi    ").lower()

        
        # ar šo if loop, pārbauda vai minejums burts ir iekšā uzminamajā vārdā, un, tad attiecīgi rīkojas, ja ir tad atklāj to burtu, ja nē, atņem mēģinājumu.
        if minejums_burts in uzminamais_vards: 
            for x in range(len(uzminamais_vards)):
                # ja uzminēja burtu
                if uzminamais_vards[x] == minejums_burts:
                    minamie_burti[x] = minejums_burts
        # ja neuzminēja burtu
        else:
            nepareizie_minejumi -= 1


        # te ir uzvaras un zaudēšans nosacījumi. Ar šiem beigsies spēle un pateiks vai spēlētājs uzvarēja vai zaudēja
        # ja uzvar
        if "_" not in minamie_burti:
            print("Tu uzminēji :) , vārds ir", uzminamais_vards)
            spele_iet = False
        # ja zaudē
        elif nepareizie_minejumi == 0:
            print("Tu neuzminēji :(  , vārds bija", uzminamais_vards)
            spele_iet = False    

# palaižu funkciju
galvenais()        
        
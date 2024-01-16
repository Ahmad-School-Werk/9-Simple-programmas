def vind_meest_voorkomend_woord(tekst):
    tekst = tekst.lower()
    tekst = ''.join(e for e in tekst if e.isalnum() or e.isspace())  

    woorden = tekst.split()
    print(woorden)
    woord_frequentie = {
    }
    for woord in woorden:
        if woord in woord_frequentie:
            woord_frequentie[woord] += 1
        else:
            woord_frequentie[woord] = 1

    meest_voorkomend_woord = max(woord_frequentie, key=woord_frequentie.get)

    return meest_voorkomend_woord

voorbeeld_tekst = "Dit is een voorbeeld tekst, dit tekst is simple"

resultaat = vind_meest_voorkomend_woord(voorbeeld_tekst)
print("Het meest voorkomende woord is:", resultaat)

def vind_grootste_element(lijst):
    if not lijst:
        return "Lijst is leeg"

    grootste_element = lijst[0]

    for element in lijst[1:]:
        if element > grootste_element:
            grootste_element = element # 

    return grootste_element

getallen = [12, 5, 8, 20, 3, 16] 
resultaat = vind_grootste_element(getallen)
print("Het grootste element is:", resultaat)


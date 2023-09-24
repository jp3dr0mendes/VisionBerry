# import requests

# response = requests.get("http://192.168.56.1:5000/teste")


from math import pi
import numpy as np

fruits = [
    (29.8/2,17.5/2),
    (28/2,24.9/2),
    (26.5/2,23/2),
    (23/2,16/2),
    (28.5/2,19.7/2),
    (26.3/2,21.7/2)
]

list_volumes_cm3 = list()
list_volumes_mm3 = list()

for fruit in fruits:

    volume_mm3 = pi * (4/3) * fruit[0] * fruit[1] ** 2
    volume_cm3 = volume_mm3 / 1000

    list_volumes_mm3.append(volume_mm3)
    list_volumes_cm3.append(volume_cm3)

    # print(f'''
    #     size         : {fruit[0]} x {fruit[1]}
    #     volume em mm3: {volume_mm3}
    #     volume em cm3: {volume_cm3}
    # ''')


list_volumes_cm3 = np.array(list_volumes_cm3)
list_volumes_mm3 = np.array(list_volumes_mm3)

media_cm3 = np.mean(list_volumes_cm3)
media_mm3 = np.mean(list_volumes_mm3)

std_mm3 = np.std(list_volumes_mm3)
std_cm3 = np.std(list_volumes_cm3)

print(f'''
    Média dos volumes         : {media_cm3} cm3 | {media_mm3} mm3
    Desvio Padrão dos volumes : {std_cm3} cm3 | {std_mm3} mm3
''')

# for i in range(len(list_volumes_cm3)):
#     if list_volumes_cm3[i] <= (media_cm3 - (std_cm3 - 0.7)):
#         print(f'''
#     Objeto Identificado!
#     Volume em mm3 : {list_volumes_mm3[i]}
#     Volume em cm3 : {list_volumes_cm3[i]}
#     Classe        : Fruto Inapropriado
#     ''')
#     else:
#         print(f'''
#     Objeto Identificado!
#     Volume em mm3 : {list_volumes_mm3[i]}
#     Volume em cm3 : {list_volumes_cm3[i]}
#     Classes       : Fruto Apropriado
#     ''')
        
# print('''
#     Objeto não identificado
#     ''')

for i in range(len(list_volumes_cm3)):
    if list_volumes_cm3[i] <= media_cm3 :
        print(f'''
    Objeto Identificado!
    Volume em mm3 : {list_volumes_mm3[i]}
    Volume em cm3 : {list_volumes_cm3[i]}
    Classe        : Fruto Inapropriado
    ''')
    else:
        print(f'''
    Objeto Identificado!
    Volume em mm3 : {list_volumes_mm3[i]}
    Volume em cm3 : {list_volumes_cm3[i]}
    Classes       : Fruto Apropriado
    ''')
        
print('''
    Objeto não identificado
    ''')
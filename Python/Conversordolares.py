def conversor(tipo_pesos, dolar):
    pesos = input ("Ingrese la cantidad de pesos " + tipo_pesos+ " que tiene: " )
    pesos = float (pesos)
    dolares = pesos / dolar
    dolares = round (dolares,2)
    dolares = str (dolares)
    print ("Total de pesos convertidos a dolares " + dolares) 

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 

"""

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3800)
elif opcion == 2:
    conversor("Argentinos", 117.45)
elif opcion == 3:
    conversor ("Mexicanos", 25.40)
else:
    print('Ingresa una opcion valida')


option = 1

empanadas = []


while option != 1:
    print('***empanadas***')
    print('***opcion 1 = Ingrese una empanada***')
    print('***opcion 2 = mostrar todas las empanadas***')
    print('***opcion 3 = buscar empanadas por Id ***')
    print('***opcion 4 = editar una empanada ***')
    print('***opcion 5 = eliminar empanada***')
    print('***opcion 0 = salir***')

    option = int(input('escoja una opcion...:'))

if (option == 1):
    empanada = {}
    empanada['id'] = int(input("ingrese id empanada:"))
    empanada['nombre'] = input('digite nombre empanada')
    empanada['precio'] = input('digite precio empanada')
    empanada['popularidad'] = input('ingrese pupularidad de la empanada')
    empanada['fechaVencimiento'] = input(
        'ingrese fechaVencimiento de la empanada')

    empanadas.append(empanada)

    print('empanadas registradas...')


elif (option == 2):
    for empanada in empanadas:
        print(empanada)
elif (option == 3):
    buscarEmpanada = int(input('digite id empanada:'))
    for empanada in empanadas:
        if (empanada['id'] != buscarEmpanada):
            print('sin empanada')
        else:
            print(f'empanada encontrada{empanada}')
elif (option == 4):
    buscarEmpanada = int(input('digite id empanada:'))
    for empanada in empanadas:
        if (empanada['id'] != buscarEmpanada):
            print('sin empanada')
        else:
          print('el precio actual de la empanada es ')
          print(empanada['precio'])
          empanada['precio']=float(input('digita el nuevo precio:'))
          
elif (option == 5):
    pass
elif (option == 0):
    pass
else:
    print('opcion invalida')

#Nombre de la empresa: 2000 Automoviles
#Lista de autos: n autos
#Datos a ingresar: DNI (o pasaporte), Nombre, Apellido, Domicilio, empresa, telefono laboral, domicilio laboral,
#Local, turista nacional, turista internacional, referencia para el hotel o agencia asociada, VIP.
#Datos del vehiculo: Modelo, numero de chasis, motor, tipo de vehiculo (camioneta, auto 4p, convertible, etc.)
#Atributos incorporados a Bariloche: 4x4(booleano, obligatorio p/ terreno montanoso y ripio),
#equipamiento para nieve(cadenas, neumaticos especiales), permiso municipal(codigo de calcomania habilitante emitido por la muni)
#Tarifas de alquiler(codigo y nombre): diaria, fin de semana, semana, mes o superior
#Tarifas de temporada: Temporada alta (Junio a Septiembre(invierno), Diciembre a febrero(verano))
#Tarifas por zona: Circuito chico, Cerro catedral, Ruta 40
#Recargos segun temporada y zona.
#Se cobra un seguro brindado por la comision nacional de seguro. Se registra codigo, nombre e importe.
#El importe no varia segun el vehiculo. Se agrega un seguro especial para rutas de tierra y danos por nieve.

#Proceso de alquiler: El cliente solicita un modelo de vehiculo y se verifica disponibilidad. Si hay vehiculo, se asigna y se
#piden los datos. Si no, se regista el motivo de rechazo. Se debe validar que el solicitante sea mayor de 25 anos, que tenga
#licencia de conducir habilitada, y en caso de ser extranjero que posea licencia internacional para turistas.

#Una vez cumplidos los requisitos se genera factura, por alquiler, datos del cliente, vehiculo, tarifa, seguros, periodo de
#alquiler, recargos por temporada y zona, descuento VIP si corresponde. El encargado de la playa registra la devolucion, 
#se envia copia de la factura al cliente y se archiva otra.

#El cliente puede pagar de forma parcial o total. Cada pago se registra con DNI, fecha, numero de factura, importe abonado y
#saldo pendiente. No se aceptan pagos mayores a la deuda.

"""Diagrama de flujo

Vehiculos = {modelo: num_chasis}
Vehiculos2 = {modelo: motor}
Vehiculos3 {modelo: tipo_vehiculo}

Ingresar año actual
Imprimir Vehiculos
Ingresar modelo de vehiculo
si modelo de vehiculo no tiene disponibilidad:
    rechazar pedido y explicar motivo
sino:
    pedir edad
    pedir vencimiento de licencia de conducir
        si edad < 25 o vencimiento_lc == año actual:
            rechazar pedido y explicar motivo
    pedir_datos()

pedir_datos():
    ingresar DNI o pasaporte, Nombre, Apellido, Domicilio, empresa, telefono laboral, domicilio laboral,
    si es Local turista nacional o turista internacional, referencia para el hotel o agencia asociada, VIP.

calcular_tarifa():
    Segun sea tiempo_estadia (1, 2, 3, 4)
        Caso 1: diaria
        Caso 2: fin de semana
        Caso 3: semana
        Caso 4: mes o sup
    
    Si el cliente es de bari:
        ingresar preguntar_de_que_zona_es
        tarifa = tiempo_estadia + zona
    Sino:
        tarifa = tiempo_estadia
    si es temporada:
        tarifa + temporada

forma_pago():
    ingresar forma_pago
    
    si forma_pago == total:
        imprimir tarifa
        ingresar pago
        
    sino si pago == parcial:
        ingresar cuotas 3, 6, 12
        si cuotas == 3:
            tarifa += 5%
        sino si cuotas == 6:
            tarifa += 10%
        sino si cuotas == 12:
            tarifa += 15%
    
    si VIP == True:
        tarifa -= 20%
        
    imprimir tarifa
            
    mientras pago > tarifa
        ingresar pago
        imprimir "no se aceptan pagos mayores a la deuda"
        
    generar_factura():
    imprimir datos_cliente, datos_vehiculo, tarifa, seguros, periodo_alquiler, recargos_temporada_zona, desc_VIP
    
"""

edad = int(input("Ingrese su edad: "))
año_actual = int(input("Ingrese el año actual"))
venc_lic = int(input("Ingrese la fecha de vencimiento de su licencia de conducir: "))
vehiculos = {"Nissan Versa": "ABC123", "Jeep Wrangler": "SDF295", "Ford Hilux" : "NVI285", "Volkswagen Gol" : "NPH954"}

while True:
    if edad < 25:
        print("Usted no es mayor de 25 años, su solicitud ha sido rechazada.")
        break
    elif venc_lic == año_actual:
        print("Su licencia de conducir ha caducado, su solicitud ha sido rechazada.")
        break

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido")
    dni = input("Ingrese su DNI o numero de pasaporte")
    domicilio = input("Ingrese su domicilio")
    empresa = input("Ingrese la empresa en la que trabaja: ")
    cel = input("Ingrese su número de telefono: ")
    
    vip = int(input("Si usted es VIP, ingrese su credencial. De lo contrario, ingrese un 0: "))
    
    forma_pago = input("Usted va a pagar con efectivo o crédito?: ").lower()
    if forma_pago is not "efectivo" or "credito":
        forma_pago = input("Usted va a pagar con efectivo o crédito?: ").lower()
        continue
    
    bari = input("Es usted de bariloche?: ").lower()
    if bari is not "si" or "no":
        bari = input("Es usted de bariloche?: ").lower()
        continue

    if bari == "si":
        print(f"Los vehiculos disponibles son:\n{vehiculos[2]}, {vehiculos.keys[2]}\n{vehiculos[3]}, {vehiculos.keys[3]}")
    else:
        print(f"Los vehiculos disponibles son:\n{vehiculos[0]}, {vehiculos.keys[0]}\n{vehiculos[1]},{vehiculos.keys[1]}\n{vehiculos[2]}, {vehiculos.keys[2]}\n{vehiculos[3]}, {vehiculos.keys[3]}")

    temp_alta = input("Es temporada alta?: ")
    if temp_alta is not "si" or "no":
        bari = input("Es temporada alta?: ").lower()
        continue
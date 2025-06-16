"""edad = int(input("Ingrese su edad: "))
año_actual = int(input("Ingrese el año actual"))
venc_lic = int(input("Ingrese la fecha de vencimiento de su licencia de conducir: "))
vehiculos = {"Nissan Versa": "ABC123", "Jeep Wrangler": "SDF295", "Ford Hilux" : "NVI285", "Volkswagen Gol" : "NPH954"}
tarifa = 0
tarifa_final = 0

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
    
    forma_pago = input("Usted va a pagar con efectivo o crédito (efectivo-crédito?): ").lower()
    if forma_pago is not "efectivo" or "credito":
        forma_pago = input("Usted va a pagar con efectivo o crédito? (efectivo-crédito?): ").lower()
        continue
    if forma_pago == "credito":
        tarifa_final += 30
    
    vip = int(input("Si usted es VIP, ingrese su credencial. De lo contrario, ingrese un 0: "))
    
    bari = input("Es usted de bariloche?(si-no): ").lower()
    if bari is not "si" or "no":
        bari = input("Es usted de bariloche(si-no)?: ").lower()
        continue

    if bari == "si":
        print(f"Los vehiculos disponibles son:\n3:{vehiculos[2]}, {vehiculos.keys[2]}\n4:{vehiculos[3]}, {vehiculos.keys[3]}")
    else:
        print(f"Los vehiculos disponibles son:\n1:{vehiculos[0]}, {vehiculos.keys[0]}\n2:{vehiculos[1]},{vehiculos.keys[1]}\n3:{vehiculos[2]}, {vehiculos.keys[2]}\n4:{vehiculos[3]}, {vehiculos.keys[3]}")
        elegir_vehiculo = int(input("Elija un auto de los presentados anteriormente (1-2-3-4): "))
        vehiculo_elegido = vehiculos[elegir_vehiculo]
        patente_vehiculo_elegido = vehiculos.keys[elegir_vehiculo]
        tarifa += 400000
        
        temp_alta = input("Es temporada alta? (si-no): ")
        if temp_alta is not "si" or "no":
                temp_alta = input("Es temporada alta? (si-no): ").lower()
                continue
        if temp_alta == "si":
            tarifa_final += 20
        
        zona_geo = input("Indique si va a manejar por los siguientes lugares\n1: Circuito Chico\n2: Cerro catedral\n3: Ruta 40\n ")
        tarifa_final += 10"""
        
        
#Declaracion de variables
año_actual = int(input("Ingrese el año actual: "))
tarifa = 20000 #Seguro inicial

#Pregunta si hay vehiculos disponibles
veh_disp = input("Hay vehiculo disponible? (si-no): ").lower()
if veh_disp == "si":
    #Toma los datos del cliente
    def datos_cliente():
        edad = int(input("Ingrese su edad: "))
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        dni = int(input("Ingrese su DNI o numero de pasaporte: "))
        domicilio = input("Ingrese su domicilio: ")
        empresa = input("Ingrese la empresa en la que trabaja: ")
        cel = int(input("Ingrese su número de telefono: "))
        venc_lic = int(input("Ingrese la fecha de vencimiento de su licencia de conducir: "))
        #Pregunta si es turista y pide un hotel de referencia
        turista = input("Es usted turista? (si-no): ").lower()
        hotel = None
        if turista == "si":
            hotel = input("Ingrese un hotel de referencia: ")
        #Pregunta si es VIP y aplica un descuento
        vip = input("Es usted VIP? (si-no): ").lower()
        desc_vip = 0
        if vip == "si":
            desc_vip = 0.15
        #Pregunta la forma de pago
        forma_pago = input("Usted pagará en crédito o efectivo?: ")
            
        return edad, nombre, apellido, dni, domicilio, empresa, cel, turista, hotel, desc_vip, forma_pago, venc_lic

    edad, nombre, apellido, dni, domicilio, empresa, cel, turista, hotel, desc_vip, forma_pago, venc_lic = datos_cliente()
    #Verifica que sea mayor de 25 y que tenga licencia válida
    if edad >= 25:
        if venc_lic >= año_actual:
            #Verifica que sea de Bariloche
            bari = input("Es la solicitud para Bariloche? (si-no): ").lower()
            if bari == "si":
                
                def mod_bariloche():
                    tarifa_1 = 0
                    #Agrega tarifas para vehiculos 4x4 y equipo de nieve
                    cuatroxcuatro = input("Usted utilizara un vehículo 4x4? (si-no): ").lower()
                    if cuatroxcuatro == "si":
                        tarifa_1 = tarifa_1 + 20000
                    equip_invierno = input("Usted necesitara equipo de invierno? (si-no): ").lower()
                    if equip_invierno == "si":
                        tarifa_1 = tarifa_1 + 20000
                    #Registra el modelo y la patente del vehiculo a utilizar
                    modelo_veh = input("Ingrese el modelo del vehiculo: ")
                    patente_veh = input("Ingrese la patente del vehiculo: ")
                    #Pregunta si va a andar por estas zonas geograficas y aplica tarifas
                    zona_geo = "a"
                    while zona_geo != "s":
                        zona_geo = input("Ingrese una de las siguientes zonas:\nCircuito Chico\nCerro Catedral\nRuta 40\nO ingrese 'S' para salir: ").lower()
                        if zona_geo == "circuito chico":
                            tarifa =+ 20000
                        elif zona_geo == "cerro catedral":
                            tarifa_1 = tarifa_1 + 20000
                        elif zona_geo == "ruta 40": #Podria agregarse validacion de que ya se ingreso una zona geografica
                            tarifa_1 = tarifa_1 + 20000
                        elif zona_geo != "circuito chico" or "cerro catedral" or "ruta 40":
                            print("Ingrese una zona válida")
                    #Pregunta si es temporada alta y aplica tarifas
                    temp_alta = input("Es para temporada alta? (si-no): ").lower()
                    if temp_alta == "si":
                        tarifa_1 = tarifa_1 + 20000
                    
                    tarifa_1 = tarifa_1 + 20000 #Seguro especial de Bariloche
                    
                    return tarifa_1, modelo_veh, patente_veh
                tarifa_1, modelo_veh, patente_veh = mod_bariloche()
                
                tarifa = tarifa + tarifa_1
            else:
                #Registra el modelo y patente del vehiculo
                modelo_veh = input("Ingrese el modelo del vehiculo: ")
                patente_veh = input("Ingrese la patente del vehiculo: ")
            
            def modTarifa_por_tiempo():
                tarifa_2 = 0
                #Pregunta el tiempo de alquiler del vehiculo
                timepo_alquiler = input("Ingrese la duracion del alquiler (diaria-fin de semana-semana-mes o superior): ").lower()
                if timepo_alquiler == "diaria":
                    tarifa_2 = tarifa_2 + 20000
                elif timepo_alquiler == "fin de semana":
                    tarifa_2 = tarifa_2 + 20000
                elif timepo_alquiler == "semana":
                    tarifa_2 = tarifa_2 + 20000
                elif timepo_alquiler == "mes superior":
                    tarifa_2 = tarifa_2 + 20000
                
                return tarifa_2
            tarifa_2 = modTarifa_por_tiempo()
            tarifa = tarifa + tarifa_2
            
            tarifa = tarifa * desc_vip
            
            print(f"La tarifa final es de ${tarifa}")
            pago = float(input("Ingrese el monto a pagar: "))
            while pago > tarifa:
                print(f"El pago no puede ser mayor que la tarifa de ${tarifa}")
                pago = float(input("Ingrese el monto a pagar: "))
            
            comprobante = f"{nombre} {apellido}\n {edad} años\n dni {dni}\n celular {cel}\n domicilio {domicilio}\n foroma de pago en {forma_pago}\n hotel de referencia {hotel}\n tarifa a pagar {tarifa}\n empresa {empresa}"
            print(comprobante)
            
        #La licencia esta vencida
        elif venc_lic < año_actual:
            print("El solicitante on cuenta con una licencia habilitante válida")
    #El solicitante es menor de 25 años
    elif edad < 25:
        print("El solicitante no cuenta con la edad minima requerida")
        
        
elif veh_disp == "no":
    print("No hay vehiculos disponibles")
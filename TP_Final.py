#Trabajo Práctico final
#Intorducción a la Ingenieria en Computación, Comisión 1
#Tomas Bizzarri, Federico García

#Declaracion de variables
año_actual = int(input("\nIngrese el año actual: "))
tarifa = 20000 #Seguro inicial
#Función de Toma de datos del cliente
def datos_cliente():
    edad = int(input("\nIngrese su edad: "))
    nombre = input("\nIngrese su nombre: ")
    apellido = input("\nIngrese su apellido: ")
    dni = input("\nIngrese su DNI o numero de pasaporte: ")
    domicilio = input("\nIngrese su domicilio: ")
    empresa = input("\nIngrese la empresa en la que trabaja: ")
    cel = input("\nIngrese su número de telefono: ")
    venc_lic = int(input("\nIngrese la fecha de vencimiento de su licencia de conducir: "))
    #Pregunta si es turista y pide un hotel de referencia
    turista = input("\nEs usted turista? (si-no): ").lower()
    hotel = None
    if turista == "si":
        hotel = input("Ingrese un hotel de referencia: ")
    #Pregunta si es VIP y aplica un descuento
    vip = input("\nEs usted VIP? (si-no): ").lower()
    desc_vip = 0
    if vip == "si":
        desc_vip = 0.15
    #Pregunta la forma de pago
    forma_pago = input("\nUsted pagará en crédito o efectivo?: ")
        
    return edad, nombre, apellido, dni, domicilio, empresa, cel, turista, hotel, desc_vip, forma_pago, venc_lic



#Función de Calculo de tarifas para Bariloche
def mod_bariloche():
    tarifa_1 = 0
    #Agrega tarifas para vehiculos 4x4 y equipo de nieve
    cuatroxcuatro = input("\nUsted utilizara un vehículo 4x4? (si-no): ").lower()
    if cuatroxcuatro == "si":
        tarifa_1 = tarifa_1 + 20000
    equip_invierno = input("\nUsted necesitara equipo de invierno? (si-no): ").lower()
    if equip_invierno == "si":
        tarifa_1 = tarifa_1 + 20000
    #Registra el modelo y la patente del vehiculo a utilizar
    modelo_veh = input("\nIngrese el modelo del vehiculo: ")
    patente_veh = input("\nIngrese la patente del vehiculo: ")
    #Pregunta si va a andar por estas zonas geograficas y aplica tarifas
    zona_geo = "a"
    while zona_geo != "s":
        zona_geo = input("\nIngrese una de las siguientes zonas:\nCircuito Chico\nCerro Catedral\nRuta 40\nO ingrese 'S' para salir: ").lower()
        if zona_geo == "circuito chico":
            tarifa_1 =+ 20000
        elif zona_geo == "cerro catedral":
            tarifa_1 = tarifa_1 + 20000
        elif zona_geo == "ruta 40": #Podria agregarse validacion de que ya se ingreso una zona geografica
            tarifa_1 = tarifa_1 + 20000
        elif zona_geo != "circuito chico" or "cerro catedral" or "ruta 40":
            print("\nIngrese una zona válida")
    #Pregunta si es temporada alta y aplica tarifas
    temp_alta = input("\nEs para temporada alta? (si-no): ").lower()
    if temp_alta == "si":
        tarifa_1 = tarifa_1 + 20000
    
    tarifa_1 = tarifa_1 + 20000 #Seguro especial de Bariloche
    
    return tarifa_1, modelo_veh, patente_veh

#Función de modificación de tarifa por timepo de estadia
def modTarifa_por_tiempo():
    tarifa_2 = 0
    #Pregunta el tiempo de alquiler del vehiculo
    timepo_alquiler = input("\nIngrese la duracion del alquiler (diaria-fin de semana-semana-mes o superior): ").lower()
    if timepo_alquiler == "diaria":
        tarifa_2 = tarifa_2 + 20000
    elif timepo_alquiler == "fin de semana":
        tarifa_2 = tarifa_2 + 20000
    elif timepo_alquiler == "semana":
        tarifa_2 = tarifa_2 + 20000
    elif timepo_alquiler == "mes o superior":
        tarifa_2 = tarifa_2 + 20000
    return tarifa_2


#Pregunta si hay vehiculos disponibles
veh_disp = input("\nHay vehiculo disponible? (si-no): ").lower()
if veh_disp != "si":
    print("\nNo hay vehiculos disponibles")
    quit()
    
#Pregunta los datos del cliente
edad, nombre, apellido, dni, domicilio, empresa, cel, turista, hotel, desc_vip, forma_pago, venc_lic = datos_cliente()

#Verifica que sea mayor de 25 y que tenga licencia válida
if edad < 25:
    print("\nEl solicitante no cuenta con la edad minima requerida")
    quit()
if venc_lic < año_actual:
    print("\nEl solicitante on cuenta con una licencia habilitante válida")
    quit()
    
#Verifica que sea de Bariloche
bari = input("\nEs la solicitud para Bariloche? (si-no): ").lower()
if bari == "si":
    tarifa_1, modelo_veh, patente_veh = mod_bariloche()
    tarifa += tarifa_1
    
else:
    #Registra el modelo y patente del vehiculo
    modelo_veh = input("\nIngrese el modelo del vehiculo: ")
    patente_veh = input("\nIngrese la patente del vehiculo: ")

tarifa_2 = modTarifa_por_tiempo()
tarifa += tarifa_2
#Aplica descuento vip
tarifa_final = tarifa * (1 - desc_vip)

print(f"\nLa tarifa final es de ${tarifa}")
pago = float(input("\nIngrese el monto a pagar: "))
while pago > tarifa:
    print(f"\nEl pago no puede ser mayor que la tarifa de ${tarifa_final}")
    pago = float(input("\nIngrese el monto a pagar: "))

comprobante = (
    f"{nombre} {apellido}\n"
    f"{edad} años\n"
    f"DNI: {dni}\n"
    f"Celular: {cel}\n"
    f"Domicilio: {domicilio}\n"
    f"Forma de pago: {forma_pago}\n"
    f"Hotel de referencia: {hotel}\n"
    f"Tarifa a pagar: ${tarifa}\n"
    f"Empresa: {empresa}\n"
    f"Modelo de vehículo: {modelo_veh} - Patente: {patente_veh}"
)
print("\nComprobante:")
print(comprobante)
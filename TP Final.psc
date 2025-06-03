Algoritmo sin_titulo
	
	imprimir "Ingrese el año actual: "
	Leer año_actual
	imprimir "Ingrese el mes actual del 1 al 12: "
	leer mes
	imprimir "Ingrese su edad: "
	Leer edad
	Imprimir "Ingrese el vencimiento de su licencia de conducir: "
	leer venc_lc
	Si edad < 25 o venc_lc == año_actual Entonces
		Imprimir "Su solicitud fue rechazada"
	FinSi
	
	Imprimir "Ingrese su nombre: "
	leer nombre
	Imprimir "Ingrese su apellido: "
	leer apellido
	imprimir "Ingrese su domicilio: "
	leer domicilio
	imprimir "Ingrese la empresa en la que trabaja: "
	leer empresa 
	imprimir "Ingrese el domicilio laboral de la empresa: "
	leer domicilio_laboral
	imprimir "Ingrese el telefono laboral de la empresa: "
	leer telefono_laboral 
	
	imprimir "Usted es de Bariolche? (1 - Si, 2 - No): "
	Leer bari 
	
	imprimir "Usted manejará por terreno montañoso y/o rutas de ripio? (1 - Si, 2 - No): "
	leer camioneta

	Si camioneta == 1 Entonces
		Imprimir vehiculos camioneta
	FinSi
	
	si camioneta == 2 entonces
		imprimir vehiculos
	FinSi
	
	imprimir "De la lista de vehiculos disponibles, elija uno: "
	leer vehiculo
	
	Si bari == 2 Entonces
		imprimir "Usted es turista internacional? (1 - Si, 2 - No)"
		leer internacional 		
	FinSi
	
	si bari == 1 Entonces
		Imprimir "Usted manejará por circuito chico, cerro catedral o ruta 40? (1 - Si, 2 - No)"
		leer zona 
		si zona == 1 Entonces
			zona = 20000
		FinSi
		
		si zona == 2 Entonces
			zona = 0
		FinSi
	FinSi
	
	imprimir "Usted es VIP? (1 - Si, 2 - No): "
	leer vip 
	si vip == 1 Entonces
		vip = 0.2
	FinSi
	Si vip == 2 Entonces
			vip = 1
	FinSi
		
	Si internacional == Verdadero Entonces
		imprimir "Ingrese un hotel o agencia de referencia"
		leer hotel_agencia 
	FinSi
	
		imprimir "Cuanto sera su tiempo de estadia? Diaria, fin de semana, semanal o mes y superior? (1, 2, 3, 4)"
		segun caso hacer
			1: estadia = 20000
			2: estadia = 35000
			3: estadia = 100000
			4: estadia = 500000
		FinSegun
		
		temporada = 0
		Si mes >= 1 y mes <= 2 o mes >= 7 y mes <= 8 Entonces
			temporada = 30000
		FinSi
	
	tarifa = estadia + zona + temporada
	tarifa = tarifa * vip
	
	Imprimir "Abonará en un solo pago o de forma parcial? (1 - directo, 2 - parcial)"
	leer forma_pago
	si forma_pago == 1 Entonces
		imprimir "Debera abonar la cantidad de: "
		imprimir tarifa
		Imprimir "Ingrese el pago: "
		leer pago
	FinSi
	Imprimir "Ingrese la cantidad de cuotas a pagar: "
	si forma_pago == 2 Entonces
		segun caso hacer
			1: tarifa = tarifa*0.05
			2: tarifa = tarifa*0.1
			3: tarifa = tarifa*0.15
		FinSegun
		imprimir "Debera abonar la cantidad de: "
		imprimir tarifa
		Imprimir "Ingrese el pago: "
		leer pago
	FinSi
	
	mientras pago > tarifa Hacer
		Imprimir "Ingrese un pago menor a la tarifa: "
		leer pago
	FinMientras
FinAlgoritmo


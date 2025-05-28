#Nombre de la empresa: 2000 Automoviles
#Lista de autos: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
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

#Proceso de alquiler: El cliente solicita un modelo de vehiculo y se verifica disponibilidad. Si hay vehiculo, se asigna y se.
#piden los datos. Si no, se regista el motivo de rechazo. Se debe validar que el solicitante sea mayor de 25 anos, que tenga
#licencia de conducir habilitada, y en caso de ser extranjero que posea licencia internacional para turistas.

#Una vez cumplidos los requisitos se genera factura, por alquiler, datos del cliente, vehiculo, tarifa, seguros, periodo de
#alquiler, regargos por temporada y zona, descuento VIP si corresponde. El encargado de la playa registra la devolucion, 
#se envia copia de la factura al cliente y se archiva otra.

#El cliente puede pagar de forma parcial o total. Cada pago se registra con DNI, fecha, numero de factura, importe abonado y
#saldo pendiente. No se aceptan pagos mayores a la deuda.


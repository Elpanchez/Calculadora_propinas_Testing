# language: es
Característica: Cálculo de propinas
  Como usuario
  Quiero calcular la propina sobre el total de mi cuenta
  Para saber cuánto pagar en total

  Escenario: Calcular una propina del 15%
    Dado que el monto de la cuenta es 100
    Y el porcentaje de propina es 15
    Cuando realizo el cálculo
    Entonces el valor de la propina debe ser 15
    Y el total a pagar debe ser 115

  Escenario: Calcular una propina del 20%
    Dado que el monto de la cuenta es 50
    Y el porcentaje de propina es 20
    Cuando realizo el cálculo
    Entonces el valor de la propina debe ser 10
    Y el total a pagar debe ser 60

  Escenario: Calcular una propina con valores decimales
    Dado que el monto de la cuenta es 123.45
    Y el porcentaje de propina es 18
    Cuando realizo el cálculo
    Entonces el valor de la propina debe ser 22.22
    Y el total a pagar debe ser 145.67

  Escenario: Calcular una propina con valores negativos
    Dado que el monto de la cuenta es -50
    Y el porcentaje de propina es 10
    Cuando realizo el cálculo
    Entonces debe lanzarse un error indicando "El monto y el porcentaje no pueden ser negativos."

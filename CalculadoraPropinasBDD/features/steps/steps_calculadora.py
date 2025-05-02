import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import math
from behave import given, when, then
from calculadora_propinas import calcular_propina

@given(u'que el monto de la cuenta es 100')
def step_impl(context):
    context.monto = 100

@given(u'el porcentaje de propina es 15')
def step_impl(context):
    context.porcentaje = 15

@when(u'realizo el cálculo')
def step_impl(context):
    try:
        context.propina, context.total = calcular_propina(context.monto, context.porcentaje)
    except ValueError as e:
        context.error_message = str(e)

@then(u'el valor de la propina debe ser 15')
def step_impl(context):
    assert context.propina == 15

@then(u'el total a pagar debe ser 115')
def step_impl(context):
    assert context.total == 115

@given(u'que el monto de la cuenta es 50')
def step_impl(context):
    context.monto = 50

@given(u'el porcentaje de propina es 20')
def step_impl(context):
    context.porcentaje = 20

@then(u'el valor de la propina debe ser 10')
def step_impl(context):
    assert context.propina == 10

@then(u'el total a pagar debe ser 60')
def step_impl(context):
    assert context.total == 60

@given(u'el porcentaje de propina es 18')
def step_impl(context):
    context.porcentaje = 18

@given(u'que el monto de la cuenta es 123.45')
def step_impl(context):
    context.monto = 123.45

@then(u'el valor de la propina debe ser 22.22')
def step_impl(context):
    assert round(context.propina, 2) == 22.22  # Comparación con redondeo a dos decimales

@then(u'el total a pagar debe ser 145.67')
def step_impl(context):
    assert round(context.total, 2) == 145.67  # Comparación con redondeo a dos decimales

# Caso con valores negativos
@given(u'que el monto de la cuenta es -50')
def step_impl(context):
    context.monto = -50

@given(u'el porcentaje de propina es 10')
def step_impl(context):
    context.porcentaje = 10

@then(u'debe lanzarse un error indicando "El monto y el porcentaje no pueden ser negativos."')
def step_impl(context):
    try:
        calcular_propina(context.monto, context.porcentaje)
        assert False, "Se esperaba una excepción"
    except ValueError as e:
        assert str(e) == "El monto y el porcentaje no pueden ser negativos."
        
#Comentario de prueba

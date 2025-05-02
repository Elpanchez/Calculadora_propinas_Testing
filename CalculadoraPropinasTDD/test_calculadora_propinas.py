from calculadora_propinas import calcular_propina

def test_propina_10_por_ciento():
    propina, total = calcular_propina(100.0, 10)
    assert propina == 10.0
    assert total == 110.0

def test_propina_20_por_ciento():
    propina, total = calcular_propina(100.0, 20)
    assert propina == 20.0
    assert total == 120.0

def test_propina_15_por_ciento():
    propina, total = calcular_propina(50.0, 15)
    assert propina == 7.5
    assert total == 57.5

def test_monto_cero():
    propina, total = calcular_propina(0.0, 10)
    assert propina == 0.0
    assert total == 0.0

def test_porcentaje_cero():
    propina, total = calcular_propina(200.0, 0)
    assert propina == 0.0
    assert total == 200.0

def test_monto_negativo_lanza_error():
    import pytest
    with pytest.raises(ValueError):
        calcular_propina(-50.0, 10)

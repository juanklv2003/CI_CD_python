from src.main import elevar, upper, hola

def test_elevar_basico():
    assert elevar(2,3)==8

def test_to_upper():
    assert upper("Carlos")=="CARLOS"

def test_hola():
    assert  hola=="adioe"

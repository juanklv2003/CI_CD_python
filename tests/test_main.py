from src.main import elevar, upper

def test_elevar_basico():
    assert elevar(2,3)==8

def test_to_upper():
    assert upper("Carlos")=="CARLOS"

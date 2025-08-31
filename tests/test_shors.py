
from src import circuits

def test_shor_demo():
    p, q = circuits.demo_shor_educational(15)
    assert p * q == 15

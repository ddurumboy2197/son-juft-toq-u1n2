# test_parity.py
import pytest

def test_juft_son():
    assert parity(2) == "Juft"

def test_toq_son():
    assert parity(3) == "Toq"

def test_manfiy_son():
    assert parity(-2) == "Juft"

def test_nol():
    assert parity(0) == "Juft"

def parity(n):
    if n % 2 == 0:
        return "Juft"
    else:
        return "Toq"

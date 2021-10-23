import pytest
from solutions.CHK import checkout_solution

@pytest.mark.parametrize("skus, total",[
    ("AAA", 130),
    ("BB" , 45),
    ("BBBEEEE", 190),
    ("BB EEEEE AAAAA AAA",530),
    ("FFFF", 20),
    ("", 0),
    (" ", 0),
    ("%$£", -1),
    ("AAbc", -1),
    ("762354", -1)
])

def test_calculation(skus, total):
    assert checkout_solution.checkout(skus) == total


import pytest
from solutions.CHK import checkout_solution

@pytest.mark.parametrize("skus, total",[
    ("AAA", 130),
    ("BB" , 45),
    ("AAbc", -1),
    ("AAAHN", -1),
    ("aabbcdd12", -1),
    ("762354", -1)
])

def test_calculation(skus, total):
    assert checkout_solution.checkout(skus) == total




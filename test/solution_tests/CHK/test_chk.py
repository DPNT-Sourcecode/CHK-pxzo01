import pytest
from solutions.CHK import checkout_solution

@pytest.mark.parametrize("skus, total",[
    ("aaa", 130),
    ("bb" , 45),
    ("aabbcdd12", 193)
])

def test_calculation(skus, total):
    assert checkout_solution.checkout(skus) == total

import pytest
import tdd

def test_a_neg():
    assert tdd.n_neg('E') == 1
    assert tdd.n_neg('D') == 1
    assert tdd.n_neg('')  == 0
    assert tdd.n_neg('ACKLWTTAE') == 1
    assert tdd.n_neg('acklwttae') == 1

    pytest.raises(RuntimeError, "tdd.n_neg('Z')")

    return None

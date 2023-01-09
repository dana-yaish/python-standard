import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False

def test_covered4():
    assert index.covered4() == True
# def test_fully_covered():
#     assert index.fully_covered() == True





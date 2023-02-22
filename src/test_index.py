import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False

def test_fully_covered():
    assert index.fully_covered() == True

def test1():
    assert index.uncovered5() == False

def test2():
    assert index.uncovered4() == True



import pytest
from matrix_counter import *

# UNIT test
def test_parse_matrix():
    s = '[[1,2],[3,4]]'
    result = parse_matrix(s)
    expected = np.array([[1,2],[3,4]])
    assert (result == expected).all()

def test_matrix_addition():
    A = np.array([[1,2], [3,4]])
    B = np.array([[5,6], [7,8]])
    result = matrix_addition(A, B)
    expected = np.array([[6, 8], [10, 12]])
    assert (result == expected).all()

def test_matrix_subtraction():
    A = np.array([[1,2], [3,4]])
    B = np.array([[5,6], [7,8]])
    result = matrix_subtraction(A, B)
    expected = np.array([[-4,-4],[-4,-4]])
    assert (result == expected).all()

def test_matrix_multiplication():
    A = np.array([[1,2], [3,4]])
    B = np.array([[5,6], [7,8]])
    result = matrix_multiplication(A, B)
    expected = np.array([[19,22],[43,50]])
    assert (result == expected).all()

def test_matrix_scaling():
    A = np.array([[1,2], [3,4]])
    num = 2
    result = matrix_scaling(A, num)
    expected = np.array([[2, 4], [6, 8]])
    assert (result == expected).all()

def test_matrix_determinant():
    A = np.array([[1,2], [3,4]])
    result = matrix_determinant(A)
    expected = -2
    assert result == expected
                    
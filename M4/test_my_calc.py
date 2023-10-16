import pytest
from my_calc import MyCalc

@pytest.fixture
def calculator():
    return MyCalc()
# Parameterized test for addition
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-2, 3, 1), (-12, 3, -9)])
def test_number_add_number(calculator, a, b, expected):
    result = calculator.add(a, b)
    assert result == expected

# Parameterized test for subtraction
@pytest.mark.parametrize("a, b, expected", [(5, 2, 3), (8, 3, 5), (-5, -3, -2)])
def test_number_sub_number(calculator, a, b, expected):
    result = calculator.sub(a, b)
    assert result == expected

# Parameterized test for multiplication
@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (-2, 3, -6), (0, 5, 0)])
def test_number_mult_number(calculator, a, b, expected):
    result = calculator.mult(a, b)
    assert result == expected

# Parameterized test for division
@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (-6, 2, -3), (0, 5, 0)])
def test_number_div_number(calculator, a, b, expected):
    result = calculator.div(a, b)
    assert result == expected

def test_ans_add_number():
    calc = MyCalc()
    data = [{"a": "15","b": "5","r": "20"},{"a": "ans","b": "4","r": "24"},{"a": "ans","b": "1","r": "25"}, ]
    for d in data:
        assert calc.add(d["a"], d["b"]) == int(d["r"])
#UCID : ss4746
#Date : 10-15-2023
# UCID:ss4746
# Date: 15-10-2023
# This method involves three test cases, where a series of data is passed as input. 
# In the first test case, we provide values, and the result of this test case is used as input for the subsequent series of tests. 
# In the second test, we pass a number and compare it with the previously passed value. 
# A loop iterates through all three test cases by invoking the "addition" method and returns whether each case has passed or failed.

def test_ans_sub_number():
    calc = MyCalc()
    data = [{"a": "15","b": "5","r": "10"},{"a": "ans","b": "4","r": "6"},{"a": "ans","b": "1","r": "5"}, ]
    for d in data:
        assert calc.sub(d["a"], d["b"]) == int(d["r"])
#UCID : ss4746
#Date : 10-15-2023
# UCID:ss4746
# Date: 15-10-2023
# This method involves three test cases, where a series of data is passed as input. 
# In the first test case, we provide values, and the result of this test case is used as input for the subsequent series of tests. 
# In the second test, we pass a number and compare it with the previously passed value. 
# A loop iterates through all three test cases by invoking the "subtraction" method and returns whether each case has passed or failed.

def test_ans_mult_number():
    calc = MyCalc()
    data = [{"a": "-5","b": "-5","r": "25"},{"a": "ans","b": "4","r": "100"},{"a": "ans","b": "1","r": "100"}, ]
    for d in data:
        assert calc.mult(d["a"], d["b"]) == int(d["r"])
#UCID : ss4746
#Date : 10-15-2023
# UCID:ss4746
# Date: 15-10-2023
# This method involves three test cases, where a series of data is passed as input. 
# In the first test case, we provide values, and the result of this test case is used as input for the subsequent series of tests. 
# In the second test, we pass a number and compare it with the previously passed value. 
# A loop iterates through all three test cases by invoking the "multiplication" method and returns whether each case has passed or failed.

def test_ans_div_number():
    calc = MyCalc()
    data = [{"a": "500","b": "5","r": "100"},{"a": "ans","b": "4","r": "25"},{"a": "ans","b": "1","r": "25"}, ]
    for d in data:
        assert calc.div(d["a"], d["b"]) == int(d["r"])
#UCID : ss4746
#Date : 10-15-2023
# UCID:ss4746
# Date: 15-10-2023
# This method involves three test cases, where a series of data is passed as input. 
# In the first test case, we provide values, and the result of this test case is used as input for the subsequent series of tests. 
# In the second test, we pass a number and compare it with the previously passed value. 
# A loop iterates through all three test cases by invoking the "division" method and returns whether each case has passed or failed.
if __name__ == "__main__":
    pytest.main()

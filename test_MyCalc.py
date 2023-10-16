from MyCalc import MyCalc

import pytest


def test_number_add_number():
    calc = MyCalc()
    assert calc.addition(5, 6) == 11
    assert calc.addition(10, 5) == 15
    assert calc.addition(5, 15) == 20


# UCID:bs643
# Date: 15-10-2023
# This method contains a test case , MyCalc is assigned to calc
# we are passing two values to addition method and comparing to the given number
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.


def test_ans_add_number():
    calc = MyCalc()
    data = [{
        "a": "5",
        "b": "5",
        "r": "10"
    },
        {
            "a": "ans",
            "b": "4",
            "r": "14"
        },
        {
            "a": "ans",
            "b": "1",
            "r": "15"
        }, ]
    for d in data:
        assert calc.addition(d["a"], d["b"]) == int(d["r"])


# UCID:bs643
# Date: 15-10-2023
# This method contains three test cases
# series of data is passing ,in first test we pass values and result of first test case is passed as input to other series and
# second number we are passing and comparing with r passing value
# for loop checks all the three test cases by calling method addition and returns pass or failure cases


def test_number_sub_number():
    calc = MyCalc()
    assert calc.subtraction(10, 5) == 5
    assert calc.subtraction(100, 5) == 95
    assert calc.subtraction(100, 15) == 85


# UCID:bs643
# Date: 15-10-2023
# This method contains three test case , MyCalc is assigned to calc
# we are passing two values to subtraction method and comparing to the given number
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.


def test_ans_sub_number():
    calc = MyCalc()
    data = [{
        "a": "10",
        "b": "2",
        "r": "8"
    },
        {
            "a": "ans",
            "b": "4",
            "r": "4"
        },
        {
            "a": "ans",
            "b": "1",
            "r": "3"
        }, ]
    for d in data:
        assert calc.subtraction(d["a"], d["b"]) == int(d["r"])


# UCID:bs643
# Date: 15-10-2023
# This method contains three test cases
# series of data is passing ,in first test we pass values and result of first test case is passed as input to other series and
# second number we are passing and comparing with r passing value
# for loop checks all the three test cases by calling method subtraction and returns pass or failure cases


def test_number_mult_number():
    calc = MyCalc()
    assert calc.multiplication(5, 2) == 10
    assert calc.multiplication(10, 2) == 20
    assert calc.multiplication(15, 2) == 30


# UCID:bs643
# Date: 15-10-2023
# This method contains a test case , MyCalc is assigned to calc
# we are passing two values to multiplication method and comparing to the given number
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.


def test_ans_mult_number():
    calc = MyCalc()
    data = [{
        "a": "20",
        "b": "2",
        "r": "40"
    },
        {
            "a": "ans",
            "b": "4",
            "r": "160"
        },
        {
            "a": "ans",
            "b": "2",
            "r": "320"
        }, ]
    for d in data:
        assert calc.multiplication(d["a"], d["b"]) == int(d["r"])


# UCID:bs643
# Date: 15-10-2023
# This method contains three test cases
# series of data is passing ,in first test we pass values and result of first test case is passed as input to other series and
# second number we are passing and comparing with r passing value
# for loop checks all the three test cases by calling method multiplication and returns pass or failure cases


def test_number_div_number():
    calc = MyCalc()
    assert calc.division(20, 2) == 10
    assert calc.division(15, 2) == 7.5
    assert calc.division(100, 4) == 25


# UCID:bs643
# Date: 15-10-2023
# This method contains three test case , MyCalc is assigned to calc
# we are passing two values to divison method and comparing to the given number
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.


def test_ans_div_number():
    calc = MyCalc()
    data = [{
        "a": "20",
        "b": "2",
        "r": "10"
    },
        {
            "a": "ans",
            "b": "2",
            "r": "5"
        },
        {
            "a": "ans",
            "b": "3",
            "r": "1.6666666666666667"
        }, ]
    for d in data:
        assert calc.division(d["a"], d["b"]) == float(d["r"])
# UCID:bs643
# Date: 15-10-2023
# This method contains three test cases
# series of data is passing ,in first test we pass values and result of first test case is passed as input to other series and
# second number we are passing and comparing with r passing value
# for loop checks all the three test cases by calling method division and returns pass or failure cases



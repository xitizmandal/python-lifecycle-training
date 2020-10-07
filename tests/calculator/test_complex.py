import pytest

import python_lifecycle_training
from python_lifecycle_training.calculator.complex import Calculator


class TestCalculator:
    @staticmethod
    def test_add():
        assert Calculator.add(1, 2) == 3

    @staticmethod
    def test_sub():
        assert Calculator.sub(2, 1) == 1

    @staticmethod
    def test_mul():
        assert Calculator.mul(1, 2) == 2

    @staticmethod
    @pytest.mark.parametrize(
        "a, b",
        [
            (2, 1),
            (2, 0),
        ],
    )
    def test_div(a, b):
        if b != 0:
            assert Calculator.div(a, b) == pytest.approx(a / b)
        else:
            python_lifecycle_training.ENV = "development"
            with pytest.raises(ZeroDivisionError) as excinfo:
                assert Calculator.div(a, b) is None
            assert str(excinfo.value) == "division by zero"

            python_lifecycle_training.ENV = "production"
            with pytest.warns(RuntimeWarning) as record:
                assert Calculator.div(a, b) == 0
            assert str(record[0].message) == "division by zero"

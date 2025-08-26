import calculator_logic as c
import pytest

def test_add():
    assert c.add(1, 2) == 3
    assert c.add(-1, 1) == 0
    assert c.add(-2, -4) == -6
    assert c.add(0, 0) == 0

    with pytest.raises(TypeError):
        c.add(1, "r")

    with pytest.raises(TypeError):
        c.add('ss', 2)

    with pytest.raises(TypeError):
        c.add('ss', '2')


def test_subtruct():
    assert c.subtruct(1, 2) == -1
    assert c.subtruct(-1, 1) == -2
    assert c.subtruct(-2, -4) == 2
    assert c.subtruct(0, 0) == 0

    with pytest.raises(TypeError):
        c.subtruct(1, "r")

    with pytest.raises(TypeError):
        c.subtruct('ss', 2)

    with pytest.raises(TypeError):
        c.subtruct('ss', '2')


def test_multiply():
    assert c.multiply(1, 2) == 2
    assert c.multiply(-1, 1) == -1
    assert c.multiply(-2, -4) == 8
    assert c.multiply(0, 0) == 0

    with pytest.raises(TypeError):
        c.multiply(1, "r")

    with pytest.raises(TypeError):
        c.multiply('ss', 2)

    with pytest.raises(TypeError):
        c.multiply('ss', '2')

def test_divide():
    assert c.divide(10, 2) == 5
    assert c.divide(-1, 1) == -1
    assert c.divide(-2, -4) == 0.5

    with pytest.raises(TypeError):
        c.divide(1, "r")

    with pytest.raises(TypeError):
        c.divide('ss', 2)

    with pytest.raises(TypeError):
        c.divide('ss', '2')

    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)


test_add()
print('Тесты на сложение пройдены успешно')

test_subtruct()
print('Тесты на вычитание пройдены успешно')

test_multiply()
print('Тесты на умножение пройдены успешно')

test_divide()
print('Тесты на деление пройдены успешно')
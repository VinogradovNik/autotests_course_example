# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a, b, result', [
    pytest.param(10, 5, 2, marks=pytest.mark.smoke),
    (20, -2, -10),
    (3, 0, pytest.raises(ZeroDivisionError)),
    pytest.param(-5, -1, 5, marks=pytest.mark.skip('skip test')),
    (1, 5, 0.2)
])
def test_check_division(a, b, result):
    assert all_division(a, b) == result


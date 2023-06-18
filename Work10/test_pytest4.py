# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.mark.usefixtures('time_class')
class TestMy:

    @pytest.mark.usefixtures('time_test')
    def test1(self):
        time.sleep(2)

    def test2(self):
        time.sleep(1)

    def test3(self):
        time.sleep(3)



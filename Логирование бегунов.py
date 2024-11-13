import logging
import unittest
from rt_with_exceptions import *


logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename='runner_tests.log',
                    encoding='utf-8',
                    format='%(levelname)s: %(message(s)')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Усэйн', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = Runner(123, 5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для Runner')


if __name__ == '__main__':
    unittest.main()
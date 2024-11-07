import unittest
import logging
from runner import Runner  # Импортируем класс Runner из файла runner.py

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


class RunnerTest(unittest.TestCase):

    def setUp(self):
        # Создаем объект Runner для тестов
        self.runner = Runner(name="Test Runner", speed=5)

    def test_walk(self):
        try:
            # Передаем отрицательное значение для speed
            self.runner = Runner(name="Test Runner", speed=-1)
            self.runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            # Передаем неправильный тип для name
            self.runner = Runner(name=123, speed=5)
            self.runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()

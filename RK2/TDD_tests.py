import unittest
from main import *

class TestJoinOperations(unittest.TestCase):
    def test_join_one_to_many(self):
        result = join_one_to_many(languages, libraries)
        self.assertTrue(len(result) > 0)  # Проверка, что результат не пустой

    def test_join_many_to_many(self):
        result = join_many_to_many(languages, language_library, libraries)
        self.assertTrue(len(result) > 0)  # Проверка, что результат не пустой

class TestTaskResults(unittest.TestCase):
    def test_get_a1_result(self):
        data = [("NumPy", 100, "Python"), ("Angular", 200, "JavaScript"), ("React", 300, "JavaScript")]
        result = get_a1_result(data)
        self.assertEqual(result, [("Angular", "JavaScript")])  # Проверка корректности результата

    def test_get_a1_empty_result(self):
        data = []  # пустой список
        result = get_a1_result(data)
        self.assertEqual(result, [])  # ожидаемый результат - пустой список

    def test_get_a2_result(self):
        data = [("NumPy", 100, "Python"), ("Angular", 200, "JavaScript"), ("React", 300, "JavaScript"),("Pandas", 1024, "Python")]
        result = get_a2_result(data)
        self.assertEqual(result, [("Python", 100), ("JavaScript", 200)])  # Проверка корректности результата

    def test_get_a3_result(self):
        data = [
            ("Library A", 100, "Language 1"),
            ("Library B", 200, "Language 2"),
            ("Library C", 150, "Language 1")
        ]
        result = sorted(data, key=itemgetter(0))  # ожидаемый результат - отсортированный по имени библиотеки
        self.assertEqual(result, get_a3_result(data))

if __name__ == '__main__':
    unittest.main()
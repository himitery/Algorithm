import json
import os
import unittest

from parameterized import parameterized

from .main import solution


def load_sample(filename: str):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    with open(path, "r") as file:
        return [(case["params"], case["expected"]) for case in json.load(file)]


class TestCase(unittest.TestCase):
    @parameterized.expand(load_sample("sample.json"))
    def test_case(self, params: list, expected: any):
        # When
        result = solution(*params)

        # Then
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()

import json
import os.path
import unittest
from io import StringIO
from unittest.mock import patch

from parameterized import parameterized

from .main import Problem


def load_sample(filename: str):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    with open(path, "r") as file:
        return [(case["input"], case["expected"]) for case in json.load(file)]


class MyTestCase(unittest.TestCase):
    @parameterized.expand(load_sample("sample.json"))
    def test_case(self, case: str, expected: list[str]):
        # When
        with (
            patch("sys.stdin.readline", side_effect=case),
            patch("sys.stdout", new_callable=StringIO) as output,
        ):
            Problem().solve()

            result = output.getvalue().strip()

        # Then
        self.assertEqual(result, "\n".join(expected))


if __name__ == "__main__":
    unittest.main()

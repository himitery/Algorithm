import json
import os.path
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from parameterized import parameterized

from main import Problem


def load_sample(filename: str):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    with open(path, "r") as file:
        return [(case["input"], case["expected"]) for case in json.load(file)]


class TestCase(unittest.TestCase):
    @parameterized.expand(load_sample("sample.json"))
    def test_case(self, case: str, expected: list[str]):
        # When
        with (
            patch("sys.stdin.readline", side_effect=case),
            patch("sys.stdout", new_callable=StringIO) as output,
        ):
            for _ in range(int(sys.stdin.readline().rstrip())):
                Problem().solve()

            result = output.getvalue().rstrip()

        # Then
        self.assertEqual("\n".join(expected), result)


if __name__ == "__main__":
    unittest.main()

import unittest
from io import StringIO
from unittest.mock import patch

from parameterized import parameterized

from .main import Problem


class MyTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (
                [
                    "2",
                    "3",
                    "hat headgear",
                    "sunglasses eyewear",
                    "turban headgear",
                    "3",
                    "mask face",
                    "sunglasses face",
                    "makeup face",
                ],
                ["5", "3"],
            ),
        ],
    )
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

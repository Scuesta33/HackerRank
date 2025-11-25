import unittest
from io import StringIO
import sys
from string_formatting import print_formatted

class TestPrintFormatted(unittest.TestCase):


    def test_print_formatted_1(self):
        captuare_output = StringIO()
        sys.stdout = captuare_output

        print_formatted(1)

        sys.stdout = sys.__stdout__

        expected = "1 1 1 1\n"
        self.assertEqual(captuare_output.getvalue(), expected)

    def test_print_formatted_5(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_formatted(5)

        sys.stdout = sys.__stdout__

        expected = (
        "  1   1   1   1\n"
        "  2   2   2  10\n"
        "  3   3   3  11\n"
        "  4   4   4 100\n"
        "  5   5   5 101\n"
        )

        self.assertEqual(captured_output.getvalue(), expected)

        if __name__ == '__main__':
            unittest.main()



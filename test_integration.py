import unittest
import subprocess

class TestIntegration(unittest.TestCase):

    def customRun(self, input_data, target):
        process = subprocess.Popen(
            ["python", "main.py", input_data, target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8"
        )
        stdout, _ = process.communicate()

        self.assertEqual(process.returncode, 0)
        return stdout.strip()
    
    def test_integration_no_pairs(self):
        input_data = "1,2,3,4"
        target = "10"

        expected_output = """\
Result: []"""

        out = self.customRun(input_data, target)
        self.assertEqual(out, expected_output)

    def test_integration_single_pair(self):
        input_data = "1,2,3,4,5"
        target = "7"

        expected_output = """\
Result: [[3, 4], [2, 5]]
0. 3 + 4 = 7
1. 2 + 5 = 7"""

        out = self.customRun(input_data, target)
        self.assertEqual(out, expected_output)

    def test_integration_multiple_pairs(self):
        input_data = "1,2,3,4,5,6,7"
        target = "7"

        expected_output = """\
Result: [[3, 4], [2, 5], [1, 6]]
0. 3 + 4 = 7
1. 2 + 5 = 7
2. 1 + 6 = 7"""

        out = self.customRun(input_data, target)
        self.assertEqual(out, expected_output)

if __name__ == '__main__':
    unittest.main()

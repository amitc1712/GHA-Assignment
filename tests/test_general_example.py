import unittest
from unittest.mock import patch
from general_example import GeneralExample

general_example_instance = GeneralExample()


class TestEmployeeRecordLoading(unittest.TestCase):
    """
    Test class for employee records loading
    """

    def test_flatten_dictionary(self):
        """
        Test flatten dictionary method.
        """
        dictValues = {"key1": [3, 2, 1], "key2": [42, 55, 10], "key3": [0, 22]}
        expected = [0, 1, 2, 3, 10, 22, 42, 55]

        actual = general_example_instance.flatten_dictionary(dictValues)

        assert expected == actual

    @patch("general_example.GeneralExample.load_employee_rec_from_database")
    def test_fetch_emp_details(self, mock_load_employee_rec):
        """
        Test fetch employee details method.
        """
        mock_load_employee_rec.return_value = ["emp001", "Sam", "100000"]

        emp_details = general_example_instance.fetch_emp_details()

        expected_emp_details = {
            "empId": "emp001",
            "empName": "Sam",
            "empSalary": "100000",
        }
        self.assertEqual(emp_details, expected_emp_details)


if __name__ == "__main__":
    unittest.main()

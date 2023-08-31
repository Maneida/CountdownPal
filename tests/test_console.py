#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

from console import CPCommand
from unittest.mock import patch
import console
import inspect
import pep8
import unittest


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    '''def test_pep8_conformance_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")'''

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the CPCommand class docstring"""
        self.assertIsNot(CPCommand.__doc__, None,
                         "CPCommand class needs a docstring")
        self.assertTrue(len(CPCommand.__doc__) >= 1,
                        "CPCommand class needs a docstring")


class TestCPCommand(unittest.TestCase):
    """Test suite for CPCommand class"""

    def setUp(self):
        """Set up the test environment"""
        self.cmd = CPCommand()

    def test_do_EOF(self):
        """Test if do_EOF method correctly returns True"""
        self.assertTrue(self.cmd.do_EOF(None))

    def test_emptyline(self):
        """Test if emptyline method correctly returns False"""
        self.assertFalse(self.cmd.emptyline())

    def test_do_quit(self):
        """Test if do_quit method correctly returns True"""
        self.assertTrue(self.cmd.do_quit(None))

    @patch('builtins.print')
    def test_do_test(self, mock_print):
        """Test if do_test method prints the expected message"""
        self.cmd.do_test(None)
        mock_print.assert_called_with("Console working without issue.")

    def test_key_value_parser(self):
        """Test key_value_parser method for parsing arguments"""
        args = ["key1=value1", "key2=42", "key3=3.14", "key4=\"quoted value\""]
        result = self.cmd._key_value_parser(args)
        self.assertEqual(result, {
            "key1": "value1",
            "key2": 42,
            "key3": 3.14,
            "key4": "quoted value"
        })

    def test_do_create_missing_class(self):
        """Test if do_create method handles missing class name"""
        with patch('builtins.print') as mock_print:
            self.cmd.do_create("")
            mock_print.assert_called_with("** class name missing")

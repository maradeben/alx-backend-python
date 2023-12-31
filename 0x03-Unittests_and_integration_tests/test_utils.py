#!/usr/bin/env python3
""" test module for the utils module """
import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """ tests for access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str], output: int) -> None:
        """ test case """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """ test case with KeyError """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ tests for get_json method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_reqget: str) -> None:
        """ basic test """
        mocked = mock.Mock(return_value=test_payload)
        mocked.json.return_value = test_payload
        mock_reqget.return_value = mocked
        self.assertEqual(get_json(test_url), test_payload)
        mock_reqget.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ tests for memoize """

    def test_memoize(self):
        """ basic test """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mocked:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mocked.assert_called_once()

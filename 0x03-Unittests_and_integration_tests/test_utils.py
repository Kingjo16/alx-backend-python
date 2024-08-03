#!/usr/bin/env python3
"""Module That will test the utils of the module."""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Function that will test the access_nested_map."""
    @parameterized.expand([
        ({"key1": 1}, ("key1",), 1),
        ({"key1": {"key2": 2}}, ("key1",), {"key2": 2}),
        ({"key1": {"key2": 2}}, ("key1", "key2"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_dict: Dict,
            keys: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests the output of `access_nested_map`."""
        self.assertEqual(access_nested_map(nested_dict, keys), expected)

    @parameterized.expand([
        ({}, ("key1",), KeyError),
        ({"key1": 1}, ("key1", "key2"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_dict: Dict,
            keys: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests the exception raising of `access_nested_map`."""
        with self.assertRaises(exception):
            access_nested_map(nested_dict, keys)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"data": True}),
        ("http://holberton.io", {"data": False}),
    ])
    def test_get_json(
            self,
            url: str,
            expected_payload: Dict,
            ) -> None:
        """Tests the output of `get_json`."""
        attrs = {'json.return_value': expected_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as mock_get:
            self.assertEqual(get_json(url), expected_payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests the output of `memoize`."""
        class SampleClass:
            def sample_method(self):
                return 42

            @memoize
            def sample_property(self):
                return self.sample_method()
        with patch.object(
                SampleClass,
                "sample_method",
                return_value=lambda: 42,
                ) as mock_method:
            sample_instance = SampleClass()
            self.assertEqual(sample_instance.sample_property(), 42)
            self.assertEqual(sample_instance.sample_property(), 42)
            mock_method.assert_called_once()

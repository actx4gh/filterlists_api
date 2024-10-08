# coding: utf-8

"""
    FilterLists Directory API

    An ASP.NET Core API serving the core FilterList information.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from filterlists_api.api.maintainers_api import MaintainersApi


class TestMaintainersApi(unittest.TestCase):
    """MaintainersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MaintainersApi()

    def tearDown(self) -> None:
        pass

    def test_get_maintainers(self) -> None:
        """Test case for get_maintainers

        Gets the maintainers of the FilterLists.
        """
        pass


if __name__ == '__main__':
    unittest.main()

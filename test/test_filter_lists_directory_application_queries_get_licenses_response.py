# coding: utf-8

"""
    FilterLists Directory API

    An ASP.NET Core API serving the core FilterList information.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from filterlists_api.models.filter_lists_directory_application_queries_get_licenses_response import FilterListsDirectoryApplicationQueriesGetLicensesResponse

class TestFilterListsDirectoryApplicationQueriesGetLicensesResponse(unittest.TestCase):
    """FilterListsDirectoryApplicationQueriesGetLicensesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilterListsDirectoryApplicationQueriesGetLicensesResponse:
        """Test FilterListsDirectoryApplicationQueriesGetLicensesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilterListsDirectoryApplicationQueriesGetLicensesResponse`
        """
        model = FilterListsDirectoryApplicationQueriesGetLicensesResponse()
        if include_optional:
            return FilterListsDirectoryApplicationQueriesGetLicensesResponse(
                id = 5,
                name = 'All Rights Reserved',
                url = 'https://en.wikipedia.org/wiki/All_rights_reserved',
                permits_modification = False,
                permits_distribution = False,
                permits_commercial_use = False,
                filter_list_ids = [6,31]
            )
        else:
            return FilterListsDirectoryApplicationQueriesGetLicensesResponse(
        )
        """

    def testFilterListsDirectoryApplicationQueriesGetLicensesResponse(self):
        """Test FilterListsDirectoryApplicationQueriesGetLicensesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

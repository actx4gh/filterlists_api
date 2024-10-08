# coding: utf-8

"""
    FilterLists Directory API

    An ASP.NET Core API serving the core FilterList information.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from filterlists_api.models.filter_lists_directory_application_queries_get_software_response import FilterListsDirectoryApplicationQueriesGetSoftwareResponse

class TestFilterListsDirectoryApplicationQueriesGetSoftwareResponse(unittest.TestCase):
    """FilterListsDirectoryApplicationQueriesGetSoftwareResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilterListsDirectoryApplicationQueriesGetSoftwareResponse:
        """Test FilterListsDirectoryApplicationQueriesGetSoftwareResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilterListsDirectoryApplicationQueriesGetSoftwareResponse`
        """
        model = FilterListsDirectoryApplicationQueriesGetSoftwareResponse()
        if include_optional:
            return FilterListsDirectoryApplicationQueriesGetSoftwareResponse(
                id = 2,
                name = 'Adblock Plus',
                description = 'Adblock Plus is a free extension that allows you to customize your web experience...',
                home_url = 'https://adblockplus.org/',
                download_url = 'https://adblockplus.org/',
                supports_abp_url_scheme = True,
                syntax_ids = [3,28,38,48]
            )
        else:
            return FilterListsDirectoryApplicationQueriesGetSoftwareResponse(
        )
        """

    def testFilterListsDirectoryApplicationQueriesGetSoftwareResponse(self):
        """Test FilterListsDirectoryApplicationQueriesGetSoftwareResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

# filterlists_api.LicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_licenses**](LicensesApi.md#get_licenses) | **GET** /licenses | Gets the licenses applied to the FilterLists.


# **get_licenses**
> List[FilterListsDirectoryApplicationQueriesGetLicensesResponse] get_licenses()

Gets the licenses applied to the FilterLists.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_licenses_response import FilterListsDirectoryApplicationQueriesGetLicensesResponse
from filterlists_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = filterlists_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with filterlists_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = filterlists_api.LicensesApi(api_client)

    try:
        # Gets the licenses applied to the FilterLists.
        api_response = api_instance.get_licenses()
        print("The response of LicensesApi->get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicensesApi->get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilterListsDirectoryApplicationQueriesGetLicensesResponse]**](FilterListsDirectoryApplicationQueriesGetLicensesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


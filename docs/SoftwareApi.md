# filterlists_api.SoftwareApi

All URIs are relative to *https://api.filterlists.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_software**](SoftwareApi.md#get_software) | **GET** /software | Gets the software that subscribes to the FilterLists.


# **get_software**
> List[FilterListsDirectoryApplicationQueriesGetSoftwareResponse] get_software()

Gets the software that subscribes to the FilterLists.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_software_response import FilterListsDirectoryApplicationQueriesGetSoftwareResponse
from filterlists_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.filterlists.com
# See configuration.py for a list of all supported configuration parameters.
configuration = filterlists_api.Configuration(
    host = "https://api.filterlists.com"
)


# Enter a context with an instance of the API client
with filterlists_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = filterlists_api.SoftwareApi(api_client)

    try:
        # Gets the software that subscribes to the FilterLists.
        api_response = api_instance.get_software()
        print("The response of SoftwareApi->get_software:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->get_software: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilterListsDirectoryApplicationQueriesGetSoftwareResponse]**](FilterListsDirectoryApplicationQueriesGetSoftwareResponse.md)

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


# filterlists_api.SyntaxesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_syntaxes**](SyntaxesApi.md#get_syntaxes) | **GET** /syntaxes | Gets the syntaxes of the FilterLists.


# **get_syntaxes**
> List[FilterListsDirectoryApplicationQueriesGetSyntaxesResponse] get_syntaxes()

Gets the syntaxes of the FilterLists.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_syntaxes_response import FilterListsDirectoryApplicationQueriesGetSyntaxesResponse
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
    api_instance = filterlists_api.SyntaxesApi(api_client)

    try:
        # Gets the syntaxes of the FilterLists.
        api_response = api_instance.get_syntaxes()
        print("The response of SyntaxesApi->get_syntaxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyntaxesApi->get_syntaxes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilterListsDirectoryApplicationQueriesGetSyntaxesResponse]**](FilterListsDirectoryApplicationQueriesGetSyntaxesResponse.md)

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


# filterlists_api.LanguagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_languages**](LanguagesApi.md#get_languages) | **GET** /languages | Gets the languages targeted by the FilterLists.


# **get_languages**
> List[FilterListsDirectoryApplicationQueriesGetLanguagesResponse] get_languages()

Gets the languages targeted by the FilterLists.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_languages_response import FilterListsDirectoryApplicationQueriesGetLanguagesResponse
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
    api_instance = filterlists_api.LanguagesApi(api_client)

    try:
        # Gets the languages targeted by the FilterLists.
        api_response = api_instance.get_languages()
        print("The response of LanguagesApi->get_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LanguagesApi->get_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilterListsDirectoryApplicationQueriesGetLanguagesResponse]**](FilterListsDirectoryApplicationQueriesGetLanguagesResponse.md)

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


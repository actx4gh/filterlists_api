# filterlists_api.TagsApi

All URIs are relative to *https://api.filterlists.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | Gets the tags of the FilterLists.


# **get_tags**
> List[FilterListsDirectoryApplicationQueriesGetTagsResponse] get_tags()

Gets the tags of the FilterLists.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_tags_response import FilterListsDirectoryApplicationQueriesGetTagsResponse
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
    api_instance = filterlists_api.TagsApi(api_client)

    try:
        # Gets the tags of the FilterLists.
        api_response = api_instance.get_tags()
        print("The response of TagsApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilterListsDirectoryApplicationQueriesGetTagsResponse]**](FilterListsDirectoryApplicationQueriesGetTagsResponse.md)

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


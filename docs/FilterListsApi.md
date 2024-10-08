# filterlists_api.FilterListsApi

All URIs are relative to *https://api.filterlists.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_details**](FilterListsApi.md#get_list_details) | **GET** /lists/{id} | Gets the details of the FilterList.
[**get_lists**](FilterListsApi.md#get_lists) | **GET** /lists | Gets the FilterLists.


# **get_list_details**
> FilterListsDirectoryApplicationQueriesGetListDetailsResponse get_list_details(id)

Gets the details of the FilterList.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_list_details_response import FilterListsDirectoryApplicationQueriesGetListDetailsResponse
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
    api_instance = filterlists_api.FilterListsApi(api_client)
    id = 1 # int | The identifier of the FilterList.

    try:
        # Gets the details of the FilterList.
        api_response = api_instance.get_list_details(id)
        print("The response of FilterListsApi->get_list_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterListsApi->get_list_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the FilterList. | 

### Return type

[**FilterListsDirectoryApplicationQueriesGetListDetailsResponse**](FilterListsDirectoryApplicationQueriesGetListDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> List[FilterListsDirectoryApplicationQueriesGetListsResponse] get_lists()

Gets the FilterLists.

### Example


```python
import filterlists_api
from filterlists_api.models.filter_lists_directory_application_queries_get_lists_response import FilterListsDirectoryApplicationQueriesGetListsResponse
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
    api_instance = filterlists_api.FilterListsApi(api_client)

    try:
        # Gets the FilterLists.
        api_response = api_instance.get_lists()
        print("The response of FilterListsApi->get_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilterListsApi->get_lists: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FilterListsDirectoryApplicationQueriesGetListsResponse]**](FilterListsDirectoryApplicationQueriesGetListsResponse.md)

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


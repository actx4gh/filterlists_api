# FilterListsDirectoryApplicationQueriesGetMaintainersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name. | [optional] 
**url** | **str** | The URL of the home page. | [optional] 
**email_address** | **str** | The email address. | [optional] 
**twitter_handle** | **str** | The Twitter handle. | [optional] 
**filter_list_ids** | **List[int]** | The identifiers of the FilterLists maintained by this Maintainer. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_maintainers_response import FilterListsDirectoryApplicationQueriesGetMaintainersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetMaintainersResponse from a JSON string
filter_lists_directory_application_queries_get_maintainers_response_instance = FilterListsDirectoryApplicationQueriesGetMaintainersResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetMaintainersResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_maintainers_response_dict = filter_lists_directory_application_queries_get_maintainers_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetMaintainersResponse from a dict
filter_lists_directory_application_queries_get_maintainers_response_from_dict = FilterListsDirectoryApplicationQueriesGetMaintainersResponse.from_dict(filter_lists_directory_application_queries_get_maintainers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



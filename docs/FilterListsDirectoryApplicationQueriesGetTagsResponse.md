# FilterListsDirectoryApplicationQueriesGetTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name. | [optional] 
**description** | **str** | The description. | [optional] 
**filter_list_ids** | **List[int]** | The identifiers of the FilterLists to which this Tag is applied. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_tags_response import FilterListsDirectoryApplicationQueriesGetTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetTagsResponse from a JSON string
filter_lists_directory_application_queries_get_tags_response_instance = FilterListsDirectoryApplicationQueriesGetTagsResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetTagsResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_tags_response_dict = filter_lists_directory_application_queries_get_tags_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetTagsResponse from a dict
filter_lists_directory_application_queries_get_tags_response_from_dict = FilterListsDirectoryApplicationQueriesGetTagsResponse.from_dict(filter_lists_directory_application_queries_get_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



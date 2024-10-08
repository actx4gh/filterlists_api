# FilterListsDirectoryApplicationQueriesGetSyntaxesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name. | [optional] 
**description** | **str** | The description. | [optional] 
**url** | **str** | The URL of the home page. | [optional] 
**filter_list_ids** | **List[int]** | The identifiers of the FilterLists implementing this Syntax. | [optional] 
**software_ids** | **List[int]** | The identifiers of the Software that supports this Syntax. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_syntaxes_response import FilterListsDirectoryApplicationQueriesGetSyntaxesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetSyntaxesResponse from a JSON string
filter_lists_directory_application_queries_get_syntaxes_response_instance = FilterListsDirectoryApplicationQueriesGetSyntaxesResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetSyntaxesResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_syntaxes_response_dict = filter_lists_directory_application_queries_get_syntaxes_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetSyntaxesResponse from a dict
filter_lists_directory_application_queries_get_syntaxes_response_from_dict = FilterListsDirectoryApplicationQueriesGetSyntaxesResponse.from_dict(filter_lists_directory_application_queries_get_syntaxes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



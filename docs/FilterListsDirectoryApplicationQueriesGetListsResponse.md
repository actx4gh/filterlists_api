# FilterListsDirectoryApplicationQueriesGetListsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name in title case. | [optional] 
**description** | **str** | The brief description in English (preferably quoted from the project). | [optional] 
**license_id** | **int** | The identifier of the License under which this FilterList is released. | [optional] 
**syntax_ids** | **List[int]** | The identifiers of the Syntaxes implemented by this FilterList. | [optional] 
**language_ids** | **List[int]** | The identifiers of the Languages targeted by this FilterList. | [optional] 
**tag_ids** | **List[int]** | The identifiers of the Tags applied to this FilterList. | [optional] 
**primary_view_url** | **str** | The primary view URL. | [optional] 
**maintainer_ids** | **List[int]** | The identifiers of the Maintainers of this FilterList. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_lists_response import FilterListsDirectoryApplicationQueriesGetListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetListsResponse from a JSON string
filter_lists_directory_application_queries_get_lists_response_instance = FilterListsDirectoryApplicationQueriesGetListsResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetListsResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_lists_response_dict = filter_lists_directory_application_queries_get_lists_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetListsResponse from a dict
filter_lists_directory_application_queries_get_lists_response_from_dict = FilterListsDirectoryApplicationQueriesGetListsResponse.from_dict(filter_lists_directory_application_queries_get_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FilterListsDirectoryApplicationQueriesGetLanguagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**iso6391** | **str** | The unique ISO 639-1 code. | [optional] 
**name** | **str** | The unique ISO name. | [optional] 
**filter_list_ids** | **List[int]** | The identifiers of the FilterLists targeted by this Language. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_languages_response import FilterListsDirectoryApplicationQueriesGetLanguagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetLanguagesResponse from a JSON string
filter_lists_directory_application_queries_get_languages_response_instance = FilterListsDirectoryApplicationQueriesGetLanguagesResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetLanguagesResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_languages_response_dict = filter_lists_directory_application_queries_get_languages_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetLanguagesResponse from a dict
filter_lists_directory_application_queries_get_languages_response_from_dict = FilterListsDirectoryApplicationQueriesGetLanguagesResponse.from_dict(filter_lists_directory_application_queries_get_languages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



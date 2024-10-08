# FilterListsDirectoryApplicationQueriesGetSoftwareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name. | [optional] 
**description** | **str** | The description. | [optional] 
**home_url** | **str** | The URL of the home page. | [optional] 
**download_url** | **str** | The URL of the Software download. | [optional] 
**supports_abp_url_scheme** | **bool** | If the Software supports the abp: URL scheme to click-to-subscribe to a FilterList. | [optional] 
**syntax_ids** | **List[int]** | The identifiers of the Syntaxes that this Software supports. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_software_response import FilterListsDirectoryApplicationQueriesGetSoftwareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetSoftwareResponse from a JSON string
filter_lists_directory_application_queries_get_software_response_instance = FilterListsDirectoryApplicationQueriesGetSoftwareResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetSoftwareResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_software_response_dict = filter_lists_directory_application_queries_get_software_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetSoftwareResponse from a dict
filter_lists_directory_application_queries_get_software_response_from_dict = FilterListsDirectoryApplicationQueriesGetSoftwareResponse.from_dict(filter_lists_directory_application_queries_get_software_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



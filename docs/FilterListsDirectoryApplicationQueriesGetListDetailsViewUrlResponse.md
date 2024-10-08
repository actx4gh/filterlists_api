# FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_number** | **int** | The segment number of the URL for the FilterList (for multi-part lists). | [optional] 
**primariness** | **int** | How primary the URL is for the FilterList segment (1 is original, 2+ is a mirror;  unique per SegmentNumber) | [optional] 
**url** | **str** | The view URL. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_list_details_view_url_response import FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse from a JSON string
filter_lists_directory_application_queries_get_list_details_view_url_response_instance = FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_list_details_view_url_response_dict = filter_lists_directory_application_queries_get_list_details_view_url_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse from a dict
filter_lists_directory_application_queries_get_list_details_view_url_response_from_dict = FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse.from_dict(filter_lists_directory_application_queries_get_list_details_view_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



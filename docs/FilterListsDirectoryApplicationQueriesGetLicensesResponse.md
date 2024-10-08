# FilterListsDirectoryApplicationQueriesGetLicensesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name. | [optional] 
**url** | **str** | The URL of the home page. | [optional] 
**permits_modification** | **bool** | If the License permits modification. | [optional] 
**permits_distribution** | **bool** | If the License permits distribution. | [optional] 
**permits_commercial_use** | **bool** | If the License permits commercial use. | [optional] 
**filter_list_ids** | **List[int]** | The identifiers of the FilterLists released under this License. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_licenses_response import FilterListsDirectoryApplicationQueriesGetLicensesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetLicensesResponse from a JSON string
filter_lists_directory_application_queries_get_licenses_response_instance = FilterListsDirectoryApplicationQueriesGetLicensesResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetLicensesResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_licenses_response_dict = filter_lists_directory_application_queries_get_licenses_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetLicensesResponse from a dict
filter_lists_directory_application_queries_get_licenses_response_from_dict = FilterListsDirectoryApplicationQueriesGetLicensesResponse.from_dict(filter_lists_directory_application_queries_get_licenses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



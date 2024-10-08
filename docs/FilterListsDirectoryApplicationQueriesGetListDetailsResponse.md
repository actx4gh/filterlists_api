# FilterListsDirectoryApplicationQueriesGetListDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier. | [optional] 
**name** | **str** | The unique name in title case. | 
**description** | **str** | The brief description in English (preferably quoted from the project). | [optional] 
**license_id** | **int** | The identifier of the License under which this FilterList is released. | [optional] 
**syntax_ids** | **List[int]** | The identifiers of the Syntaxes implemented by this FilterList. | [optional] 
**language_ids** | **List[int]** | The identifiers of the Languages targeted by this FilterList. | [optional] 
**tag_ids** | **List[int]** | The identifiers of the Tags applied to this FilterList. | [optional] 
**view_urls** | [**List[FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse]**](FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse.md) | The view URLs. | [optional] 
**home_url** | **str** | The URL of the home page. | [optional] 
**onion_url** | **str** | The URL of the Tor / Onion page. | [optional] 
**policy_url** | **str** | The URL of the policy/guidelines for the types of rules this FilterList includes. | [optional] 
**submission_url** | **str** | The URL of the submission/contact form for adding rules to this FilterList. | [optional] 
**issues_url** | **str** | The URL of the GitHub Issues page. | [optional] 
**forum_url** | **str** | The URL of the forum page. | [optional] 
**chat_url** | **str** | The URL of the chat room. | [optional] 
**email_address** | **str** | The email address at which the project can be contacted. | [optional] 
**donate_url** | **str** | The URL at which donations to the project can be made. | [optional] 
**maintainer_ids** | **List[int]** | The identifiers of the Maintainers of this FilterList. | [optional] 
**upstream_filter_list_ids** | **List[int]** | The identifiers of the FilterLists from which this FilterList was forked. | [optional] 
**fork_filter_list_ids** | **List[int]** | The identifiers of the FilterLists that have been forked from this FilterList. | [optional] 
**included_in_filter_list_ids** | **List[int]** | The identifiers of the FilterLists that include this FilterList. | [optional] 
**includes_filter_list_ids** | **List[int]** | The identifiers of the FilterLists that this FilterList includes. | [optional] 
**dependency_filter_list_ids** | **List[int]** | The identifiers of the FilterLists that this FilterList depends upon. | [optional] 
**dependent_filter_list_ids** | **List[int]** | The identifiers of the FilterLists dependent upon this FilterList. | [optional] 

## Example

```python
from filterlists_api.models.filter_lists_directory_application_queries_get_list_details_response import FilterListsDirectoryApplicationQueriesGetListDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterListsDirectoryApplicationQueriesGetListDetailsResponse from a JSON string
filter_lists_directory_application_queries_get_list_details_response_instance = FilterListsDirectoryApplicationQueriesGetListDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(FilterListsDirectoryApplicationQueriesGetListDetailsResponse.to_json())

# convert the object into a dict
filter_lists_directory_application_queries_get_list_details_response_dict = filter_lists_directory_application_queries_get_list_details_response_instance.to_dict()
# create an instance of FilterListsDirectoryApplicationQueriesGetListDetailsResponse from a dict
filter_lists_directory_application_queries_get_list_details_response_from_dict = FilterListsDirectoryApplicationQueriesGetListDetailsResponse.from_dict(filter_lists_directory_application_queries_get_list_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# filterlists-api
An ASP.NET Core API serving the core FilterList information.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.10
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import filterlists_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import filterlists_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import filterlists_api
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
    except ApiException as e:
        print("Exception when calling FilterListsApi->get_list_details: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.filterlists.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FilterListsApi* | [**get_list_details**](docs/FilterListsApi.md#get_list_details) | **GET** /lists/{id} | Gets the details of the FilterList.
*FilterListsApi* | [**get_lists**](docs/FilterListsApi.md#get_lists) | **GET** /lists | Gets the FilterLists.
*LanguagesApi* | [**get_languages**](docs/LanguagesApi.md#get_languages) | **GET** /languages | Gets the languages targeted by the FilterLists.
*LicensesApi* | [**get_licenses**](docs/LicensesApi.md#get_licenses) | **GET** /licenses | Gets the licenses applied to the FilterLists.
*MaintainersApi* | [**get_maintainers**](docs/MaintainersApi.md#get_maintainers) | **GET** /maintainers | Gets the maintainers of the FilterLists.
*SoftwareApi* | [**get_software**](docs/SoftwareApi.md#get_software) | **GET** /software | Gets the software that subscribes to the FilterLists.
*SyntaxesApi* | [**get_syntaxes**](docs/SyntaxesApi.md#get_syntaxes) | **GET** /syntaxes | Gets the syntaxes of the FilterLists.
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags | Gets the tags of the FilterLists.


## Documentation For Models

 - [FilterListsDirectoryApplicationQueriesGetLanguagesResponse](docs/FilterListsDirectoryApplicationQueriesGetLanguagesResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetLicensesResponse](docs/FilterListsDirectoryApplicationQueriesGetLicensesResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetListDetailsResponse](docs/FilterListsDirectoryApplicationQueriesGetListDetailsResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse](docs/FilterListsDirectoryApplicationQueriesGetListDetailsViewUrlResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetListsResponse](docs/FilterListsDirectoryApplicationQueriesGetListsResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetMaintainersResponse](docs/FilterListsDirectoryApplicationQueriesGetMaintainersResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetSoftwareResponse](docs/FilterListsDirectoryApplicationQueriesGetSoftwareResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetSyntaxesResponse](docs/FilterListsDirectoryApplicationQueriesGetSyntaxesResponse.md)
 - [FilterListsDirectoryApplicationQueriesGetTagsResponse](docs/FilterListsDirectoryApplicationQueriesGetTagsResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

b72d8917-851f-4864-ad5c-61630408048d@gb4emlsep.anonaddy.com



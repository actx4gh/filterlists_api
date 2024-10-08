# coding: utf-8

"""
    FilterLists Directory API

    An ASP.NET Core API serving the core FilterList information.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FilterListsDirectoryApplicationQueriesGetLicensesResponse(BaseModel):
    """
    FilterListsDirectoryApplicationQueriesGetLicensesResponse
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The identifier.")
    name: Optional[StrictStr] = Field(default=None, description="The unique name.")
    url: Optional[StrictStr] = Field(default=None, description="The URL of the home page.")
    permits_modification: Optional[StrictBool] = Field(default=None, description="If the License permits modification.", alias="permitsModification")
    permits_distribution: Optional[StrictBool] = Field(default=None, description="If the License permits distribution.", alias="permitsDistribution")
    permits_commercial_use: Optional[StrictBool] = Field(default=None, description="If the License permits commercial use.", alias="permitsCommercialUse")
    filter_list_ids: Optional[List[StrictInt]] = Field(default=None, description="The identifiers of the FilterLists released under this License.", alias="filterListIds")
    __properties: ClassVar[List[str]] = ["id", "name", "url", "permitsModification", "permitsDistribution", "permitsCommercialUse", "filterListIds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FilterListsDirectoryApplicationQueriesGetLicensesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if filter_list_ids (nullable) is None
        # and model_fields_set contains the field
        if self.filter_list_ids is None and "filter_list_ids" in self.model_fields_set:
            _dict['filterListIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FilterListsDirectoryApplicationQueriesGetLicensesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "permitsModification": obj.get("permitsModification"),
            "permitsDistribution": obj.get("permitsDistribution"),
            "permitsCommercialUse": obj.get("permitsCommercialUse"),
            "filterListIds": obj.get("filterListIds")
        })
        return _obj



from typing import List, Optional

from pydantic import AliasGenerator, BaseModel, ConfigDict, Field, AliasChoices
from pydantic.alias_generators import to_camel, to_snake


class ImportBase(BaseModel):

    year: int
    month: int
    origin_name: str
    origin_type_name: str
    destination_name: str
    destination_type_name: str
    grade_name: str
    quantity: int

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        )
    )


class ImportCreatePayload(ImportBase):
    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_camel,
        ),
    )


class ImportUpdatePayload(ImportBase):
    year: Optional[int]
    month: Optional[int]
    origin_name: Optional[str]
    origin_type_name: Optional[str]
    destination_name: Optional[str]
    destination_type_name: Optional[str]
    grade_name: Optional[str]
    quantity: Optional[int]

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_camel,
        ),
    )


class ImportCreateResponse(BaseModel):
    id: int


class ImportUpdateResponse(BaseModel):
    result: int


class ImportSchema(ImportBase):
    id: int
    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )


class ImportListResponse(BaseModel):
    results: List[ImportSchema]

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )

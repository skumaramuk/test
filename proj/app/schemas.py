from pydantic import BaseModel
from typing import Optional


class QueryTypes(BaseModel):
    name: Optional[str]
    alias: Optional[str]
    category: Optional[str]
    sub_category: Optional[str]
    id: Optional[str]
    type: Optional[str]
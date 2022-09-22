from enum import Enum, unique

from pydantic import BaseModel
from vaex.dataframe import DataFrame


class BaseLoggerInOutFrames(BaseModel):
    prob: DataFrame
    emb: DataFrame
    data: DataFrame

    class Config:
        arbitrary_types_allowed = True


@unique
class FileType(str, Enum):
    """Valid file extensions for an exported dataframe"""

    arrow = "arrow"
    parquet = "parquet"
    json = "json"
    csv = "csv"

from dataclasses import dataclass

import numpy as np
import pandas as pd

from aladdin.feature import FeatureType
from aladdin.redis.config import RedisConfig
from aladdin.request.retrival_request import RetrivalRequest
from aladdin.retrival_job import FactualRetrivalJob

try:
    import dask.dataframe as dd
except ModuleNotFoundError:
    import pandas as dd


@dataclass
class FactualRedisJob(FactualRetrivalJob):

    config: RedisConfig
    requests: list[RetrivalRequest]
    facts: dict[str, list]

    async def _to_df(self) -> pd.DataFrame:
        redis = self.config.redis()

        columns = set()
        for request in self.requests:
            columns.update(request.all_feature_names)

        result_df = pd.DataFrame(self.facts)

        for request in self.requests:
            # If using multiple entities, will this fail!
            # Need to sort on something in order to fix the bug
            entity_ids = result_df[sorted(request.entity_names)]
            mask = ~entity_ids.isna().any(axis=1)
            entities = request.feature_view_name + ':' + entity_ids.loc[mask].astype(str).sum(axis=1)
            for feature in request.all_features:
                keys = entities + ':' + feature.name

                # If there is no entities, set feature to None
                if entities.empty:
                    result_df[feature.name] = np.nan
                    continue

                result = await redis.mget(keys.values)
                result_series = pd.Series(result)
                set_mask = mask.copy()
                result_value_mask = result_series.notna()
                set_mask[mask] = set_mask[mask] & (result_value_mask)

                if feature.dtype == FeatureType('').datetime:
                    dates = pd.to_datetime(result_series[result_value_mask], unit='s', utc=True)
                    result_df.loc[set_mask, feature.name] = dates
                elif feature.dtype == FeatureType('').int32 or feature.dtype == FeatureType('').int64:
                    result_df.loc[set_mask, feature.name] = (
                        result_series[result_value_mask]
                        .str.split('.', n=1)
                        .str[0]
                        .astype(feature.dtype.pandas_type)
                    )
                else:
                    result_df.loc[set_mask, feature.name] = result_series[result_value_mask].astype(
                        feature.dtype.pandas_type
                    )

        return result_df

    async def to_df(self) -> pd.DataFrame:
        return await self._to_df()

    async def _to_dask(self) -> dd.DataFrame:
        return await self._to_df()

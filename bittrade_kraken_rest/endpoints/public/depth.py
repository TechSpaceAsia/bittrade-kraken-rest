from dataclasses import dataclass
from typing import List, Tuple
from reactivex import operators
from bittrade_kraken_rest.connection.observable import send_public
from bittrade_kraken_rest.connection.result import map_to_result


@dataclass
class GetDepthResult:
    asks: List[Tuple[str, str, int]]
    bids: List[Tuple[str, str, int]]


def get_depth(pair: str, count: int = 100):
    params = {"pair": pair, "count": count}
    return send_public(url="/0/public/Depth", params=params).pipe(
        operators.map(lambda resp: resp.json()),
        operators.map(lambda results: results["result"][pair.upper()]),
        operators.map(lambda depth: GetDepthResult(**depth)),
    )

__all__ = ["get_depth", "GetDepthResult"]

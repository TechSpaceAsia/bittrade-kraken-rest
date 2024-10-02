from bittrade_kraken_rest.endpoints.public.depth import get_depth


def test_get_depth():
    result = get_depth("btc/usd", 10).run()
    assert len(result.asks) == 10
    assert len(result.bids) == 10

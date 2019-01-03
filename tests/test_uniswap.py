import pytest
import time
import os

from uniswap.uniswap import UniswapWrapper


@pytest.fixture(scope="module")
def client():
    address = os.environ["ETH_ADDRESS"]
    priv_key = os.environ["ETH_PRIV_KEY"]
    # For testing, use Rinkeby
    provider = os.environ["TESTNET_PROVIDER"]
    return UniswapWrapper(address, priv_key, provider)


@pytest.mark.usefixtures("client")
class TestUniswap(object):

    ONE_ETH = 1*10**18

    # ------ Exchange ------------------------------------------------------------------
    def test_get_fee_maker(self, client):
        r = client.get_fee_maker()
        assert r == 0

    def test_get_fee_taker(self, client):
        r = client.get_fee_taker()
        assert r == 0.003

    # ------ Market --------------------------------------------------------------------
    @pytest.mark.parametrize("token, qty", [
        ("bat", ONE_ETH),
        ("dai", ONE_ETH),
        ("bat", 2 * ONE_ETH),
        pytest.param("btc", ONE_ETH,
                     marks=pytest.mark.xfail)
        ])
    def test_get_eth_token_input_price(self, client, token, qty):
        r = client.get_eth_token_input_price(token, qty)
        assert bool(r)

    @pytest.mark.parametrize("token, qty", [
        ("bat", ONE_ETH),
        ("dai", ONE_ETH),
        ("bat", 2 * ONE_ETH),
        pytest.param("btc", ONE_ETH,
                     marks=pytest.mark.xfail)
        ])
    def test_get_token_eth_input_price(self, client, token, qty):
        r = client.get_token_eth_input_price(token, qty)
        assert bool(r)

    @pytest.mark.parametrize("token, qty", [
        ("bat", ONE_ETH),
        ("dai", ONE_ETH),
        ("bat", 2 * ONE_ETH),
        pytest.param("btc", ONE_ETH,
                     marks=pytest.mark.xfail)
        ])
    def test_get_eth_token_output_price(self, client, token, qty):
        r = client.get_eth_token_output_price(token, qty)
        assert bool(r)

    @pytest.mark.parametrize("token, qty", [
        ("bat", ONE_ETH),
        ("dai", ONE_ETH),
        ("bat", 2 * ONE_ETH),
        pytest.param("btc", ONE_ETH,
                     marks=pytest.mark.xfail)
        ])
    def test_get_token_eth_output_price(self, client, token, qty):
        r = client.get_token_eth_output_price(token, qty)
        assert bool(r)

    # ------ ERC20 Pool ----------------------------------------------------------------
    @pytest.mark.parametrize("token", [
        ("bat"),
        ("dai")
        ])
    def test_get_eth_balance(self, client, token,):
        r = client.get_eth_balance(token)
        assert bool(r)

    @pytest.mark.parametrize("token", [
        ("bat"),
        ("dai")
        ])
    def test_get_token_balance(self, client, token,):
        r = client.get_token_balance(token)
        assert bool(r)

    @pytest.mark.parametrize("token", [
        ("bat"),
        ("dai")
        ])
    def get_exchange_rate(self, client, token,):
        r = client.get_exchange_rate(token)
        assert bool(r)

    # ------ Liquidity -----------------------------------------------------------------
    @pytest.mark.parametrize("token, max_eth", [
        ("bat", 0.005 * ONE_ETH),
        ("dai", 0.005 * ONE_ETH),
        ("bat", 0.001 * ONE_ETH),
        pytest.param("btc", ONE_ETH,
                     marks=pytest.mark.xfail)
        ])
    def test_add_liquidity(self, client, token, max_eth):
        r = client.add_liquidity(token, max_eth)
        assert bool(r)


    @pytest.mark.parametrize("token, max_token", [
        ("bat", 0.005 * ONE_ETH),
        ("dai", 0.005 * ONE_ETH),
        ("bat", 0.001 * ONE_ETH),
        pytest.param("btc", ONE_ETH,
                     marks=pytest.mark.xfail)
        ])
    def test_remove_liquidity(self, client, token, max_token):
        r = client.remove_liquidity(token, max_token)
        assert bool(r)

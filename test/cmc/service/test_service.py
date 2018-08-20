from cmc.service import CMCService


class TestCMCService:
    def test_cmc_service(self):
        srv = CMCService()
        t = srv.fetch_token('Bitcoin')
        assert t.name == 'Bitcoin'
        assert t.symbol == 'BTC'
        assert t.price_usd != -1
        assert t.price_btc == 1.0
        assert t.hchange != -1
        assert t.dchange != -1
        assert t.wchange != -1
        srv.kill_service()

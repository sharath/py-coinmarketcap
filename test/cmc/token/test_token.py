from cmc.token import Token


class TestToken:
    def test_token(self):
        t = Token('BTC', 'Bitcoin', 1000, 1.0, 1, 1, 1)
        assert str(t) == str(vars(t))

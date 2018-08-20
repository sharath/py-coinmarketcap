# py-coinmarketcap
[![Build Status](https://travis-ci.org/sharath/pycmc.svg?branch=master)](https://travis-ci.org/sharath/pycmc)

Installation: `pip install py-coinmarketcap`

#### Usage

As a service:
```python
from cmc.service import CMCService

# create service with update interval of 15 seconds
srv = CMCService(start=True, update_interval=15)

# automatically updates from cmc every 15 seconds
bitcoin_token = srv.fetch_token('Bitcoin')

print(vars(bitcoin_token))

# kill service
srv.kill_service()

```

Output
```bash
{'symbol': 'BTC', 'name': 'Bitcoin', 'price_usd': 6479.51734354, 'price_btc': 1.0, 'hchange': '0.06', 'dchange': '1.27', 'wchange': '2.40'}
```
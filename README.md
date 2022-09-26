## Plot the forecasts data from cryptowarp.io with the coins historical data from binance.

Requirements:
- Python
- Bokeh
- Pandas


It should produce a plot like this:

<p align="center"><img width="1000px" src="shots/shot1.png" alt="cryptowarp.io btc shot no.1"></p>
<p align="center"><img width="1000px" src="shots/shot2.png" alt="cryptowarp.io btc shot no.2"></p>
<p align="center"><img width="1000px" src="shots/shot3.png" alt="cryptowarp.io aave"></p>

### Usage

```bash
$ python plot_cryptowarp.py "BTCUSDT"
```

### Don't forget to change the API key

```python
api_key = "YOUR_API_KEY"
```

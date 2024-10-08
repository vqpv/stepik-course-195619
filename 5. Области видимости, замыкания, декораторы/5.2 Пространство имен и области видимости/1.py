exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}

def convert(c1, c2, count):
    return round((exchange_rates[c2] / exchange_rates[c1]) * count, 2)

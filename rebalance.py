def moneyify(value):
    return round(value, 2)

def percentify(a, b):
    return round(a / float(b), 2) * 100

def print_money(value):
    return '${}'.format(value) if value >= 0 else '-${}'.format(abs(value))


# TODO: have your portfolio here
# If you are adding tickers from your portfolio, put {'shares': 0}
# If you are removing tickers from your portfolio, put {'target': 0}
portfolio = {
    'a': {'price': 14.36, 'shares': 49, 'target': 0.05},
    'b': {'price': 26.50, 'shares': 294, 'target': 0.65},
    'c': {'price': 26.11, 'shares': 117, 'target': 0.25},
    'd': {'price': 16.56, 'shares': 0, 'target': 0.05}
}

# TODO: have your deposit/withdrawal here
new_cash_pos = 5000

old_total = sum(portfolio[x]['price'] * portfolio[x]['shares'] for x in portfolio.keys())
new_total = moneyify(old_total + new_cash_pos)

old_ind = {x: portfolio[x]['price'] * portfolio[x]['shares'] for x in portfolio.keys()}
old_alloc = {x: percentify(old_ind[x], old_total) for x in portfolio.keys()}

new_ind = {x: moneyify(new_total * portfolio[x]['target']) for x in portfolio.keys()}
new_alloc = {x: percentify(new_ind[x], new_total) for x in portfolio.keys()}

diff = {x: moneyify(new_ind[x] - (portfolio[x]['price'] * portfolio[x]['shares'])) for x in portfolio.keys()}

print("Portfolio Value: ${}".format(moneyify(old_total)))
print("Cash Investments: {}".format(print_money(new_cash_pos)))

print('\n-------------ORDERS-------------')
for ticker in portfolio.keys():
    price = portfolio[ticker]['price']
    # Sell
    if diff[ticker] < 0:
        sell_shares = int(abs(round(diff[ticker] / float(price), 0)))
        print("{} Sell: {} shares at {}, total value {}".format(ticker, sell_shares, print_money(price), print_money(diff[ticker])))
        print("{} Buy: N/A".format(ticker))
    elif diff[ticker] > 0:
        buy_shares = int(round(diff[ticker] / float(price), 0))
        print("{} Sell: N/A".format(ticker))
        print("{} Buy: {} shares at {}, total value {}".format(ticker, buy_shares, print_money(price), print_money(diff[ticker])))
    print('-------------{}-------------'.format(len('ORDERS') * '-'))

print('\n----------SUMMARY------------')
for ticker in portfolio.keys():
    print('{} Before: {}% of portfolio, total value {}'.format(ticker, old_alloc[ticker], print_money(old_ind[ticker])))
    print('{} After: {}% of portfolio, total value {}'.format(ticker, new_alloc[ticker], print_money(new_ind[ticker])))
    print('----------{}------------'.format(len('SUMMARY') * '-'))

print("Portfolio Value: ${}".format(moneyify(new_total)))
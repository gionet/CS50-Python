import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        print('Missing command-line argument')
        sys.exit(1)

    try:
        number = float((sys.argv[1]))

    except ValueError:
        print('Command-line argument is not a number')
        sys.exit(1)

    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    o = response.json()
    # data = json.dumps(response.json(), indent=2)

    try:
        usd_rate = o['bpi']['USD']['rate_float']
        total_price = usd_rate * number

    except requests.RequestException:
        print('Request Exception')
        sys.exit(1)

    print(f'${total_price:,.4f}')


if __name__ == '__main__':
    main()
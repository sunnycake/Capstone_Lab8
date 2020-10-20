import requests
# more readable json import pprint
# from pprint import pprint 

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main():
    dollars = get_us_dollars()
    bitcoin_rate = convert_dollars_to_bitcoin(dollars)
    display_results(dollars, bitcoin_rate)


def get_us_dollars():
    while True:
        try:
            dollars = float(input('Enter dollars: '))
            if dollars >= 0:
                return dollars
            else:
                print('Enter number greater than 0. ')
        except ValueError:
            print('Error - Please enter a valid number. ')


def convert_dollars_to_bitcoin(dollars):
    exchange_rate = request_rate(dollars)
    bitcoin = convert(dollars, exchange_rate)
    return bitcoin
    

def request_rate(rate):
    try:
        response = requests.get(coindesk_url)
        data = response.json()
        dollars_exchange_rate = data['bpi']['USD']['rate_float']
        return(dollars_exchange_rate)
    except Exception as e:
        print(f'Error making request. ', e)


def convert(dollars, bitcoin_rate):
    return dollars * bitcoin_rate


def display_results(dollars, bitcoin):
    print(f'${dollars:.2f} is equivalent to {bitcoin:.2f} Bitcoin.')



if __name__ == '__main__':
    main()

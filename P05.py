import requests
import csv
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if response.status_code == 200:
        data = response.json()
        price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        price_gbp = float(data['bpi']['GBP']['rate'].replace(',', ''))
        price_eur = float(data['bpi']['EUR']['rate'].replace(',', ''))

        # Archivo en TXT
        with open('bitcoin_prices.txt', 'w') as txt_file:
            txt_file.write(f'USD: {price_usd} USD\n')
            txt_file.write(f'GBP: {price_gbp} GBP\n')
            txt_file.write(f'EUR: {price_eur} EUR\n')

        # Archivo en CSV
        with open('bitcoin_prices.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Currency', 'Price'])
            writer.writerow(['USD', price_usd])
            writer.writerow(['GBP', price_gbp])
            writer.writerow(['EUR', price_eur])

        print('Los datos de precio de Bitcoin se han almacenado correctamente.')

    else:
        print('Error al obtener el precio de Bitcoin')

except requests.RequestException as e:
    print(f'Error al realizar la solicitud HTTP: {str(e)}')

except KeyError:
    print('No se pudo obtener el precio de Bitcoin de la respuesta JSON')

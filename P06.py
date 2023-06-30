import sqlite3
import requests
import csv
from datetime import datetime

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if response.status_code == 200:
        data = response.json()
        price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        price_gbp = float(data['bpi']['GBP']['rate'].replace(',', ''))
        price_eur = float(data['bpi']['EUR']['rate'].replace(',', ''))
        
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('bitcoin_prices.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bitcoin (
                currency TEXT,
                price REAL,
                date TEXT
            )
        ''')
        conn.commit()

        cursor.execute('INSERT INTO bitcoin (currency, price, date) VALUES (?, ?, ?)', ('USD', price_usd, current_date))
        cursor.execute('INSERT INTO bitcoin (currency, price, date) VALUES (?, ?, ?)', ('GBP', price_gbp, current_date))
        cursor.execute('INSERT INTO bitcoin (currency, price, date) VALUES (?, ?, ?)', ('EUR', price_eur, current_date))
        conn.commit()

        print('Los datos de precio de Bitcoin se han almacenado correctamente en la base de datos.')
        
        conn.close()
        
        with open('bitcoin_prices.txt', 'w') as txt_file:
            txt_file.write(f'USD: {price_usd} USD\n')
            txt_file.write(f'GBP: {price_gbp} GBP\n')
            txt_file.write(f'EUR: {price_eur} EUR\n')
        
        with open('bitcoin_prices.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Currency', 'Price', 'Date'])
            writer.writerow(['USD', price_usd, current_date])
            writer.writerow(['GBP', price_gbp, current_date])
            writer.writerow(['EUR', price_eur, current_date])
    else:
        print('Error al obtener el precio de Bitcoin')

except requests.RequestException as e:
    print(f'Error al realizar la solicitud HTTP: {str(e)}')

except KeyError:
    print('No se pudo obtener el precio de Bitcoin de la respuesta JSON')

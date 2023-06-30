import requests
while True:
 try:   
    n = int(input("Ingrese la cantidad de bitcoins que posee: "))    
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if response.status_code == 200:        
        data = response.json()        
        price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        price_gbp = float(data['bpi']['GBP']['rate'].replace(',', ''))
        price_eur = float(data['bpi']['EUR']['rate'].replace(',', ''))
        # Precio Total por tipo de cambio
        total_value_usd = n * price_usd
        total_value_gbp = n * price_gbp
        total_value_eur = n * price_eur
        # Formato deseado
        formatted_value_usd = '{:,.4f}'.format(total_value_usd)
        formatted_value_gbp = '{:,.4f}'.format(total_value_gbp)
        formatted_value_eur = '{:,.4f}'.format(total_value_eur)

        print(f'El costo actual de {n} monedas de Bitcoins es de:')
        print(f'USD: {formatted_value_usd}')
        print(f'GBP: {formatted_value_gbp}')
        print(f'EUR: {formatted_value_eur}')
        break

    else:        
        print('Error al obtener el precio de Bitcoin')

 except (ValueError, requests.RequestException) as e:    
    print(f'Error: {str(e)}')
    print('El formato ingresado no es el correcto intente de nuevo....')



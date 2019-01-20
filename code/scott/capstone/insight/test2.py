# from django.shortcuts import render
# from models import IP
# from forms import IP_Form
# from django.utils import timezone
# from shodan import Shodan
# #from sho import do_shodan
# import censys.ipv4
# #from cens import do_censys
# from insight.config import shodan_key, censys_api_id, censys_api_secret

# from ipware import get_client_ip




def do_censys(ip_address):
    try:
        # c = censys.ipv4.CensysIPv4(api_id=censys_api_id, api_secret=censys_api_secret)
        # query = ' '.join(ip_address)
        # result = c.view(query)

        result = {
            'tags': ['cwmp', 'ipp', 'printer', 'http'],
            'ip': '120.50.13.165',
            'updated_at': '2019-01-15T15:37:24+00:00',
            'ports': [16992, 8080, 80, 631, 8888, 7547],
            'location': {
                'province': 'Dhaka Division',
                'city': 'Dhaka',
                'country': 'Bangladesh',
                'longitude': 90.4598,
                'registered_country': 'Bangladesh',
                'registered_country_code': 'BD',
                'postal_code': '1362',
                'country_code': 'BD',
                'latitude': 23.7121,
                'timezone': 'Asia/Dhaka',
                'continent': 'Asia'
            },
            'autonomous_system': {
                'description': 'TELNET-AS-BD-AP Telnet Communication Limited',
                'rir': 'unknown',
                'routed_prefix': '120.50.13.0/24',
                'country_code': 'BD',
                'path': [11164, 4637, 9498, 58682, 38712],
                'asn': 38712,
                'name': 'TELNET-AS-BD-AP Telnet Communication Limited'},
            'protocols': [
                '80/http', '631/ipp', '7547/cwmp', '16992/http', '8888/http', '8080/http'
            ]
        }
        
        # formatting result for display
        censys_result_clean = {
            'location': {
                'Country': result['location']['country_name'],
                'Region': result['location']['province'],
                'City': result['location']['city'],
                'Latitute': result['location']['latitude'],
                'Longitude': result['location']['longitude']
            },
            'network': {
                'ASN': result['autonomous_system']['asn'],
                'ASN Name': result['autonomous_system']['name']
            },
            'device': {
                'OS': result['os'],
                'Ports': result['protocols'],
            }
        }

        print(censys_result_clean)

    except Exception as e:
            return f'Error: {e}'


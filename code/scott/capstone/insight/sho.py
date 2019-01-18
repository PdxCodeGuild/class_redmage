import sys
from shodan import Shodan
from config import shodan_key



try:
    sho = Shodan(shodan_key)
    # query = ' '.join("120.50.13.165")
    result = sho.host("123.245.10.187", minify=True)
    print(result)
    # sample result
    # result = {
    #     'region_code': '81',
    #     'tags': [],
    #     'ip': 2016546213,
    #     'area_code': None,
    #     'latitude': 23.729000000000013,
    #     'hostnames': ['NEW-ASSIGNED-FROM-APNIC-20-03-2008.telnet.net.bd'],
    #     'postal_code': '1000',
    #     'dma_code': None,
    #     'country_code': 'BD',
    #     'org': 'Telnet Communication Limited',
    #     'data': [],
    #     'asn': 'AS38712',
    #     'city': 'Dhaka',
    #     'isp': 'Telnet Communication Limited',
    #     'longitude': 90.41120000000001,
    #     'last_update': '2019-01-16T16:39:57.393738',
    #     'country_code3': 'BGD',
    #     'country_name': 'Bangladesh',
    #     'ip_str': '120.50.13.165',
    #     'os': None,
    #     'ports': [
    #         5555, 8554, 7547, 4664, 23424, 9000,
    #         9869, 7779, 5357, 9981, 1234, 8181,
    #         3749, 311, 3310, 1911, 2086, 8009,
    #         8081, 8086, 1599, 7474, 5601,
    #         9295, 6664, 51106, 82, 10243, 8889,
    #         8112, 83, 4782, 5001, 52869, 10000,
    #         8126, 2082, 4022, 80, 81, 113, 8098,
    #         10554, 8888, 1471,
    #     ]
    # }

    # formatting result for display
    shodan_result_clean = {
        'location': {
            'Country': result['country_name'],
            'Region': result['region_code'],
            'City': result['city'],
            'Latitute': result['latitude'],
            'Longitude': result['longitude']
        },
        'network': {
            'ASN': result['asn'],
            'ASN Name': result['isp'],
            # 'Host Name': result['hostnames'][0]
        },
        'device': {
            'OS': result['os'],
            'Ports': result['ports']
            #'Vulnerabilities': result['vulns'],
        }
    }
    if len(result['hostnames']) > 0:
        shodan_result_clean['network']['Host Name'] = result['hostnames'][0]
    if 'vulns' in result:
        shodan_result_clean['device']['Vulnerabilities'] = result['vulns']

    print(shodan_result_clean)

except Exception as e:
        print(f'Error: {e}')


### Sample responses to sho.host *ip*

# {
#     'region_code': '81', 
#     'tags': [], 
#     'ip': 2016546213, 
#     'area_code': None, 
#     'latitude': 23.729000000000013, 
#     'hostnames': ['NEW-ASSIGNED-FROM-APNIC-20-03-2008.telnet.net.bd'], 
#     'postal_code': '1000', 
#     'dma_code': None, 
#     'country_code': 'BD', 
#     'org': 'Telnet Communication Limited', 
#     'data': [], 
#     'asn': 'AS38712', 
#     'city': 'Dhaka', 
#     'isp': 'Telnet Communication Limited', 
#     'longitude': 90.41120000000001,
#     'last_update': '2019-01-15T21:20:00.178627', 
#     'country_code3': 'BGD', 
#     'country_name': 'Bangladesh', 
#     'ip_str': '120.50.13.165', 
#     'os': None, 
#     'ports': [
#         8009, 8081, 8086, 1599, 7474, 5601, 9295, 6664, 
#         51106, 82, 10243, 8889, 8112, 83, 4782, 5001, 
#         52869, 10000, 8126, 1911, 2082, 4022, 80, 81, 
#         113, 8098, 10554, 8888, 1471, 1024, 2087, 5901, 
#         8080, 3000, 25105, 1234, 23424, 7777, 5000, 32400, 8834
#         ]
#     }

# {
#     'region_code': 'UT',
#     'tags': ['starttls'],
#     'ip': 844581816,
#     'area_code': 801,
#     'latitude': 40.21809999999999,
#     'hostnames': ['50-87-75-184.unifiedlayer.com'],
#     'postal_code': '84606',
#     'dma_code': 770,
#     'country_code': 'US',
#     'org': 'Unified Layer',
#     'data': [],
#     'asn': 'AS46606',
#     'city': 'Provo',
#     'isp': 'Unified Layer',
#     'longitude': -111.6133,
#     'last_update': '2019-01-14T21:06:51.916299',
#     'country_code3': 'USA',
#     'vulns': [
#         'CVE-2011-5000',
#         'CVE-2017-15906',
#         'CVE-2014-1692',
#         'CVE-2010-5107',
#         'CVE-2018-15473',
#         'CVE-2016-10708',
#         'CVE-2010-4478',
#         'CVE-2016-0777',
#         'CVE-2011-4327',
#         'CVE-2010-4755',
#         'CVE-2012-0814'],
#     'country_name': 'United States',
#     'ip_str': '50.87.75.184',
#     'os': None,
#     'ports': [
#         993, 110, 465, 8080, 587, 143, 21, 8443, 2082, 995, 80, 22, 25, 443, 2083, 26]
#       }

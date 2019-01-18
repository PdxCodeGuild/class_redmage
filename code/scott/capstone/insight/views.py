from django.shortcuts import render
from .models import IP
from .forms import IP_Form
from django.utils import timezone
from shodan import Shodan
#from sho import do_shodan
import censys.ipv4
#from cens import do_censys
from insight.config import shodan_key, censys_api_id, censys_api_secret

# from ipware import get_client_ip


def do_shodan(ip_address):
    try:
        sho = Shodan(shodan_key)
        result = sho.host(ip_address, minify=True)

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
                # 'Host Name': result['hostnames']
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
        if result['os'] != 'None':
            shodan_result_clean['device']['Vulnerabilities'] = result['vulns']

        return shodan_result_clean

    except Exception as e:
            return f'Error: {e}'


def do_censys(ip_address):
    try:
        c = censys.ipv4.CensysIPv4(api_id=censys_api_id, api_secret=censys_api_secret)
        result = c.view(ip_address)

        # sample result
        # result = {
        #     'tags': ['cwmp', 'ipp', 'printer', 'http'],
        #     'ip': '120.50.13.165',
        #     'updated_at': '2019-01-15T15:37:24+00:00',
        #     'ports': [16992, 8080, 80, 631, 8888, 7547],
        #     'location': {
        #         'province': 'Dhaka Division',
        #         'city': 'Dhaka',
        #         'country': 'Bangladesh',
        #         'longitude': 90.4598,
        #         'registered_country': 'Bangladesh',
        #         'registered_country_code': 'BD',
        #         'postal_code': '1362',
        #         'country_code': 'BD',
        #         'latitude': 23.7121,
        #         'timezone': 'Asia/Dhaka',
        #         'continent': 'Asia'
        #     },
        #     'autonomous_system': {
        #         'description': 'TELNET-AS-BD-AP Telnet Communication Limited',
        #         'rir': 'unknown',
        #         'routed_prefix': '120.50.13.0/24',
        #         'country_code': 'BD',
        #         'path': [11164, 4637, 9498, 58682, 38712],
        #         'asn': 38712,
        #         'name': 'TELNET-AS-BD-AP Telnet Communication Limited'},
        #     'protocols': [
        #         '80/http', '631/ipp', '7547/cwmp', '16992/http', '8888/http', '8080/http'
        #     ]
        # }

        # formatting result for display
        censys_result_clean = {
            'location': {
                'Country': result['location']['country'],
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
                # 'OS': result['autonomous_system']['os'],
                'Ports': result['protocols'],
            }
        }

        if 'os' in result['autonomous_system']:
             censys_result_clean['device']['OS'] = result['autonomous_system']['os']

        return censys_result_clean

    except Exception as e:
            return f'Error: {e}'

def index(request):

    if request.method == 'POST':
        form = IP_Form(request.POST)
        if form.is_valid():
            # getting IP address from form
            ip_address = form.cleaned_data['ip_address']
            # creating new instance
            newIP = IP(ip_address=ip_address)
            # running censys and shodan searches against the IP
            censys_search = do_censys(ip_address)
            shodan_search = do_shodan(ip_address)
            # adding censys and shodan results to the instance
            newIP.censysresult=censys_search
            newIP.shodanresult=shodan_search
            newIP.save()  # saving the instance
            form = IP_Form()  # blanking out the form

            
            shodan_search_location = shodan_search['location']
            shodan_search_network = shodan_search['network']
            shodan_search_device = shodan_search['device']

            censys_search_location = censys_search['location']
            censys_search_network = censys_search['network']
            censys_search_device = censys_search['device']

            context = {
                'form': form,
                # 'shodan_search': shodan_search,
                'shodan_search_location': shodan_search_location,
                'shodan_search_network': shodan_search_network,
                'shodan_search_device': shodan_search_device,

                # 'censys_search': censys_search,
                'censys_search_location': censys_search_location,
                'censys_search_network': censys_search_network,
                'censys_search_device': censys_search_device,
            }

        else:
            form = IP_Form() # blanking out the form

    else:
        form = IP_Form()
        context = {
            'form': form,
            }

    return render(request, 'insight/index.html', context)

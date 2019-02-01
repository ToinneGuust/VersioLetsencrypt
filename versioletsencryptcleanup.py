from requests.auth import HTTPBasicAuth
import requests
import json
import sys

#################
# CONFIGURATION #
#################
#Do not forget to add the public IP into the allowed IPs for API use
baseURL = 'https://www.versio.nl/api/v1'
#baseURL = 'https://www.versio.nl/testapi/v1'
user = 'Versio_login'
password = 'Versio_password'


##########
# SCRIPT #
##########
domain = sys.argv[1]

print '-------------'
print 'versioletsencryptcleanup.py started'
print domain

r = requests.get(baseURL+'/domains/'+domain+'?show_dns_records=true', auth=HTTPBasicAuth(user, password))
parsed_json = json.loads(r.text)
dns_records = parsed_json['domainInfo']['dns_records']

pop_records = 1
while pop_records == 1:
    i=0
    pop_records = 0
    for dns_record in dns_records:
        if dns_record['name'] == '_acme-challenge.'+domain+'.' and pop_records == 0:
            print 'popping:'
            print dns_record
            dns_records.pop(i)
            pop_records = 1
        i += 1

returnJson = json.loads('{"dns_records" : ' + json.dumps(dns_records) + '}')
r = requests.post('https://www.versio.nl/api/v1/domains/'+domain+'/update', auth=HTTPBasicAuth(user, password), data = json.dumps(returnJson))
print '-------------'

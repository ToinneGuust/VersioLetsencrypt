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
key = sys.argv[2]

print '-------------'
print 'versioletsencrypt.py started'
print domain
print key

TXTrecord = '{"type":"TXT","name":"_acme-challenge.'+domain+'.","value":"\\"'+key+'\\"","prio":0,"ttl":300}'
jsonTXTrecord = json.loads(TXTrecord)

r = requests.get(baseURL+'/domains/'+domain+'?show_dns_records=true', auth=HTTPBasicAuth(user, password))
parsed_json = json.loads(r.text)
dns_records = parsed_json['domainInfo']['dns_records']
dns_records.append(jsonTXTrecord)
returnJson = json.loads('{"dns_records" : ' + json.dumps(dns_records) + '}')
r = requests.post('https://www.versio.nl/api/v1/domains/'+domain+'/update', auth=HTTPBasicAuth(user, password), data = json.dumps(returnJson))
print '-------------'

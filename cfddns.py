import time
import requests
import json
import logging

exisiting_ip = "empty"

headers = {
    "X-Auth-Email": "email@email.com",
    "X-Auth-Key": "auth key",
    'Content-Type': "application/json",
}

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("/var/log/cfddns.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

if exisiting_ip == "empty" :
    exisiting_ip = ((requests.get('http://ip.42.pl/raw')).content)
    logger.info('exisiting ip is {}'.format(exisiting_ip))

while 1:
    time.sleep(10)
    new_ip = ((requests.get('http://ip.42.pl/raw')).content)
    if new_ip != exisiting_ip :
        data = '{"type":"A","name":"your.sub.domain","content":"' + new_ip + '","ttl":120,"proxied":false}'
        response = requests.put('https://api.cloudflare.com/client/v4/zones/zone_id/dns_records/dns_id', headers=headers, data=data)
        logger.info("change cloudflare ip to {}".format(new_ip))
        exisiting_ip = new_ip
    else :
        print("no change")

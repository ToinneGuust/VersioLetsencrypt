#!/bin/bash
#echo $CERTBOT_DOMAIN
#echo $CERTBOT_VALIDATION
#echo $CERTBOT_TOKEN
#echo $CERTBOT_AUTH_OUTPUT
python /home/pi/scripts/versioletsencryptcleanup.py $CERTBOT_DOMAIN $CERTBOT_VALIDATION

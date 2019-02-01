# VersioLetsencrypt
Manual hooks for certbot DNS-01 verification with the versio.nl api

1. Modify the username and password in the .py scripts according to your versio username and password
2. Verify your ip has acces to the versio API https://www.versio.nl/customer/account/api or Account > Versio API
3. Configure certbot's manual_auth_hook and manual-cleanup-hook to call the .sh files in this repositorie

example certbot config:
```
  version = 0.28.0
  archive_dir = /etc/letsencrypt/archive/example.com
  cert = /etc/letsencrypt/live/example.com/cert.pem
  privkey = /etc/letsencrypt/live/example.com/privkey.pem
  chain = /etc/letsencrypt/live/example.com/chain.pem
  fullchain = /etc/letsencrypt/live/example.com/fullchain.pem

  # Options used in the renewal process
  [renewalparams]
  server = https://acme-v02.api.letsencrypt.org/directory
  authenticator = manual
  manual_public_ip_logging_ok = True
  manual_auth_hook = /home/ToinneGuust/scripts/versioletsencrypt.sh
  manual_cleanup_hook = /home/ToinneGuust/scripts/versioletsencryptcleanup.sh
  pref_challs = dns-01
  account = abcdefghijklmnopqrstuvwxyz123456
```
4. A simple entry in crontab can renew your certs automatically
```
@daily certbot renew
```

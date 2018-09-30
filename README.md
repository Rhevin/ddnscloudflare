# ddnscloudflare
this will help you change your A record to your cloudflare domain / sub domain by updating it dynamicaly when it's change
it's suitable for raspberry / pine64 user that need to remote it but have dynamic IP

# Things to Do
+ Make sure you already have domain that pointed to Cloudflare
+ Get your cloudflare api key in here
  https://support.cloudflare.com/hc/en-us/articles/200167836-Where-do-I-find-my-Cloudflare-API-key-
+ Get Zone ID
  ```  curl -X GET "https://api.cloudflare.com/client/v4/zones?   name=example.com&status=active&page=1&per_page=20&order=status&direction=desc&match=all" \
     -H "X-Auth-Email: user@example.com" \
     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
     -H "Content-Type: application/json"
     ```
change `name=example.com` with your domain name, `user@example.com` with your email, and `xauthkey` with you api key
+ Check for zone id in result, example `7c5dae5552338874e5053f2534d2767a`
+ Get DNS ID
```  curl -X GET "https://api.cloudflare.com/client/v4/zones/023e105f4ecef8ad9ca31a8372d0c353/dns_records?type=A&name=example.com" \
     -H "X-Auth-Email: user@example.com" \
     -H "X-Auth-Key: c2547eb745079dac9320b638f5e225cf483cc5cfdda41" \
     -H "Content-Type: application/json"
```
change `name=example.com` with your domain name, `user@example.com` with your email, and `xauthkey` with you api key, `023e105f4ecef8ad9ca31a8372d0c353` with your zone id

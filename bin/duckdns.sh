##############################################
################   Edit here  ################

TOKEN="<Your DuckDNS Token>"

DOMAIN="<Your Domain name without http:// and duckdns.org>"
#eg:- if your domain is http://example.duckdns.org, your domain name you should enter above is "example"



##############################################
############     Optional     ################
#uncomment below 2 lines and edit the UINTERVAL value if you don't like 15 minutes default IP update interval.. Otherwose leave it unedited as is..
#UINTERVAL=15
#echo "*/$UINTERVAL * * * * ~/bin/duckdns.sh&&date >~/duck.log" > /data/data/com.termux/files/usr/var/spool/cron/crontabs.11699


##############################################
############  Don't edit below  ##############

IPV6ADDRESS=$(curl http://ipv6.icanhazip.com/)
echo "Your IPV6 is $IPV6ADDRESS"
curl "https://www.duckdns.org/update?domains=$DOMAIN&token=$TOKEN&ipv6=$IPV6ADDRESS&verbose=true"


#https://www.duckdns.org/update?domains={YOURVALUE}&token={YOURVALUE}[&ip={YOURVALUE}][&ipv6={YOURVALUE}][&verbose=true][&clear=true]



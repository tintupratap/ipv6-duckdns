bash dependencies.sh

cp -r bin ~/bin

echo "Set SSH password"

passwd

echo "*/15 * * * * ~/bin/duckdns.sh&&date >~/duck.log" > /data/data/com.termux/files/usr/var/spool/cron/crontabs.11699

chmod +x /data/data/com.termux/files/usr/var/spool/cron/crontabs.11699

echo "export PATH=~/bin:$PATH" >> ~/.bashrc

echo 'Done, please create DuckDNS domain and get API key..'

echo 'Edit ~/bin/duckdns.sh file and put your API there..'

echo 'Once done, you can run expose.sh in terminal to start publicly accessible(IPV6) server..'


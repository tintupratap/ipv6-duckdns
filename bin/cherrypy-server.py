import cherrypy
import subprocess
import time
import string
wake_unlock=subprocess.run(['termux-wake-unlock'],stdout=subprocess.PIPE)
print(wake_unlock.stdout)
wake_lock=subprocess.run(['termux-wake-lock'],stdout=subprocess.PIPE)
print(wake_lock.stdout)
exposer=subprocess.run(['bash','/data/data/com.termux/files/home/bin/duckdns.sh'],stdout=subprocess.PIPE)
print(exposer.stdout)
crond_kill=subprocess.run(['pkill', 'crond'], stdout=subprocess.PIPE)
print(crond_kill.stdout)
crond=subprocess.run(['crond'], stdout=subprocess.PIPE)
print(crond.stdout)
sshd_kill=subprocess.run(['pkill','sshd'], stdout=subprocess.PIPE)
print(sshd_kill.stdout)
sshd=subprocess.run(['sshd'], stdout=subprocess.PIPE)
print(sshd.stdout)
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return '''<html>
<body>
<p>Hello, Human!! Got me? Nice try..</p>
<p>You can now access my device!!</p>
<p><img src="https://picsum.photos/200" alt="randompic" /></p>
<a href="http://tintupratap.duckdns.org:8080/info">neofetch</a>
<a href="http://tintupratap.duckdns.org:8080/termux_info">termux-info</a>
<a href="http://tintupratap.duckdns.org:8080/net">ifconfig</a>
<p>&copy; R4N4C0D3R </p>
</body>
</html>'''

    @cherrypy.expose
    def id(self):
        username=subprocess.run(['id'], stdout=subprocess.PIPE)
        result=username.stdout.decode("utf-8")
        return result

    @cherrypy.expose
    def termux_info(self):
        info=subprocess.run(['bash','/data/data/com.termux/files/home/bin/termux-info-html.sh'],stdout=subprocess.PIPE)
        result=info.stdout.decode("utf-8")
        return result
    @cherrypy.expose
    def net(self):
        network=subprocess.run(['bash','/data/data/com.termux/files/home/bin/ifconfig-html.sh'],stdout=subprocess.PIPE)
        result=network.stdout.decode("utf-8")
        return result
    @cherrypy.expose
    def info(self):
        neofetch=subprocess.run(['bash','/data/data/com.termux/files/home/bin/neofetch-html.sh'],stdout=subprocess.PIPE)
        result=neofetch.stdout.decode("utf-8")
        return result
    @cherrypy.expose
    def ssh(self):
        username=subprocess.run(['id','-un'], stdout=subprocess.PIPE)
        userhost=username.stdout.decode("utf-8")+"@tintupratap.duckdns.org".replace(" ","").translate({ord(c): None for c in string.whitespace})
        concatstr=str(str(userhost).translate({ord(c): None for c in string.whitespace}))
        result= "ssh "+concatstr+" -p 8022"
        return result

if __name__ == '__main__':
    cherrypy.server.socket_host = '::'
    cherrypy.quickstart(HelloWorld())

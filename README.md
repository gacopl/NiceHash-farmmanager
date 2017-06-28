# NiceHash-farmmanager
This will allow you to monitor all your nicehash mining rigs in one place, easily add and remove rigs from UI
Of course you will need NiceHashMiner from my repo it includes patched WebManager running on your rigs for this to work

# Configuration

By default the web server will start on localhost:8885/nhmfm admin/admin, you can and should change this in nhmfm.conf
You can run this behind nginx or apache reverse proxy if you wish without any magic setup

# Windows
For windows download the binaries from release page, or build it on your own, things needed for building:
Python3 for windows, pip, cherrypy, pyinstaller, then just run build-win.bat

# Linux
For linux you can run directly from sources but you will need to have installed python3, pip3, cherrypy, i also attached script for building 
Linux ELF if for some reason you need it.
To test run do "python3 nhmfm.py" 
To install it properly mv contents to /opt/nhmfm, create user nhmfm, copy ubuntu.init.sh to /etc/init.d/nhmfm
and then you can do service nhmfm start/stop/status (at least in Ubuntu)

Please feel free to contribute I am no html expert at all, it's working but it could be looking better

# Tips
1Cnb8ievaqvsJwg5VL5xiss2EzGLYu1HD6

# Roadmap (if tips will be coming...)
* Update NHM-gaco-mod with proper API with keys instead of webmanager
* Add control over your nhm mining rigs (start/stop)
* Update your mining rigs from one place
* Configure your mining rigs (algos and settings) through farm manager UI


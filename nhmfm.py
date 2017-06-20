import cherrypy
import os
import sqlite3

import json
import urllib.request, urllib.error, urllib.error, json
from socket import timeout

from mako.template import Template

cherrypy.config.update("nhmfm.conf")

db = "db.sqlite3"

class NHMFM(object):
	@cherrypy.expose
	def index(self):
		rigs = self.getRigs()
		mytemplate = Template(filename='templates/index.html')
		return mytemplate.render(rigs=rigs)


	@cherrypy.expose
	def stats(self, ip):
		try:
			with urllib.request.urlopen("http://" + ip + ":8888/stats.json", timeout=1) as url:
				data = json.loads(url.read().decode())
		except (urllib.error.HTTPError, urllib.error.URLError) as error:
			data = str('socket error')
		except timeout:
			data = str('socket timed out - URL %s', ip)

		return json.dumps(data)

	@cherrypy.expose
	def setRigs(self, rigs):
		if not isinstance(rigs, list):
			rigs = [ rigs ]

		db = self.connect_db()
		sql = 'delete from rigs'
		cur = db.execute(sql)
		db.commit()

		for rig in rigs:
			rig_row = rig.split(',')
			sql = 'insert into rigs VALUES ("' + rig_row[0] + '", "' + rig_row[1] + '", "'  + rig_row[2] + '", "'  + rig_row[3] + '")'
			cur = db.execute(sql)
		
		db.commit()
		db.close()
		return json.dumps({'redirect': cherrypy.server.base_url})

	def getRigs(self):
		db = self.connect_db()
		sql = 'select * from rigs'
		cur = db.execute(sql)
		rigs = [dict(id=row[0], name=row[1], ip=row[2], api=row[3]) for row in cur.fetchall()]
		db.close()
		return rigs



	@cherrypy.expose
	def config(self):
		mytemplate = Template(filename='templates/config.html')
		return mytemplate.render(rigs = self.getRigs())


	def connect_db(self):
		return sqlite3.connect(db)



if __name__ == '__main__':
    conf = {
    	'/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    cherrypy.quickstart(NHMFM(), cherrypy.server.base_url, conf)
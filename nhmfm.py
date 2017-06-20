import cherrypy
import os
import sqlite3

import json
import urllib.request, json 

from mako.template import Template


db = "db.sqlite3"

class NHMFM(object):
	@cherrypy.expose
	def index(self):
		rigs = self.getRigs()
		mytemplate = Template(filename='templates/index.html')
		return mytemplate.render(rigs=rigs)
#		return open('templates/index.html')

	@cherrypy.expose
	def stats(self, ip):
		with urllib.request.urlopen("http://" + ip + ":8888/stats.json") as url:
			data = json.loads(url.read().decode())
		return json.dumps(data)

	@cherrypy.expose
	def setRigs(self, rigs):
		print(rigs)
		if not isinstance(rigs, list):
			print("not list")
			rigs = [ rigs ]
		print(rigs)
		db = self.connect_db()
		sql = 'delete from rigs'
		cur = db.execute(sql)
		db.commit()
		print(sql)
		for rig in rigs:
			rig_row = rig.split(',')
			print(rig_row)
			sql = 'insert into rigs VALUES ("' + rig_row[0] + '", "' + rig_row[1] + '", "'  + rig_row[2] + '", "'  + rig_row[3] + '")'
			cur = db.execute(sql)
			print(cur)
		print(db.commit())
		db.close()
		return json.dumps(rigs)

	def getRigs(self):
		db = self.connect_db()
		sql = 'select * from rigs'
		print(sql)
		cur = db.execute(sql)
		rigs = [dict(id=row[0], name=row[1], ip=row[2], api=row[3]) for row in cur.fetchall()]
		print(rigs)
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
    cherrypy.quickstart(NHMFM(), '/nhmfm', conf)
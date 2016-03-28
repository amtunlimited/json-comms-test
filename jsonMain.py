#!/usr/bin/python

import web
import json

urls = (
	'/json/', 'test',
	'/', 'index'
)

class test:
	def POST(self):
		ops = json.loads(web.data())
		web.header('Content-Type', 'application/json')
		return json.dumps({"result" : (ops["in1"] + ops["in2"])})

class index:
	def GET(self):
		index = web.template.frender('index.html')
		return index()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

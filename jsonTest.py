#!/usr/bin/python

import web
import json

urls = (
	'/json/jsonTest.py/test', 'test'
)

class test:
	def POST(self):
		ops = json.loads(web.data())
		web.header('Content-Type', 'application/json')
		return json.dumps({"result" : (ops["in1"] + ops["in2"])})

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

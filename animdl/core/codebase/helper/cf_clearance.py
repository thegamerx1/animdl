import os
from configparser import ConfigParser
config = ConfigParser()

configFilePathVeryLongName = os.path.join(
	os.getenv("APPDATA"), "AnimDL", "config.ini")


config.read(configFilePathVeryLongName)
if not os.path.exists(configFilePathVeryLongName):
	os.makedirs(os.path.dirname(configFilePathVeryLongName), exist_ok=True)
	config.add_section('main')


def query(session, useConfig):
	if useConfig:
		useragent = config.get("main", "useragent")
		cf_clearance = config.get("main", "cf_clearance")
	else:
		useragent = input("user-agent: ")
		cf_clearance = input("cf_clearance: ")
		if useragent == "":
			useragent = config.get("main", "useragent")

	session.cookies.set("cf_clearance", cf_clearance)
	session.headers.update({"User-Agent": useragent})

	config.set('main', 'cf_clearance', cf_clearance)
	config.set('main', 'useragent', useragent)

	with open(configFilePathVeryLongName, 'w') as f:
		config.write(f)

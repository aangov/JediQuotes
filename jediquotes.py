#!/usr/bin/env python2

import twitter
import random
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config")
credentials = dict()

for key, value in config.items("Credentials"):
    credentials[key]=value

f = open ("jediquotes", "r")
data = f.readlines()

api = twitter.Api(**credentials)

api.PostUpdate(random.choice(data))

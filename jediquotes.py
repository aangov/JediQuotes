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

data = []

for line in f.readlines():
    data.append(line)

api = twitter.Api(**credentials)

api.PostUpdate(random.choice(data))

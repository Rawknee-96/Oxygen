import json
import os

with open("info.json", "r") as f:
  DATA = json.load(f)

OWNER_IDS = DATA["OWNER_IDS"]
EXTENSIONS = DATA["EXTENSIONS"]
No_Prefix = DATA["np"]
NAME = DATA["name"]
server = DATA["server"]
ch = DATA["ch"]
CID = ch
OpenAi = DATA["OpenAi"]

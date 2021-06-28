import requests
import time
from os import system

url = "http://10.54.158.207:4348/containers/json?all=l"
command = "st2 action execute service_remediations_pack.docker_remediations_action message='NEP@L_Monitoring is CRITICAL docker container stopped value:  1'"

def ejecutaScript():
    res = requests.get(url)
    js = res.json() 

    for service in js:
        if str(service["Names"]) == "['/kapacitor']" and str(service["State"]) != "running":
            system(command)
while True:
    ejecutaScript()
    time.sleep(180)
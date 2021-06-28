import subprocess
import json

from st2common.runners.base_action import Action

class EchoRemote(Action):
    def run(self, hosts, username, private_key, cmd):
        print()
        execution = subprocess.check_output("st2 run core.remote hosts='{}' username='{}' private_key='{}' cmd='{}' -j".format(hosts, username, private_key, cmd), shell=True)
        print(json.loads(execution))
        #id_execution = json.loads(execution)[0]["id"]
        return (False)

import subprocess
import json
from functions import send_email, syslog, vm_remed

from st2common.runners.base_action import Action

class EchoRemote(Action):
    def run(self, 
            hosts='10.54.158.192' , 
            username='root', 
            private_key='/home/stanley/.ssh/id_rsa', 
            cmd='systemctl is-enabled docker', 
            message='NEP@L_NSO is CRITICAL docker container stopped value:  1', 
            VM=False, 
            Docker=False):
        if Docker:
            remote = subprocess.check_output("st2 run core.remote hosts='{}' username='{}' private_key='{}' cmd='{}' -j".format(hosts, username, private_key, cmd), shell=True)
            result_state = json.loads(remote)["result"][hosts]["stdout"]
            if 'enabled' in result_state:
                return (True, result_state)
            else:
                return (False, "Not enabled")           
        
        if VM:
            with open('/opt/stackstorm/packs/service_remediations_pack/actions/service_data.json') as file:
                service_data = json.load(file)
            host = message.split()[0]
            vm = service_data[host]['VM']
            vm_status = vm_remed(vm, False)
            if vm_status:
                return (True, service_data[host]['host'])
            else:
                return (False, "deadman-host={} status CRITICAL".format(host))


        return (False, "False message")

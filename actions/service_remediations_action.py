import json
from functions import send_service_command
from datetime import datetime
from pytz import timezone
tz = timezone("America/Buenos_Aires")

from st2common.runners.base_action import Action

class ServiceRemediationsAction(Action):
    def run(self, message):
        try:
            with open('/opt/stackstorm/packs/service_remediations_pack/actions/service_data.json') as file:
                service_data = json.load(file)
            io_rule = service_data['Commands']['IO_rule']["service"]
            remote = service_data['Commands']['remote']
            
            host = message.split()[0]
            service = message.split()[2]

            if host in service_data and int(message[-1]) not in (1,2):
                with open("/opt/stackstorm/packs/service_remediations_pack/actions/logs.txt", "a") as f:
                    f.write("{} | {}\n".format(tz.localize(datetime.now()).strftime("%D-%H:%M:%S"), message))
                send_service_command(remote, io_rule, service, host, message, service_data)
                return (True, "Success")

            return (False, "Message doesn't match")
        
        except IOError:
            return (False, "File not accessible")
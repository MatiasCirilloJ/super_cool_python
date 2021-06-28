import json
from functions import send_docker_command
from datetime import datetime
from pytz import timezone
tz = timezone("America/Buenos_Aires")

from st2common.runners.base_action import Action

class DockerRemediationsAction(Action):
    def run(self, message):
        try:
            with open('/opt/stackstorm/packs/service_remediations_pack/actions/service_data.json') as file:
                service_data = json.load(file)

            host = message.split()[0]

            if host in service_data and 'cmd' in service_data[host] and int(message[-1]) != 0:
                #with open("/opt/stackstorm/packs/service_remediations_pack/actions/logs.txt", "a") as f:
                #    f.write("{} | {}\n".format(tz.localize(datetime.now()).strftime("%D-%H:%M:%S"), message))
                io_rule = service_data['Commands']['IO_rule']["docker"]
                remote = service_data['Commands']['remote']

                send_docker_command(remote, io_rule, host, message, service_data)
                return (True, "Success")

            return (False, "Message doesn't match")

        except IOError:
            return (False, "File not accessible")
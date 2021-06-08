from st2common.runners.base_action import Action

class HelloStackStorm(Action):
    def run(self, name2):
        print(name2 + " | Funca")
        return (True)

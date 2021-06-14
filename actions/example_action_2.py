from st2common.runners.base_action import Action

class HelloStackStorm(Action):
    def run(self, name2, key = False):
        print(name2)
        if key:
            return (True)
        return (True)

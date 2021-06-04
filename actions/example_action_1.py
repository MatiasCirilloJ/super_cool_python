from st2common.runners.base_action import Action

class HelloStackStorm(Action):
    def run(self, name):
        print(name)
        resultado = ("res1", "res2")
        return (True, resultado)

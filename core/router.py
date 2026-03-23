class Router:
    def __init__(self):
        self.agents = {}

    def add_agent(self, name, agent):
        self.agents[name] = agent

    def run(self, name, input_data=None):
        if name not in self.agents:
            raise ValueError(f"Agent '{name}' not found")
        return self.agents[name].run(input_data)

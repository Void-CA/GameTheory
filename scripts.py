import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Agent:
    def __init__(self, behavior: str) -> None:
        self.behavior = behavior
        self.states = []
        self.last_state = None
        self.rencoroso_flag = True

    def get_state(self, state=1):
        if self.behavior == "peaceful":
            self.states.append(1)
        elif self.behavior == "aggressive":
            self.states.append(0)
        elif self.behavior == "tft":
            self.get_state_tft(state)
        elif self.behavior == "rencoroso":
            self.get_state_rencoroso(state)
        elif self.behavior == "randomboy":
            self.get_state_randomboy()
        else:
            NameError("Agent behavior not available")
        self.last_state = self.states[-1]
    
    def get_state_tft(self, state):
        self.states.append(1 if state > 0 else 0)
    
    def get_state_rencoroso(self, state):
        if state < 1:
            self.rencoroso_flag = False
        self.states.append(int(self.rencoroso_flag))
    
    def get_state_randomboy(self):
        self.states.append(random.randint(0,1))



class Match:
    def __init__(self, agents: list) -> None:
        self.x = Agent(agents[0])
        self.y = Agent(agents[1])
        self.agent_names = agents


    def run(self, iterations: int = 10):
        self.x.get_state()
        for _ in range(iterations):
            self.y.get_state(self.x.last_state)
            self.x.get_state(self.y.last_state)
        self.y.get_state()
        return self.x.states, self.y.states
    
    def show(self, iterations=10):
        results = np.array(self.run(iterations=iterations))
        plt.figure(figsize=(10, 2))
        sns.heatmap(results, cmap="coolwarm", annot=True, cbar=False, linewidths=.5)
        plt.xlabel("Iterations")
        plt.ylabel("Agents")
        plt.yticks([0.5, 1.5], self.agent_names, rotation=0)
        plt.title("Simulation Heatmap")
        plt.show()


class Tournament:
    def __init__(self, single_agent:str, multiple_agents:list):
        self.x = single_agent
        self.ys = multiple_agents

matchs = Match(["tft", "aggressive"])
matchs.show()
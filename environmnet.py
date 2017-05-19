import gym
import cv2

class Environment:
    def __init__(self, parameter_list):
        
        self.gym = gym.make(parameter_list.game) # inicializa o gym, responsável por admistrar nosso aprendizado
        self.displayTesting = params.displayTesting # decide se deve mostrar um display do processo
        self.displayResult = params.displayResult
        self.terminal = False
        self.dimensions = (params.height, params.width)
        self.currentObservation = None
        
        # variáveis relativas ao gym
        self.metadata = self.gym.metadata
        self.action_space = self.gym.action_space.n
        self.observation_space = self.gym.observation_space
        self.reward_range = self.gym.reward_range
        self.spec = self.gym.spec

    def actions(self):
        return self.action_space

    def restart(self):
        self.currentObservation = self.gym.reset()
        self.terminal = False

    def act(self, action):
        if self.displayTesting:
            self.gym.render()
        # dar um jeito de só trocar essa variável após completar o treino
        if self.displayResult:
            self.gym.render()
        self.currentObservation, reward, self.terminal, info = self.gym.step(action)
        if self.terminal:
            self.gym.reset()
        return reward

    def getScreen(self):
        return cv2.resize(cv2.cvtColor(self.currentObservation, cv2.COLOR_RGB2GRAY), self.dimensions)

    def isTerminal(self):
        return self.terminal
        
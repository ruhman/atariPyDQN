import gym
import cv2

class Environment:
    def __init__(self, parameter_list):
        
        self.gym = gym.make(parameter_list.game) # inicializa o gym, responsavel por admistrar nosso aprendizado
        self.displayTesting = parameter_list.displayTesting # decide se deve mostrar um display do processo
        self.displayResult = parameter_list.displayResult
        self.terminal = False
        self.dimensions = (parameter_list.height, parameter_list.width)
        self.currentObservation = None
        
        # variaveis relativas ao gym
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
        # dar um jeito de so trocar essa variavel apos completar o treino
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
        
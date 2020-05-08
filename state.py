import math
import random
from action import Action

REWARD = 1.0
DISCOUNT = 1.0
EXPLORATION_VALUE = 0.3

class State:

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.utility = 0
        self.prob = 0.
        self.result_states = list()
        self.actions = list()
        self.utility_map = dict()
        self.policy = None

    def set_utility(self,):
        min_action = None
        min_value = math.inf
        for k, v in self.utility_map.items():
            if v < min_value:
                min_value = v
                min_action = k
        # assert min_action is not None
        if min_action is None:
            return
        self.utility = min_value
        self.policy = min_action.get_name()

    def get_prob(self):
        return self.prob
    
    def set_prob(self, val):
        self.prob = val

    def get_name(self):
        return self.name
    
    def get_actions(self):
        return self.actions

    def get_policy(self):
        return self.policy
    
    def get_utility(self):
        return self.utility

    def add_state(self, state):
        self.result_states.append(state)

    def add_action(self, name):
        self.actions.append(Action(name))

    def get_action(self, name):
        for action in self.actions:
            if name == action.get_name():
                return action
        return None

    def check_action(self, name):
        if len(self.actions) == 0: return True
        return name not in self.actions

    def choose_action(self,):
        if len(self.actions) == 0: return None
        rand_index = random.randint(0, len(self.actions)-1)
        return self.actions[rand_index]

    def choose_action_greedyq(self,):
        randval = random.random()
        if randval < EXPLORATION_VALUE:
            return self.choose_action()
        else:
            minval = math.inf
            for action in self.actions:
                if action.get_f_value < minval:
                    return action
        return self.choose_action()

    def update_utility(self,):
        for action in self.actions:
            sumup = 0
            for act_state in action.get_action_states():
                sumup += act_state.get_state().get_utility() * act_state.get_prob()
            val = REWARD + DISCOUNT * sumup
            self.utility_map[action] = val
        self.set_utility()

    def update_prob(self,):
        for action in self.actions:
            action.update_prob()

    def __str__(self):
        return self.name

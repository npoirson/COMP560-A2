import random
from random import shuffle
from action_state import ActionState

DISCOUNT = 0.9
ALPHA = 0.2
REWARD = 1.0
EXPLORATION_VALUE = 0.2

class Action:
    
    def __init__(self, name):
        self.name = name
        self.action_states = list()
        self.scores = list()
        self.count = 0
        self.function_val = 0
        self.result_prob = 0.
        self.result_action_state = None

    def get_name(self,):
        return self.name
    
    def get_action_states(self):
        return self.action_states

    def add_pair(self, state, prob, count):
        new_as = ActionState(state, prob, count)
        self.action_states.append(new_as)

    def print_pairs(self,):
        for act_state in self.action_states:
            print(act_state)

    def get_f_value(self):
        return self.function_val
    
    def update_f_value(self, action):
        fval = action.get_f_value() + ALPHA*(
            REWARD + DISCOUNT*self.function_val - action.get_f_value())
        self.function_val = fval

    def update_prob(self):
        for act_state in self.action_states:
            act_state.update_prob(self.count)
    
    def get_result_prob(self):
        return self.result_prob
    
    def update_count(self):
        self.count += 1
    
    def set_result_action_state(self, act_state):
        self.result_action_state = act_state

    def update_result_action_state(self):
        self.result_action_state.add_to_count()

    def random_result_state(self,):
        randindex = random.randint(0, len(self.action_states)-1)
        return self.action_states[randindex].get_state()

    def sample_result_state(self):
        randval = random.random()
        if len(self.action_states) == 0: return None
        if randval < EXPLORATION_VALUE:
            randindex = random.randint(0, len(self.action_states)-1)
            self.result_prob = self.action_states[randindex].get_prob()
            self.set_result_action_state(self.action_states[randindex])
            return self.action_states[randindex].get_state()
        else:
            tot_prob = 0.
            shuffle(self.action_states)
            for act_state in self.action_states:
                tot_prob += act_state.get_prob()
                if randval <= tot_prob:
                    self.result_prob = act_state.get_prob()
                    self.set_result_action_state(act_state)
                    return act_state.get_state()
        return None

    def __str__(self):
        return self.name

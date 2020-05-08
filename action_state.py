import math
import random

class ActionState:

    def __init__(self, state, probability, count):
        self.state = state
        self.probability = probability
        self.count = count

    def get_prob(self):
        return self.probability
    
    def get_count(self):
        return self.count
    
    def get_state(self):
        return self.state
    
    def add_to_count(self):
        self.count += 1

    def __str__(self):
        out = '{}, Prob: {:.2f}, Count: {}'.format(self.state.get_name(),
                                                   self.probability, self.count)
        return out

    def update_prob(self, total_count):
        self.probability = 0. if total_count == 0 else self.count / total_count
        print('Count: {}, Total: {}'.format(self.count, total_count))

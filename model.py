

class Model:
    
    def __init__(self, states):
        self.states = states

    def fit_model(self):
        for iteration in range(1, 60001):
            print('ITERATION: {}'.format(iteration))

            state = self.get_state('Fairway')
            action = None

            while state.get_name() != 'In':
                start_state_name = state.get_name()
                temp_state = None
                while temp_state is None:
                    action = state.choose_action()
                    if action is None: continue
                    temp_state = action.sample_result_state()

                action.update_count()
                action.update_result_action_state()
                state = temp_state
                print('{}/{}/{}/{}'.format(start_state_name,
                                            action.get_name(),
                                            state.get_name(),
                                            action.get_result_prob()))
            print('Lets make it in the hole!: {}'.format(state.get_name()))
            if iteration % 500 == 0:
                print('RECALCULATING')
                self.update_all_probs()
            
            self.update_all_utilities()
            print('')
        
        print('///////////////////////////////////////')
        # print all probs
        for state in self.states:
            print(state.get_name())
            print('////////////')
            for action in state.get_actions():
                print(action.get_name())
                print('Action: {} has these value pairs'.format(action.get_name()))
                action.print_pairs()
            print('////////////')

        print('')
        print('FINAL RESULTS: ')
        # print final results
        print('////////////')
        for state in self.states:
            state.update_utility()
            print('State: {}, Utility: {:.2f}, Policy: {}'.format(
                state.get_name(),
                state.get_utility(),
                state.get_policy()
            ))
        print('////////////')

    def update_all_probs(self):
        for state in self.states:
            state.update_prob()
    
    def update_all_utilities(self):
        for state in self.states:
            state.update_utility()
    
    def get_state(self, name):
        for state in self.states:
            if state.get_name() == name:
                return state
        return None

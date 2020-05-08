from state import State
from model import Model

def parse_inputs():
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [l[:-2] for l in lines[:-1]] + [lines[-1]]
    lines[-1] = lines[-1][:-1]
    inputs = [l.split('/') for l in lines]
    return inputs

def get_state(states, name):
    for state in states:
        if state.get_name() == name:
            return state

def main():
    inputs = parse_inputs()
    state_names = list()
    states = list()
    for (state, action, result, prob) in inputs:
        if state not in state_names:
            state_names.append(state)
            temp_state = State(state)
            states.append(temp_state)

    for (state, action, result, prob) in inputs:
        if result not in state_names:
            state_names.append(result)
            temp_state = State(result)
            states.append(temp_state)
        elif get_state(states, state).check_action(action):
            get_state(states, state).add_action(action)

        act_states = get_state(states, state).get_action(action).get_action_states()
        state_act_states = [a.get_state() for a in act_states]
        if (get_state(states, result) not in 
            state_act_states):
            cur_action = get_state(states, state).get_action(action)
            res = get_state(states, result)
            cur_action.add_pair(res, float(prob), 0)
    
    model = Model(states)
    model.fit_model()
    print('////////////////////////')
    # model.fit_model_free()


if __name__ == "__main__":
    main()
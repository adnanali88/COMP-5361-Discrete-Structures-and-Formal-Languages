import os
os.environ["PATH"] += os.pathsep + 'D:\Program Files\Graphviz\bin'

from PySimpleAutomata import NFA, DFA, automata_IO

# nfa_example = {
#     'alphabet': {'0', '1'},
#     'states': {'q0', 'q1', 'q2'},
#     'initial_states': {'q0'},
#     'accepting_states': {'q2'},
#     'transitions': {
#         ('q0', '0'): {'q0','q1'},
#         ('q0', '1'): {'q0'},
#         ('q1', '1'): {'q2'}
#     }
# }

def create_nfa():
    user_alphabtes = input("Please enter the ALPHABETS (split the alphabets by a comma): ")
    array_alphabtes = user_alphabtes.split(',')
    user_states = input("Please enter the States (split the States by a comma): ")
    array_states = user_states.split(',')
    user_initial_states = input("What is/are the initial state(s)? Split by a comma if more than one: ")
    array_initial_states = user_initial_states.split(',')
    user_accepting_states = input("What is/are the accepting state(s)? Split by a comma: ")
    array_accepting_states = user_accepting_states.split(',')
    set_transitions = {}
    user_transition = "init"
    while(user_transition!=""):
        user_transition = input("Please enter transitions one at a time and press Enter: ")
        array_transition = user_transition.split(',')
        if(len(array_transition) == 3):
            if((array_transition[0], array_transition[1]) in set_transitions):
                set_transitions[array_transition[0], array_transition[1]].add(array_transition[2])
            else:
                set_transitions[array_transition[0], array_transition[1]] = set()
                set_transitions[array_transition[0], array_transition[1]].add(array_transition[2])
    nfa = {
        'alphabet': set(array_alphabtes),
        'states': set(array_states),
        'initial_states': set(array_initial_states),
        'accepting_states': set(array_accepting_states),
        'transitions': set_transitions
    }
    print(nfa)
    return nfa



def nfa_convert(nfa: dict):

    dfa = {
        'alphabet': nfa['alphabet'].copy(),
        'initial_state': None,
        'states': set(),
        'accepting_states': set(),
        'transitions': dict()
    }

    if len(nfa['initial_states']) > 0:
        dfa['initial_state'] = str(set(sorted(nfa['initial_states'])))
        dfa['states'].add(str(set(sorted(nfa['initial_states']))))

    states_in_set = list()
    sets_in_row = list()
    sets_in_row.append(nfa['initial_states'])
    states_in_set.append(nfa['initial_states'])
    if len(states_in_set[0].intersection(nfa['accepting_states'])) > 0:
        dfa['accepting_states'].add(str(set(sorted(states_in_set[0]))))

    while sets_in_row:
        curr = sets_in_row.pop(0)
        for a in dfa['alphabet']:
            next_set = set()
            for state in curr:
                if (state, a) in nfa['transitions']:
                    for next_state in nfa['transitions'][state, a]:
                        next_set.add(next_state)
            if len(next_set) == 0:
                continue
            if next_set not in states_in_set:
                states_in_set.append(next_set)
                sets_in_row.append(next_set)
                dfa['states'].add(str(set(sorted(next_set))))
                if next_set.intersection(nfa['accepting_states']):
                    dfa['accepting_states'].add(str(set(sorted(next_set))))

            dfa['transitions'][str(set(sorted(curr))), a] = str(set(sorted(next_set)))

    return dfa

nfa = create_nfa()
dfa = nfa_convert(nfa)

for key, value in dfa["transitions"].items():
    print(key[0] + "   " + key[1] + "   " + value)

automata_IO.dfa_to_dot(dfa, 'h_dfa_convert', './part2')

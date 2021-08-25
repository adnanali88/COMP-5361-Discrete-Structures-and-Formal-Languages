import os
os.environ["PATH"] += os.pathsep + 'D:\Program Files\Graphviz\bin'

from PySimpleAutomata import automata_IO

# Getting a DFA from the user
def get_dfa_from_user():
    alphabet_input = input("Please enter the ALPHABETS (split the alphabets by a comma): ")
    alphabets = set(alphabet_input.split(","))
    states_input = input("Please enter the States (split the States by a comma): ")
    states = set(states_input.split(","))
    initial_state = input("What is the initial state: ")
    accepting_states_input = input("What is/are the accepting state(s)? Split by a comma: ")
    accepting_states = accepting_states_input.split(",")

    # Transitions input
    transitions = {}
    transition_input = " "
    while transition_input != "":
        transition_input = input("Please enter transitions one at a time and press Enter: ")
        if transition_input != "":
          transition_user = transition_input.split(",")
          transitions[(transition_user[0], transition_user[1])] = transition_user[2]

    dfa = {
        "alphabet": alphabets,
        "states": states,
        "initial_state": initial_state,
        "accepting_states": accepting_states,
        "transitions": transitions
    }
    return dfa

def get_nfa_from_user():
    alphabet_input = input("Please enter the ALPHABETS (split the alphabets by a comma): ")
    alphabets = set(alphabet_input.split(","))
    states_input = input("Please enter the States (split the States by a comma): ")
    states = set(states_input.split(","))
    initial_state = input("What is/are the initial state(s)? Split by a comma if more than one: ")
    accepting_states_input = input("What is/are the accepting state(s)? Split by a comma: ")
    accepting_states = accepting_states_input.split(",")

    transitions = {}
    transition_input = " "
    while transition_input != "":
        transition_input = input("Please enter transitions one at a time and press Enter: ")
        if transition_input != "":
          transition_user = transition_input.split(",")

          if ((transition_user[0], transition_user[1]) in transitions):
              transitions[(transition_user[0], transition_user[1])].add(transition_user[2])
          else:
              transitions[(transition_user[0], transition_user[1])] = set()
              transitions[(transition_user[0], transition_user[1])].add(transition_user[2])

    nfa = {
        "alphabet": alphabets,
        "states": states,
        "initial_states": initial_state,
        "accepting_states": accepting_states,
        "transitions": transitions
    }

    return nfa


automata_type = input("Please specify: For DFA enter 1, for NFA enter 2: ")
if (automata_type == "1"):
    dfa = get_dfa_from_user()
    automata_IO.dfa_to_dot(dfa, "dfa", "./results")
elif (automata_type == "2"):
    nfa = get_nfa_from_user()
    automata_IO.nfa_to_dot(nfa, "nfa", "./results")

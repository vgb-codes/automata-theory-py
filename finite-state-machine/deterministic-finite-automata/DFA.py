"""Deterministic Finite State Machine"""

class DFA:

    def __init__(self):
        """Initialize DFSM object"""
        self.Q = self.populate_states()
        self.SIGMA = self.populate_alphabet()
        self.DELTA = self.populate_transition_function()
        self.START_STATE, self.ACCEPT_STATES = self.set_start_accept()
        self.CURRENT_STATE = None

    def set_start_accept(self):
        """Takes user input for START_STATE and ACCEPT_STATE, and checks if it's a valid state (if it belongs to Q)"""
        while(True):
            start = input("Enter the START_STATE: ")
            accept = input("Enter the ACCEPT_STATES: ").split()
            #Making sure that start and accept are both in Q and that start and accept are not the state
            if (start in self.Q) and (set(accept).issubset(set(self.Q))):
                return start, accept
            else:
                print("Please enter STATE_STATE and ACCEPT_STATES that are in Q : {}.\nAccept states should be a valid subset of Q\n".format(self.Q))

    def populate_states(self):
        """Takes user input for states (Q)"""
        Q_input = input("Enter list of states separated by spaces: ").split()
        print("STATES : {}".format(Q_input))
        return Q_input
    
    def populate_alphabet(self):
        """Takes user input for alphabet/symbols (SIGMA)"""
        SIGMA_input = input("Enter input alphabet separated by spaces: ").split()
        print("ALPHABET : {}".format(SIGMA_input))
        return SIGMA_input

    def populate_transition_function(self):
        """Creates the transition function (Q X SIGMA -> Q) and prints it out"""
        transition_dict = {el : {el_2 : 'REJECT' for el_2 in self.SIGMA} for el in self.Q}

        for key, dict_value in transition_dict.items():
            print("Enter transitions for state {}. If required, use 'REJECT'.".format(key))

            for input_alphabet, transition_state in dict_value.items():
                transition_dict[key][input_alphabet] = input("CURRENT STATE : {}\tINPUT ALPHABET : {}\tNEXT STATE : ".format(key, input_alphabet))
        
        print("\nTRANSITION FUNCTION Q X SIGMA -> Q")
        print("CURRENT STATE\tINPUT ALPHABET\tNEXT STATE")
        for key, dict_value in transition_dict.items():
            for input_alphabet, transition_state in dict_value.items():
                print("{}\t\t{}\t\t{}".format(key, input_alphabet, transition_state))

        return transition_dict

    def run_state_transition(self, input_symbol):
        """Takes in current state and goes to next state based on input symbol."""
        if (self.CURRENT_STATE == 'REJECT'):
            return False
        print("CURRENT STATE : {}\tINPUT SYMBOL : {}\t NEXT STATE : {}".format(self.CURRENT_STATE, input_symbol, self.DELTA[self.CURRENT_STATE][input_symbol]))
        self.CURRENT_STATE = self.DELTA[self.CURRENT_STATE][input_symbol]
        return self.CURRENT_STATE
        
    def check_if_accept(self):
        """Checks if the current state is one of the accept states."""
        if self.CURRENT_STATE in self.ACCEPT_STATES:
            return True
        else:
            return False

    def run_machine(self, in_string):
        """Run the machine on input string"""
        self.CURRENT_STATE = self.START_STATE
        for ele in in_string:
            check_state = self.run_state_transition(ele)
            #Check if new state is not REJECT
            if (check_state == 'REJECT'):
                return False
        return self.check_if_accept()

if __name__ == "__main__":
    check = True
    print("\nDeterministic Finite State Machine.")
    machine = DFA()
    while(check):
        choice = int(input("\nEnter Choice:\n1. Replace DFSM\n2. Run DFSM on input string\nEnter choice : "))
        if (choice == 1):
            machine = DFA()
        elif (choice == 2):
            input_string = list(input("Enter the input string : "))
            print("ACCEPTED" if machine.run_machine(input_string) else "REJECTED")
        else:
            check = False

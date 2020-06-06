# Deterministic Finite Automata (DFA)

DFA M is a 5-tuple consisting of (Q, SIGMA, RHO, START_STATE, ACCEPT_STATES)

1. Finite set of states Q
2. Finite set of input symbols called alphabet SIGMA
3. Transition Function DELTA: Q X E -> Q
4. An initial or START_STATE
5. A set of ACCEPT_STATES

[Wikipedia]

### Example: Create a DFA that accepts set of all strings over {0,1} which are binary numbers divisible by 3.

### Creation of DFA
```
$ py DFA.py
Deterministic Finite State Machine.
Enter list of states separated by spaces: q0 q1 q2
STATES : ['q0', 'q1', 'q2']
Enter input alphabet separated by spaces: 0 1
ALPHABET : ['0', '1']
Enter transitions for state q0. If required, use 'REJECT'.
CURRENT STATE : q0      INPUT ALPHABET : 0      NEXT STATE : q0
CURRENT STATE : q0      INPUT ALPHABET : 1      NEXT STATE : q1
Enter transitions for state q1. If required, use 'REJECT'.
CURRENT STATE : q1      INPUT ALPHABET : 0      NEXT STATE : q2
CURRENT STATE : q1      INPUT ALPHABET : 1      NEXT STATE : q0
Enter transitions for state q2. If required, use 'REJECT'.
CURRENT STATE : q2      INPUT ALPHABET : 0      NEXT STATE : q1
CURRENT STATE : q2      INPUT ALPHABET : 1      NEXT STATE : q2

TRANSITION FUNCTION Q X SIGMA -> Q
CURRENT STATE   INPUT ALPHABET  NEXT STATE
q0              0               q0
q0              1               q1
q1              0               q2
q1              1               q0
q2              0               q1
q2              1               q2
Enter the START_STATE: q0
Enter the ACCEPT_STATES: q0
```

### Test String '0' [0]

```
Enter Choice:
1. Replace DFSM
2. Run DFSM on input string
Enter choice : 2
Enter the input string : 0
CURRENT STATE : q0      INPUT SYMBOL : 0         NEXT STATE : q0
ACCEPTED
```
### Test String '110' [6]

```
Enter Choice:
1. Replace DFSM
2. Run DFSM on input string
Enter choice : 2
Enter the input string : 110
CURRENT STATE : q0      INPUT SYMBOL : 1         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 1         NEXT STATE : q0
CURRENT STATE : q0      INPUT SYMBOL : 0         NEXT STATE : q0
ACCEPTED
```

### Test String '10100' [20]

```
Enter Choice:
1. Replace DFSM
2. Run DFSM on input string
Enter choice : 2
Enter the input string : 10100
CURRENT STATE : q0      INPUT SYMBOL : 1         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 0         NEXT STATE : q2
CURRENT STATE : q2      INPUT SYMBOL : 1         NEXT STATE : q2
CURRENT STATE : q2      INPUT SYMBOL : 0         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 0         NEXT STATE : q2
REJECTED
```

### Test String '100001111' [271]

```
Enter Choice:
1. Replace DFSM
2. Run DFSM on input string
Enter choice : 2
Enter the input string : 100001111
CURRENT STATE : q0      INPUT SYMBOL : 1         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 0         NEXT STATE : q2
CURRENT STATE : q2      INPUT SYMBOL : 0         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 0         NEXT STATE : q2
CURRENT STATE : q2      INPUT SYMBOL : 0         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 1         NEXT STATE : q0
CURRENT STATE : q0      INPUT SYMBOL : 1         NEXT STATE : q1
CURRENT STATE : q1      INPUT SYMBOL : 1         NEXT STATE : q0
CURRENT STATE : q0      INPUT SYMBOL : 1         NEXT STATE : q1
REJECTED
```

[Wikipedia]: https://en.wikipedia.org/wiki/Deterministic_finite_automaton

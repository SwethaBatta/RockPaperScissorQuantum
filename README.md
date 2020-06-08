# RockPaperScissorQuantum
Built a version of RockPaperScissor game using quantum superposition property

## Steps to execute
```
To run the application via command line from cloned repository
> python RockPaperScissors.py

To run the unit tests via command line from cloned repository
> python -m unittest -v unitTests.py
```

## Game rules
```
This is a game of Rock, Paper, Scissors played by user against the computer.

Rules: You and the computer both choose rock, paper or scissors. The winner is decided by these rules:
Rock blunts scissors
Paper covers rock
Scissors cuts paper
```

## Process description
```
- The project uses the quantum computing property - "Superposition" (the idea that a quantum object can exist in multiple states at the same time) for generating a random output which is used for computer's turn in the game.

- The user's input is collected by a UI widget.

- Trick case: 
  If the user tries to play/win using the same input consecutively more than 3 times, the computer also mimics the user's input creating a dead-end until the user changes his input
 
 - This feature can find use when in industries where an automated bot/hacker tries to retrieve or win a game by repeatedly using the input which worked previously. 
 
 - The idea to implement this feature came from learning about the quantum property "Entanglement" (a special state of strong correlation between two qubits even when the qubits are physically separated from each other by great distances. The correlation is so strong that the qubits appear to be communicating faster than the speed of light). 
 
- Whenever the system detects that the user's input might need scrutiny, the user's input and system's response to the user can be entangled. They can remain in entangled state until the user activity returns to normal state.

- I would like to know if the above use-case can make use of entanglement property. 
```



## References
```
https://towardsdatascience.com/building-your-own-quantum-circuits-in-python-e9031b548fa7

https://www.pythonistaplanet.com/rock-paper-scissors-game-using-python-tkinter/
```

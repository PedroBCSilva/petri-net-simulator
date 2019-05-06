# PetriNet
Group: Gabriel Colling, Pedro Bohlmann Cascaes Silva, Jaqueline Dahmer Steffenon

How to run:
```
    python3 main.py
```
The default file to load data from is input.txt but it can be changed by sending a parameter:
```
    python3 main.py --file path
```
# Input pattern
* Create a new place:
```
    new_place place_name quantity_of_marks is_start_place

    new_place A 0 True
    new_place B 10 False
```
* Create a new transition:
```
    new_transition transition_name

    new_transition T1
```
* Create a new arc:
```
    new_arc arc_name place_name transition_name arc_type cost

    new_arc ARC1 A T1 arc_in 1
    new_arc ARC2 B T1 arc_out 1
```
The idea behind arc_type is to set if the marks inside the place are to be consumed a result from a transition

# Dependencies
* PrettyTable 7
* colorama 0.4.1

# The Monty Hall README file

## Introduction
The Monty Hall problem is loosely based on the game show *Let's Make a Deal.*
The problem is simple: given a set of three doors (behind which there is just
one prize), you select a door. The host then reveals one of the remaining two doors, leaving just your door and the unopened door. Then you are given the
option of switching doors and the game ends and all doors are open.

This program uses a Monte Carlo simulation to run through many iterations of
the game to provide proof that the best strategy is to always switch to doors.

## Input
There program runs from the command line, and there are only two options to
enter values. The first request is whether the computer will simulate a
strategy of always keeping its choice (the input value of 0) or always changing
its door choice when asked (the input value of 1). The simulation will only
accept a return of 0 or 1. Any other value will simply cause the prompt to
repeat until the user provides 0 or 1.

The next user prompt is for a number of trials to run. The user must input an
integer, and the integer must be 1 or greater. Any other value will cause the
computer to continue requesting input until a valid integer is returned. The
simulation works best when the value is sufficiently large. For three doors, a
small value (less than 20) occasionally gives contradictory results.

## Extension
The program is can be modified to more doors. There is an internal variable
called at the beginning of the game that sets the total number of doors.
Changing this value can demonstrates the diminishing return for switching as
the number of choices grows.

## Additions
Included with the base program is a suite of tests, in a file 'monty_hall_test.py' that check the operation of functions with the main simulation file. This test program is strictly used for debugging purposes and should not be considered part of the program.

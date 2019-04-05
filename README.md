# stima-4gamesolver

An application made with Python to input four numbers and put mathematical operators to equal (or nearing) 24.
Done to fulfill IF2211 Algorithm Strategies's Big Mission (or whatever Tugas Besar is called).

**Strategy:**
* Sort the array of 4 numbers descendingly.
* Find which operator has the local maxima score.
* [Local maxima is defined as: 1) getting as close as possible to 24, 2) use the best operator possible.]
* Also check for parentheses combinations: `AB@C`, `(AB)@C`, `A(B@C)`.

## Installation and Running
* Make sure that Python 3.7.0 is already installed on your computer.
* To test the program, execute:
``` bash
stima-4gamesolver> python test.py
```
* To run the program using file handling, execute:
``` bash
stima-4gamesolver> python front2.py in.txt out.txt
```
* To run the frontend GUI, make sure that you have already installed Pygame or execute:
``` bash
stima-4gamesolver> pip install pygame
```
* Then run:
``` bash
stima-4gamesolver> python front1.py
```

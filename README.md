# Beyond-Basic-Calculator-
A Python-based Calculator Program that performs basic arithmetic as well as determining GCF, LCM and basic statistical methods of data classification.

---

## Features
- Performs addition, subtraction, multiplication, division, and exponentiation.
- Determines the Greatest Common Factor and Least Common Multiple of two numbers.
- Computes basic measures of spread for a dataset (min, max, range, mean, median, standard deviation, mode).
- Simple console-based interface.
- Capable of saving past calculations to an external file, with history deletion after 25 calculations.

---

## Installation 
1. Clone the repository:
```bash
git clone https://github.com/1106-Guillebeau-Georgia/Beyond-Basic-Calculator-.git
```

---

## Usage
After cloning the repository run it from the console:
```bash
python3 calc.py
```

Example Output:
```
What operation would you like to compute (+, -, *, /, ^, GCF, LCM, STATS, H to view calculation history, X to Quit): H


The greatest common factor of 65 and 101 is 1


The greatest common factor of 65 and 130 is 65


4 ^ 7 = 16384


5 ^ 8 = 390625


The greatest common factor of 8 and 88 is 8


2 ^ 5 = 32


The least common multiple of 24 and 6 is 72


[1.0, 2.0, 3.0, 4.0]
The statistics for your data set are: 
Minimum: 1
Maximum: 4
Range: 3
Mean: 2.5
Median: 2.5
Standard Deviation: 1.2909944487358056
This data set has no mode, each value appears once.


Continue calculating? Y


What operation would you like to compute (+, -, *, /, ^, GCF, LCM, STATS, H to view calculation history, X to Quit): ^

Enter 2 numbers separated by a space: 4 6

4 ^ 6 = 4096

Continue calculating? N
```

---

## Technologies
- Python 3
- Standard Libraries (math, statistics, etc.)

---

## Notes
- This program saves calculation history to an external file (`calcs.txt`), this file is included in the repository.  
- **You must either download the given file or create `calcs.txt` in the same directory as `calc.py` and input 0 in the first line of the file before running the program.**  
- History is deleted after 25 calculations to limit file size.
  
---

## About
Created by Georgia Guillebeau — Computer Science & Engineering student at UNR.
[LinkedIn](https://www.linkedin.com/in/georgia-guillebeau-3b3636285)

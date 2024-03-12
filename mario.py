import numpy as np
import sys
from handwriting_synthesis import Hand

Test1 = sys.argv[1]
Test2 = sys.argv[2]
Test3 = sys.argv[3]

print (Test1 + Test2 + Test3)

all_star = """Hier steht das erste Argv : """ + Test1 + """
Hier steht das zweite Argv : """ + Test2 + """
Hier steht das dritte Argv : """ + Test3

if __name__ == '__main__':
    hand = Hand()

    # demo number 1 - fixed bias, fixed style
    lines = all_star.split("\n")
    biases = [.75 for i in lines]
    styles = [12 for i in lines]

    hand.write(
        filename='img/mario.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )

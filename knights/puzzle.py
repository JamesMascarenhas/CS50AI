from logic import *
'''
Declaring all knights and knaves needed for puzzles
'''
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

'''
Creating an general knowledge base that will be used for each puzzle
Any additional information for individual puzzles will be added in additionally
'''
general_knowledge_base =  And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)


'''
Puzzle 0
A says "I am both a knight and a knave"
Uses general knowledge base where A can either be a Knight or a Knave but not both
The first implication states that if A is a knight then their statement must be true
The second implication states that if A is a knave then their statement must be false
Since we know A can't be a Knight and a Knave then in this case A must be a Knave
'''
knowledge0 = And(
    general_knowledge_base,
    Biconditional(AKnight, And(AKnight, AKnave))
)


'''
Puzzle 1
A says "We are both knaves
B says nothing
Since we know that a knight cannot say it's a knave A is knave, but since it's a knave it must be lying so B must be a knight
'''
knowledge1 = And(
    general_knowledge_base,
    Biconditional(AKnight, And(AKnave, BKnave))
)


'''
Puzzle 2
A says "We are the same kind"
B says "We are of different kinds"
Since either A or B must be lying (contradictory sentences) one must be a knave, since A says they are the same kind it's the knave, and B is the knight
'''
knowledge2 = And(
    general_knowledge_base,
    Biconditional(AKnight, Biconditional(AKnight, BKnight)),
    Biconditional(BKnight, Not(Biconditional(AKnight, BKnight)))
)


'''
Puzzle 3
A says either "I am a knight." or "I am a knave.", but you don't know which.
B says "A said 'I am a knave'."
B says "C is a knave."
C says "A is a knight."
'''

knowledge3 = And(
    general_knowledge_base,
    # A can either say that it is a knight or a knave
    Or(Biconditional(AKnight, AKnight), Biconditional(AKnight, AKnave)),
    # If B is a knight then A said that it is a knave
    Implication(BKnight, Biconditional(AKnight, AKnave)),
    # If B is a knight then C is a knave, but if B is a knave then C is a knight
    Biconditional(BKnight, CKnave),
    # If C is a knight then A is a knight
    Implication(CKnight, AKnight)
)



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

# CS50AI Projects
All project's through HarvardX's CS50 Introduction to Artificial Intelligence with Python Course

# 0.1 degrees
### Description
- This program determines how many "degrees of separation" apart two actors are
### Background
- According to the Six Degrees of Kevin Bacon game, anyone in the Hollywood film industry can
  be connected to Kevin Bacon within six steps, where each step consists of finding a film that
  two actors both starred in
- In this problem, we’re interested in finding the shortest path between any two actors by
  choosing a sequence of movies that connects them. For example, the shortest path between
  Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by
  both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both
  starring in “Apollo 13.”
- We can frame this as a search problem: our states are people. Our actions are movies, which
  take us from one actor to another (it’s true that a movie could take us to multiple different
  actors, but that’s okay for this problem). Our initial state and goal state are defined by
  the two people we’re trying to connect. By using breadth-first search, we can find the
  shortest path from one actor to another.

# 0.2 tictactoe
### Description
- This program implements an AI using Minimax to play Tic-Tac-Toe optimally
### Background
- Minimax is a kind of backtracking (recursive) algorithm that is used in decision making and
  game theory to find the optimal move for a player, assuming that your opponent
  also plays optimally
- This algorithm works well with two player deterministic games such as tic-tac-    toe or chess
- It works by minimzing the possible loss for a worst case scenario

# 1.1 knights
### Description
- This program is meant to solve the "Knights and Knaves puzzle" from the book of logical puzzles published by Raymond Smullyan in 1978 called "What is the name of this book?" by using model checking and knowledge
### Background
- In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.
- The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.
- For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave.”
- Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave.

# 1.2 minesweeper
### Description
- In this project I build an AI that can play Minesweeper using propositional logic, and knowledge representation
### Background 
- Minesweeper is a puzzle game that consists of a grid of cells, where some of the cells contain hidden “mines.” Clicking on a cell that contains a mine detonates the mine, and causes the user to lose the game. Clicking on a “safe” cell (i.e., a cell that does not contain a mine) reveals a number that indicates how many neighboring cells – where a neighbor is a cell that is one square to the left, right, up, down, or diagonal from the given cell – contain a mine.
- In Minesweeper values of 1 indicate that the cell clicked on has one neighboring mine, and a value of 0 indicates that that cell has no neighboring mines ect.
- The goal is to build an AI that uses propositional logic to make decisions considering it's knowledge base, and making inferences based on this knowledge
- What information does the AI have access to? Well, the AI would know every time a safe cell is clicked on and would get to see the number for that cell.



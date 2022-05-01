'''
@myWSU-ID: V964T747
@Name: Enosh Nyarige
@Due Date: 05 / 01 / 2022
@ Artificial Intelligence, Programming Assignment 2
Wichita State University
'''

import random
import numpy as np


max_steps = 1000

inSize = 0
while inSize < 4:
	inSize = int(input("What is the size of n-queen board configuration?:\n\n"))

# print('- ' *(inSize+(inSize-1)))

queenRows = []

def nqueens(size):
	for i in range(size):
		print("\nColumn ", i)
		print("What row do you want to place a queen for the column? ", end='')		

		rowVar = int(input())
		queenRows.append(rowVar)
    
	print("You provided the following configuration: \n")
	print( '- ' *(inSize+(inSize-1)))
	_boardState(queenRows, size)

	
	print("\nA solution to your board configuration is: \n")
	print('- ' *(inSize+(inSize-1)))
	_boardState(min_conflicts(queenRows, size), size)

def _boardState(goal, size):
	for i in range(size):
		
		# print("Enter element at position ", i)
		row = ['o'] * size
		for col in range(size):
			if goal[col] == size - 1 - i:
				row[col] = 'x'
		
		print('| ', end='')
		print('  '.join(row), end='')
		print(' |')
	print('- ' *(size+(size-1)))

def _pathTo_sol(goal, size, col, row):
	total = 0
	for i in range(size):
		if i == col:
			continue
		if goal[i] == row or abs(i - col) == abs(goal[i] - row):
			total += 1
	return total

def _avail_conflicts(goal, size):
	_conflicts = [_pathTo_sol(goal, size, col, goal[col]) for col in range(size)]
	# print(_conflicts)
	return _conflicts

def min_conflicts(goal, size, numIters=max_steps):
	def randomQ_pos(x, y):

		choices_avail = random.choice([i for i in range(size) if y(x[i])])
		return choices_avail

	for k in range(numIters):
		numConflicts = _avail_conflicts(goal, size)
		if sum(numConflicts) == 0:
			return goal
		col = randomQ_pos(numConflicts, lambda elt: elt > 0)
		de_numConflict = [_pathTo_sol(goal, size, col, row) for row in range(size)]
		goal[col] = randomQ_pos(de_numConflict, lambda elt: elt == min(de_numConflict))

	_boardState(goal, size)

nqueens(inSize)
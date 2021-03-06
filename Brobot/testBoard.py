''' this file contains unit tests for the clobber board. To test model functionaility '''

import Board

def testInit():
	''' test the basic initialization of a Board object '''

	size = 16
	try:
		rr = Board.Board(size, size)
		if rr.array.size != size*size:
			return 0
		if rr.rows != size or rr.cols != size:
			return 0
		if len(rr.robotPositions) != 4:
			return 0
		if len(rr.targetPostitions) != 17:
			return 0

		return 1

	except:
		return 0


def testRobotPlacement():
	''' test that the four robots are placed on the board in distinct spots '''
	size = 16
	try:
		rr = Board.Board(size,size)
		positions = rr.robotPositions
		for i in xrange(4):
			position = positions[i]
			if positions.values().count(position) > 1:
				return 0
			if position[0] < 0 or position[0] >= size or position[1] < 0 or position[1] >= size:
				return 0

		return 1
	except:
		return 0

if __name__ == "__main__":

	tests = [testInit, testRobotPlacement]

	totalTestsRan = 0
	passedTests = 0
	for test in tests:
		totalTestsRan += 1
		result = test()
		passedTests += result
		if result:
			print("Passed: " + str(test))
		else:
			print("Failed: " + str(test))

	print("Passed {}/{} tests!".format(passedTests, totalTestsRan))
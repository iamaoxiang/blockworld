from State import State

class BlockWorldAgent:
    def __init__(self):
        
        pass

    def solve(self, initial_arrangement, goal_arrangement):
        #construct state object with initial state
        numOfBlocks = 0
        for ls in initial_arrangement:
            for e in ls:
                numOfBlocks +=1

        state = State(initial_arrangement, goal_arrangement, numOfBlocks)
        return state.moveToGoal()




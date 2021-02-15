import copy

class State:
    

    def __init__(self, initial_arrangement, goal_arrangement, numOfBlocks, moves = list()):
        self.leftTable = initial_arrangement # [["A", "B", "C"], ["D", "E"]]
        self.rightTable = goal_arrangement  #[["A", "C"], ["D", "E", "B"]]
        self.numOfBlocks = numOfBlocks
        self.diff = self.calcDiff()  # diff between init and goal, num of blocks - num of same arrangment
        self.moves = moves
        

    def moveToGoal(self): 
        while self.diff != 0:
            self = self.generateNextMove()
     
        return self.moves

    def ApplyNewMove(self, table, fromStackIndex, toStackIndex):
        curTable = copy.deepcopy(table)
        fromStack = curTable[fromStackIndex]
        topBlock = fromStack.pop()
        move = ()

        if (toStackIndex < 0): # a move to table
            toStack = list()  #create a new stack
            curTable.append(toStack)
            move = (topBlock, 'Table')
        else: # a move to stack
            toStack = curTable[toStackIndex]
            move = (topBlock, toStack[-1])

        # add block to new stack
        toStack.append(topBlock)

        # clean up empty stack
        if (len(fromStack) == 0):
            curTable.remove(fromStack)

        return curTable, move

    def generateNextMove(self): #will select and return the best move
        try: # first try moving a block to a stack, if none of the moves reduces the diff, move a block to the table

            # for each stack 
            for index, stack in enumerate(self.leftTable):

                for index2, stack2 in enumerate(self.leftTable):

                    # move top block from index stack to all other stacks
                    if (index != index2): # don't move to itself stack

                        newTable, move = self.ApplyNewMove(self.leftTable, index, index2) #passing by index so it can avoid modifing references 
                        newState = State(newTable, self.rightTable, self.numOfBlocks, copy.copy(self.moves))
                        newState.moves.append(move)
                        if newState.diff < self.diff: #it must be one of the best move if the diff gets smaller, no need to seek other moves
                            return newState

            # for each stack try to move onto the table
            for index, stack in enumerate(self.leftTable):

                # skip if this is already on a table
                if (len(stack) > 1):

                    # try move the top block to table
                    newTable, move = self.ApplyNewMove(self.leftTable, index, -1) # -1 means it is a moving to table
                    newState = State(newTable, self.rightTable, self.numOfBlocks, copy.copy(self.moves))
                    newState.moves.append(move)
                    if newState.diff <= self.diff:
                        return newState

        except:
            print("error: cannot find move") # actually it will never happen in this problem 


    def calcDiff(self):
        #diff = numOfBlocks - num of matching consecutive blocks beginning in a chain 
        numOfmatchedBlocks = 0
        
        tempTable = copy.copy(self.rightTable) #don't change original goal table
        for leftStack in self.leftTable:  #compare each stack on two tables
            for rightStack in tempTable:
                index = 0
                while len(leftStack) > index and len(rightStack) > index and leftStack[index] == rightStack[index]: 
                    numOfmatchedBlocks += 1
                    index += 1
                if index > 0:
                    tempTable.remove(rightStack) # just try to be more efficient, remove the stack that has been compared  
        
        return self.numOfBlocks - numOfmatchedBlocks

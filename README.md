# blockworld
### This is an explaination of my algorithm. The agent uses generate & test and Means-Ends Analysis.

## Design details

The State class constructs a state object which contains the current arrangement, goal arrangement, moves it has done, the number of differences from current state to goal state, number of blocks in total.
It starts with constructing a state with initial arrangement. MoveToGoal() method will keep checking diff between current state and goal state, until diff turns zero, which means it has reached the goal state. If diff is great than zero, it will generate a best move as the next move and replace current state to the new state.
The critical functions are calDiff() and generateNextMove(). calDiff() calculates the differences between current state and goal state, which is the number of blocks minus the number of blocks that are on the same position starting from the table and consecutively.

generateNextMove() first tries moving a block to another stack, if the new move can reduce the diff, that will the best next move. If moving a block to another stack does not reduce the diff, it will move a block to the table, use this state as the new state.
The technique behind the agent is: first use generate & test to generate a possible state, then use Means-Ends Analysis to choose the best state to move to.

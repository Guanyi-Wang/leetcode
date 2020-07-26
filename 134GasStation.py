class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # find the possible start point
        for i in range(len(gas)):
            # start from i, try to go back to i
            j = i+1
            tank = gas[i]-cost[i]
            while tank>=0:
                j = j%(len(gas))
                if j ==i:
                    return i
                tank += gas[j]-cost[j]
                j += 1
        return -1
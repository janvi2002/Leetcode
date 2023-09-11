class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total=0
        c=capacity
        for i in range(len(plants)):
            step=i
            capacity-=plants[i]
            if capacity < 0:
                total+=step+step+1
                capacity=c-plants[i]
            else:
                total+=1
        return total
            
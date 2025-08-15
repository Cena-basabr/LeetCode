class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_fruits = 0
        
        for fruit in fruits:
            found_basket = False
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = -1  # Mark the basket as used
                    found_basket = True
                    break
            
            if not found_basket:
                unplaced_fruits += 1
                
        return unplaced_fruits
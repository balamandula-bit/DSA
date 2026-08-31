class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord("a") + 1
        y = int(coordinates[1])

        if x % 2 == 0:
            if y % 2 == 0:
                return False
            else:
                return True
        
        else:
            if y % 2 == 0:
                return True
            else:
                return False

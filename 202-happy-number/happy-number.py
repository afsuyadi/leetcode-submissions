class Solution:
    def isHappy(self, n: int) -> bool:
        nstring = str(n)
        isDuplicate = False
        collection = []
        
        while isDuplicate == False:
            sqsum = 0
            for nstr in nstring:
                sqsum += int(nstr) * int(nstr)
            if sqsum == 1 :
                return True
            
            if sqsum in collection:
                isDuplicate = True
            else:
                collection.append(int(sqsum))
            
            nstring = str(sqsum) # return the number

        return False
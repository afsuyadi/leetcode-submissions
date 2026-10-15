# two-pointers
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        newimage = []
        for row in image:
            lastidx = len(row) - 1
            newrow = []
            while lastidx >= 0:
                newrow.append(row[lastidx])
                lastidx -= 1
            newimage.append(newrow)
            # row[:len(row)] = row[-1:1]
            print(row)
        
        print('after reverse=', image)
        couple = {
            0:1,
            1:0
        }
        for row in newimage:
            for i in range(len(row)):
                row[i] = couple[row[i]]
        
        return newimage

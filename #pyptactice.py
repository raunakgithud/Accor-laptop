#pyptactice

class findfreq:  
    def __init__(self,target,string): 
        self.Str = string
        self.T = target

    def findaction(self):
        N = len(self.Str)
        M = len(self.T)
        n = N -1
        m = M - 1
        count = 0
        for i in range(N):
            if ((self.Str[i] ==  self.T[0]) and (self.Str[i+m] == self.T[m])):
                count += 1

        print(count)

        return count


f = findfreq(target="ab", string="ababababab")
f.findaction()






               

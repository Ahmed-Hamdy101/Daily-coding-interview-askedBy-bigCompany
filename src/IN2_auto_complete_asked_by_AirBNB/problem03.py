# solved by Ahmed Hamdy : this problem asked by AirBNB for more algorithm see DailyInterviewPro.com
class Solution:
    # contructor
    def __init__(self):
        self.words = []
        # build will accept some list
    def build(self, words):
        # match the propreties 
        self.words = words
        # match the prefix 
    def autocomplete(self, prefix):
        if len(prefix) == 0:
            print('error zero length')
        else:
            temp = []
            for i in self.words:
                if (i.startswith(prefix)):
                    temp.append(i)
                
        return temp

s = Solution()
s.build(['dog', 'dot', 'door', 'cot'])
print(s.autocomplete('do'))

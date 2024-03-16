class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        i=1
        index=0
        while n>0 and index < len(target):
            if target[index]==i:
                res.append('Push')
                index+=1
            else:
                res.append('Push')
                res.append('Pop')
            n-=1
            i+=1
        return res
        


            
        
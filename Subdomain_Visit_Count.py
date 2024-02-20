class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        myDict = defaultdict(int)

        for cpdomain in cpdomains:
            count, cp = cpdomain.split()
            cp = cp.split(".")

            for i in range(len(cp)):
                subdomain = ".".join(cp[i:])
                myDict[subdomain] += int(count)
        
        return [str(count) + " " + subdomain for subdomain, count in myDict.items()]  

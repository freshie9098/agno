from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach : take a word and sort it to create key, 
        # add whichever word matches the sort into the dictionary.
        # create a final list of dictionary keys - list of lists.
        di = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            #Error 2 : unhashable type list. 
            # A list cannot become key. Change it to tuple. 
            di[key].append(word)
        
        res = []
        for k,v in di.items():
            res.append(v)
        return res


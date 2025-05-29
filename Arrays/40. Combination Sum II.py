#Python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(start,lis,total):
            if(total==target):
                result.append(lis[:])
                return
            if(total>target):
                return
            for i in range(start+1,len(candidates)):
                if(i>(start+1) and candidates[i]==candidates[i-1]):     #this is the statement where it helps us skip the duplicates with help of sorting at the start
                    continue
                lis.append(candidates[i])
                backtrack(i,lis,total+candidates[i])
                lis.pop()
            
        backtrack(-1,[],0)
        return result



#same logic but slight change in the use of parameter updation's   (this helps better as we code the previous combination version problem in the same format
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Step 1: Sort the candidates
        
        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])  # i+1 to not reuse the same element
                path.pop()
        
        backtrack(0, [], 0)
        return result

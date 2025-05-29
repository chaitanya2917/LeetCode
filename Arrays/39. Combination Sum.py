#optimal Python code -> backtracking
✅ Time Complexity: Approx. O(2^N), exponential because we try all combinations.
✅ Space Complexity: O(target) for the recursion stack and O(#combinations) for the result.

note: here the numbers in candidates list is unique distinct so there is less hassle unlike in the next question combination sum II  where they contain duplicates too
so there we have to manage these duplicates 


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        
        def backtracking(start,lis,sum):
            if(sum==target):
                result.append(lis[:])
                return
            if(sum>target):
                return
            for i in range(start,len(candidates)):
                lis.append(candidates[i])
                backtracking(i,lis,sum+candidates[i])
                lis.pop()

            
        
        backtracking(0,[],0)
        return result




Note: 
(mistakes i have done)
you see in the line 9 you see  "result.append(lis[:])"  
we can also use lis.copy() too
difference between  (lis[:] or lis.copy()) vs lis
when we pass lis we are passing the reference to the lis (as we also know it is mutable) later if we change the lis it also gets updated
so we can use lis[:] -> which creates a shallow copy so it won't change by the changes in the lis 





# C++ code:
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> path;
        backtrack(0, candidates, target, path, result);
        return result;
    }

    void backtrack(int start, vector<int>& candidates, int target, vector<int>& path, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(path);
            return;
        }
        if (target < 0) return;

        for (int i = start; i < candidates.size(); ++i) {
            path.push_back(candidates[i]);
            backtrack(i, candidates, target - candidates[i], path, result);
            path.pop_back();
        }
    }
};


# Java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(0, candidates, target, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, int[] candidates, int target, List<Integer> path, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        if (target < 0) return;

        for (int i = start; i < candidates.length; i++) {
            path.add(candidates[i]);
            backtrack(i, candidates, target - candidates[i], path, result);
            path.remove(path.size() - 1);
        }
    }
}




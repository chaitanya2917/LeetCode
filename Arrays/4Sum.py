#Python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        l=0
        r=len(nums)-1
        for i in range(len(nums)-3):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,len(nums)-2):
                if(j>i+1 and nums[j]==nums[j-1]):
                    continue
                l=j+1
                r=len(nums)-1
                while(l<r):
                    value=nums[i]+nums[j]+nums[l]+nums[r]
                    if(value==target):
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while(l<r and nums[l]==nums[l-1]):
                            l+=1
                        while(l<r and nums[r]==nums[r+1]):
                            r-=1
                    elif(value<target):
                        l+=1
                    else:
                        r-=1
        return res
            

#C++
#include <vector>
#include <algorithm>
using namespace std;
vector<vector<int>> fourSum(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> res;
    for (int i = 0; i < n-3; ++i) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        for (int j = i+1; j < n-2; ++j) {
            if (j > i+1 && nums[j] == nums[j-1]) continue;
            int left = j+1, right = n-1;
            while (left < right) {
                long long curr_sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];
                if (curr_sum == target) {
                    res.push_back({nums[i], nums[j], nums[left], nums[right]});
                    ++left; --right;
                    while (left < right && nums[left] == nums[left-1]) ++left;
                    while (left < right && nums[right] == nums[right+1]) --right;
                } else if (curr_sum < target) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
    }
    return res;
}


#Java
import java.util.*;
public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n-3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i+1; j < n-2; j++) {
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                int left = j+1, right = n-1;
                while (left < right) {
                    long curr_sum = (long)nums[i] + nums[j] + nums[left] + nums[right];
                    if (curr_sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++; right--;
                        while (left < right && nums[left] == nums[left-1]) left++;
                        while (left < right && nums[right] == nums[right+1]) right--;
                    } else if (curr_sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return res;
    }
}



Time Complexity:
Sorting: O(n log n)

Nested loops: O(n³)
Total: O(n³)—which is the best possible for this problem.


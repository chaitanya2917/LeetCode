#Python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=float('inf')
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                temp=nums[i]+nums[l]+nums[r]
                if(abs(target-temp)<abs(target-close)):
                    close=temp
                if(temp<target):
                    l+=1
                elif(temp>target):
                    r-=1
                else:
                    
                    return target
        return close


#C++
#include <vector>
#include <algorithm>
#include <cstdlib>  // For abs
using namespace std;
int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int closest_sum = nums[0] + nums[1] + nums[2];
    for (int i = 0; i < n-2; ++i) {
        int left = i+1, right = n-1;
        while (left < right) {
            int curr_sum = nums[i] + nums[left] + nums[right];
            if (abs(curr_sum - target) < abs(closest_sum - target))
                closest_sum = curr_sum;
            if (curr_sum < target)
                ++left;
            else if (curr_sum > target)
                --right;
            else
                return target;  // Perfect match
        }
    }
    return closest_sum;
}



#Java
import java.util.*;
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int closestSum = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n-2; i++) {
            int left = i+1, right = n-1;
            while (left < right) {
                int currSum = nums[i] + nums[left] + nums[right];
                if (Math.abs(currSum - target) < Math.abs(closestSum - target))
                    closestSum = currSum;
                if (currSum < target)
                    left++;
                else if (currSum > target)
                    right--;
                else
                    return target;  // Perfect match
            }
        }
        return closestSum;
    }
}

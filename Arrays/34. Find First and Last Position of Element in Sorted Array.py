#python

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        a=b=-1
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if(nums[mid]==target):
                temp=mid
                while(temp>=0 and nums[temp]==target):
                    temp-=1
                a=temp+1
                temp=mid
                while(temp<len(nums) and nums[temp]==target):
                    temp+=1
                b=temp-1
                return [a,b]
            if(nums[l]<= target < nums[mid]):
                r=mid-1
            else:
                l=mid+1

            
            
        return [-1,-1]
                    


in while loop we wrote a condition 
temp>=0 and nums[temp]==target
remember always to mention the (index out of bounds error condition first) rather than mentioning error condition in end

nums[temp]==target and temp>0  -> this produces error index out of bounds 



the above python code It finds the first and last occurrence of the target in the sorted array using binary search by expanding temp left and right from mid.


We can make it even more efficient by using binary search twice—once for the first occurrence, once for the last occurrence, instead of expanding temp left and right from mid.


#python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # Search left side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        def findRight():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1  # Search right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        return [findLeft(), findRight()]



#C++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = -1, right = -1;
        
        // Find leftmost
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                left = mid;
                r = mid - 1;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        // Find rightmost
        l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                right = mid;
                l = mid + 1;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return {left, right};
    }
};
    

#Java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[] {-1, -1};
        
        // Find leftmost
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                result[0] = mid;
                r = mid - 1;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        // Find rightmost
        l = 0; r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                result[1] = mid;
                l = mid + 1;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return result;
    }
}


#python
# my solution   yes optimal but there is even better solution and best
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            if(nums[r]==val):
                r-=1
            else:
                if(nums[l]==val):
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                    r-=1
                else:
                    l+=1
        return l


#python best optimal simple solution  (just visualize it)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    


#C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
};



#Java
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
}


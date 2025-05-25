#Python
#Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
#Optimal using HashMap to reduce the time complexity searching time reduces searching time O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls={}
        for i,num in enumerate(nums):
            if((target-num) in ls):
                return [i,ls[target-num]]
            else:
                ls[num]=i



#C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> nums_map;
        for(int i=0;i<nums.size();i++){
            if(nums_map.count(target-nums[i])){
                return {i,nums_map[target-nums[i]]};
            }
            else{
                nums_map[nums[i]]=i;
            }
        }

        return {};
    }
};
    


#Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer,Integer> nums_map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(nums_map.containsKey(target-nums[i])){
                return new int[]{i,nums_map.get(target-nums[i])};
            }
            else{
                nums_map.put(nums[i],i);
            }
        }


        return new int[]{};
    }
}
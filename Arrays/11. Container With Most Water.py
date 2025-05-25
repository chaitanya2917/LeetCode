#Python
#2 pointer (optimal)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while(l<r):
            area=max(area,min(height[l],height[r])*(r-l))
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return area

#C++
#include <vector>
#include <algorithm>
#include <vector>
#include <algorithm>
using namespace std;
int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1, max_area = 0;
    while (left < right) {
        int area = min(height[left], height[right]) * (right - left);
        max_area = max(max_area, area);
        if (height[left] < height[right])
            left++;
        else
            right--;
    }
    return max_area;
}



#Javapublic class Solution {
public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1, max_area = 0;
        while (left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            max_area = Math.max(max_area, area);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return max_area;
    }
}

                

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int low =0;
        int high = 0;
        for(int i = 0 ; i<nums.size();i++){
            if(nums[i]==val){
                low = i;
                high= i+1;
                break;
            }
        }
        while (high<nums.size()){
            if (nums[high]!=val){
                swap(nums[high],nums[low]);
                low+=1;
                high+=1;}
            else {high+=1;}
        }
        return low;
    }

};
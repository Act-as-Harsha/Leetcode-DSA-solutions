int evenNumberBitwiseORs(int* nums, int numsSize) {
    int result=0;
    for(int i=0;i < numsSize;i++){
        if(nums[i]%2==0){
            result |=nums[i];
        }
    }
    return result;
}

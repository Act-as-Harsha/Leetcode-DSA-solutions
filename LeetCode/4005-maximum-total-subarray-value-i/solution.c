long long maxTotalValue(int* nums, int numsSize, int k) {
    long size= numsSize;
        long long maxValue = nums[0],minValue = nums[0];
    for(int i= 1; i < size; i++){
        if(nums[i] > maxValue) maxValue = nums[i];
        if(nums[i] < minValue) minValue = nums[i];
    }
    return(maxValue - minValue) * (long long)k;
    
}

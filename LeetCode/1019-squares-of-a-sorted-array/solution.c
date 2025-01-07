int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int left = 0, right = numsSize - 1, i = numsSize - 1;
    int* output = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    
    while(left <= right){
        int value;
        if(nums[left] * nums[left] >= nums[right] * nums[right]){
            value = nums[left] * nums[left++];
        }else{
            value = nums[right] * nums[right--];
        }
        output[i--] = value;
    }
    return output;
}

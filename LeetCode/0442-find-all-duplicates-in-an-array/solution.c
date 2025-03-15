int* findDuplicates(int* nums, int numsSize, int* returnSize)
{
 *returnSize = 0;
 int *result = (int*)malloc(numsSize * sizeof(int));
 int i,index;
 for (i = 0; i < numsSize; i++) 
 {
 index = abs(nums[i]) - 1;
 if (nums[index] < 0) 
 {
 result[(*returnSize)++] = index + 1;
 } 
 else 
 {
 nums[index] = -nums[index]; 
 }
 }
 return result;
}

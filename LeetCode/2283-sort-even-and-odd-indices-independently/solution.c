int* sortEvenOdd(int* nums, int numsSize, int* returnSize) {
    int *arr=(int *)malloc(numsSize * sizeof(int));
     for(int i=0;i<numsSize;i++)
    {
        arr[i]=nums[i];
    }
    for(int i=0;i<numsSize;i+=2)
    {
        int key=arr[i];
        int j=i-2;
        while(j>=0 && arr[j]>key)
        {
            arr[j+2]=arr[j];
            j-=2;
        }
        arr[j+2]=key;
    }
    for(int i=1;i<numsSize;i+=2)
    {
        int key=arr[i];
        int j=i-2;
        while(j>=0 && arr[j]<key)
        {
            arr[j+2]=arr[j];
            j-=2;
        }
        arr[j+2]=key;
    }
    *returnSize=numsSize;
    return arr;
}

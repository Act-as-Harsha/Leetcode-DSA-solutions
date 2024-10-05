int* selfDividingNumbers(int left, int right, int* returnSize)
{
    int*arr = malloc((right-left+1)*sizeof(int));
    int index = 0;
    for(int i = left;i<=right;i++)
    {
        int digits=0,n=i,m=i;
        while(m!=0)
        {
            digits++;
            m/=10;
        }
        int z=0;
        while(n!=0)
        {
            int a = n%10;
            if(a!=0 && i%a==0) 
            z++;
            n/=10;
        }
        if(z==digits)
        {
            arr[index] = i;
            index++;
        }
    }
    *returnSize = index;
    return arr;
}

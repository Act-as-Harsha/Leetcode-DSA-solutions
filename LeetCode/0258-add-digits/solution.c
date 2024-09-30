int addDigits(int num) 
{
    int sum,rem;
    do{
        sum=0;
        while(num>0)
        {
            rem=num%10;
            sum+=rem;
            num/=10;
        }
        num=sum;
    }
    while(sum>=10);
    return sum;
}

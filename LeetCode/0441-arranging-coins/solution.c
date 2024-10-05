int arrangeCoins(int n) {
    int count=1;
    while(n>=0){
        int x=n-count;
        if(x>count){
            n-=count;
            count++;
        }
        else{
            return count;
        }
    }
    return 0;
}

bool isPalindrome(int x) {
    long int rem,rev = 0,org = x;
    while(x>0){
    rem = x%10;
    rev = (rev*10)+rem;
    x = x/10;
    }
    if(rev == org){
        return 1;
        }
    else{
        return 0; }
}
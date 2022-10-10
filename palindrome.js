function checkPalindrome(n)
{
    let reverse = 0;
    let temp = n;
    while (temp != 0) {
        reverse = (reverse * 10) + (temp % 10);
        temp = Math.floor(temp / 10);
    }
    return (reverse == n); 
}
 
// driver code
 
let n = 7007;
var result=checkPalindrome(n);
console.log(result);
 
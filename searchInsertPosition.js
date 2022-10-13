var searchInsert = (nums, target) =>{
    count=1;
    if(nums[0]>= target){
        return 0;
    }
    for(i=1; i<=nums.length-1; i++){
        if(target <= nums[i])
        {
            return i;
        }
        count=count+1;
    }
    if (count==nums.length){
        return i;
    }
}
var result = searchInsert([1,3,5,6],7);
console.log(result);
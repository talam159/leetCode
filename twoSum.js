var twoSum = function(nums, target) {
    for(i=0; i<=length.nums; i++){
        for(j=i+1;j<=length.nums; j++){
            if(nums[i]+nums[j]===target){
                return [i,j];
            }
        }
    }
};
two
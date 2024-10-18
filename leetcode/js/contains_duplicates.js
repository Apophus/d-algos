/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let numCount = {}
    for(num in nums){
     
        if(nums[num] in numCount){
            return true
        }
        else{
            numCount[nums[num]] = 1
        }
    }
    return false
    
};
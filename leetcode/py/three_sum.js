/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort()
    const res = []

    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        if(index>0 && element===nums[index-1]){
            continue;
        }
        let left = 0;
        let right = nums.length - 1;
        while (left < right) {
            const threeSum = nums[left] + nums[right] + element
            if(threeSum >0){
                right - 1
            }
            else if(threeSum <0){
                left + 1
            }
            else{
                let triplets = [element, nums[left], nums[right]]
                res.push(triplets)
                left +1
                while(nums[left] === nums[left-1] && left < right){
                    left +1
                }
            }
        }
        
    }
    return res

};
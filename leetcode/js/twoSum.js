/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let res
    for(let index=0; index < nums.length; index++){
        let diff = target - nums[index]
        if(nums.slice(index+1).includes(diff)){
            // res.push()
            res = [nums.slice(index+1).indexOf(diff)+index+1, index]
            console.log(res)
            return res
        }
    }
    return res

};
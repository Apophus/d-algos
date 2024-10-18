/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let charMaps = {}
    for(let i=0; i<strs.length; i++){
        let curr = strs[i]
        let currKey = curr.split('').sort().join('')
        if(currKey in charMaps){
            charMaps[currKey].push(curr)
        }
        else{
            charMaps[currKey] = [curr]
        }
    }
    for(let i =0; i<Object.keys(charMaps).length; i++){
        res.push(charMaps[Object.keys(charMaps)[i]])
    }
    
    return Object.values(charMaps)
};
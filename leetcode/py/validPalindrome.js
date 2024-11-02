/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let cleanedString = ''
    for(let index=0; index< s.length; index++){
        let code = s.charCodeAt(index)
        if(code >= 48 && code <= 122){
            cleanedString + s[index].toLowerCase()
        }
    }

    if(cleanedString == cleanedString.split('').reverse().join('')){
        return true
    }
    return false
};
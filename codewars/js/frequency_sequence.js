function freqSeq(str, sep) {
    
    let res = ''
    let clean  = new Map()

    for (i=0; i< str.length; i++){
        if (str[i] && !clean[str[i]]){
            clean[str[i]] = 1
        }
        else{
            if (str[i]){
                clean[str[i]] += 1
            }
            
        }
    } 

    for (i = 0; i < str.length; i++){
        if (i == str.length -1){
            res += clean[str[i]]
        }
        else{
            res += (clean[str[i]] + sep)
        }
       
        
    }

    return res
}

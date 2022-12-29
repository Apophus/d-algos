function disemvowel(str) {
    const vowels = ['a', 'e', 'i', 'o', 'u']
    for (let i=1; i<= str.length; i++){
        
        if (vowels.includes(str[i].toLowerCase())){
            str.replace(str[i], '')
        }
    }

    return str;
}
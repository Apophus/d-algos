function toCamelCase(str){
	let res = ''
	for (let i = 0; i < str.length; i++){
		if (str[i] === '-' || str[i] === '_'){
			continue;
		}
		else if(i>0 && (str[i-1] === '-' || str[i-1] === '_')) {
			res += str[i].toUpperCase()
		}
		else {
			res += str[i]
		}
	}
	return res
}

const str = "the-stealth-warrior"
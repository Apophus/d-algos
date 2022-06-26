function solution(number){
  // convert the number to a roman numeral
  // TODO Complete the flow.
  console.log(number)
  let roman_ob = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  let entries_ = Object.keys(roman_ob)
  console.log(entries_.length)

  for (let i=0; i< entries_.length; i++){
    if (roman_ob[entries_[i]]=== number){
      return entries_[i]
    }
  }
  let roman_translation = ''
  
  let filtered = entries_.filter((entry, value) => {
    return roman_ob[entry] > value
  })
  const closest = Math.min(filtered)
  console.log(filtered, closest)
  for (let j=0; j< filtered.length; j++){
    if (number > roman_ob[filtered[i]]){
      continue
    }
    else if(number < roman_ob[filtered[i]]){
      roman_translation += roman_ob[filtered[i]]
      let remainder = number - roman_ob[filtered[i]]

    }
  }



}
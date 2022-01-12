def longestDigitsPrefix(inputString):
    prefix = ''
    def remove_wite_space(inputString):
        cleaned_string = inputString.replace(' ', '')

        return cleaned_string

    if inputString.startswith(' '):
        return prefix
        
    if remove_wite_space(inputString).isdigit():
        prefix = remove_wite_space(inputString)
    for index, character in enumerate(remove_wite_space(inputString)):
        if character.isalpha() and not character.isdigit():
            prefix = remove_wite_space(inputString)[:index]
            break
    
    return prefix
def matchingStrings(strings, queries):
    # Write your code here

    answers = []
    for query in queries:
        count = strings.count(query)
        answers.append(count)

    return answers

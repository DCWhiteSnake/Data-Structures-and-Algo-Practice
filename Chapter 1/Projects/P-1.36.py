words = input("Please input a list of words seperated by space here")
list_of_words = words.split(" ")
archived_words = {}
for word in list_of_words:
    if word != " ":
        if word in archived_words:
            archived_words[word] += 1
        else:
            archived_words[word] = 1
    else:
        pass

print(archived_words)
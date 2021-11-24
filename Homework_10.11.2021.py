import re

if __name__ == '__main__':
    file = "text.txt"
    #the file has to be in the same directonary as the project
    text = open(file, 'r')
    #open the file in read mode
    dict = dict()
    for line in text:
        #remove special symbols and put all words in lower case
        line = line.strip()
        line = re.sub(r"[^a-zA-Z ]", "", line)
        #depending on the text you use, sometimes you have to delete the numbers, sometimes not.
        #Here the numbers are deleted, but if you don't want to delete them, you have to put them into the brackets "[]"
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in dict:
                dict[word] = dict[word]+1
            else:
                dict[word] = 1
                #count one more if the word is in the dictionary, otherwise put the word into the dictionary
    print(dict)
    #print the dictionary

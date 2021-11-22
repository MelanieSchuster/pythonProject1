import re

if __name__ == '__main__':
    f = "text.txt"
    #the file has to be in the same directonary as the project
    text = open(f, 'r')
    #open the file in read mode
    d = dict()
    for line in text:
        #remove special symbols and put all words in lower case
        line = line.strip()
        line = re.sub(r"[^a-zA-Z ]", "", line)
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word]+1
            else:
                d[word] = 1
                #count one more if the word is in the dictionary, otherwise put the word into the dictionary
    print(d)
    #print the dictionary

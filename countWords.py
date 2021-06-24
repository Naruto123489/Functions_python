#a program which takes the path of a file from the user and outputs the number of words used in the file
def countWordsFromFile():
    #takes the file path as input
    filename=input('Enter the file name: ')

    #variable to count the number of words
    count=0

    #open the file using open() in read mode
    file=open(filename,'r')

    #For each line in the file, split the line by whitespace to store all the words in the line as a list
    for line in file:
        words=line.split()
        # count the number of words in the words list for each file and keep adding to the count
        # len() in python which will give you the length of the list.
        # use it to find the length of words listed for each line
        count = count + len(words) 

    print("number of words: ")
    print(count)


countWordsFromFile()
    

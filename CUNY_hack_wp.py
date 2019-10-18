
#PYTHON IS VERY FLEXIBLE AND CAN HANDLE A VARIETY OF INPUT SOURCES - BUT LETS START WITH A SIMPLE .TXT FILE

fname = input("Enter file name: ")

if len(fname) < 1: fname = 'words.txt'
fh = open(fname)

#GIVEN A PIECE OF TEXT, YOU CAN EASILY DO SOME SIMPLE PROCESSING SUCH AS WORD COUNTS OR WORD FREQUENCIES

#PARSE THE LIST OF WORDS IN A PIECE OF TEXT AND PRINT THEM IN THE SORTED ORDER IN UPPER CASE

list = [] #New list to store unique words in the text
biglist = [] #New list to store ALL words in the text
bigcount = 0 #Counter for word count in the text

for line in fh:
    words = (line.rstrip().upper()).split()
    for word in words:
        biglist.append(word)
        bigcount = bigcount + 1
        if word in list:
            continue
        else:
            list.append(word)

list.sort()
biglist.sort()

print('***THIS INPUT TEXT HAS', bigcount, 'WORDS***\n')


print('***THIS IS A SORTED LIST OF ALL WORDS IN THE INPUT TEXT***\n')
print (biglist)

print ('***THIS IS A SORTED LIST OF UNIQUE WORDS IN THE INPUT TEXT***\n')
print (list)

#FIND THE FREQUENCY OF WORDS IN THE TEXT


counts = dict()

for word in biglist:
    counts[word] = counts.get(word,0) + 1

print ('***THIS IS THE SAME LIST WITH THE WORD COUNT***\n')
print(counts)

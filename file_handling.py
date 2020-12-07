
# the file does not exist so I opened a file in written mode
file = open('ajitesh1.txt',"w")
file.write("Hello first file created")
file.close()

# now appending the file2
file2 = open('ajitesh1.txt',"a+")
file2.write("\nso Who are you!!")
file2.close()

#copying the content of first file into second
# so here I am converting the content into binary and then copying that content into second file
file3 = open('ajitesh1.txt','rb')
file4 = open('ajitesh2.txt','wb')
while True:
    buf = file3.readline()
    if len(buf) != 0:
        file4.write(buf)
    else:
        break
file3.close()
file4.close()

# writing multiple lines into python file
# first create the list fo lines you wanna add into file and the just use the
'''function writelines(list)''' #and send the file

lines = ['Write a program','not to add two numbers','agar nahi likh paye','to batadena']
file5 = open('ajitesh1.txt','a+')
file5.writelines(lines)
file5.close()

#now the with keyword
'''with open('ajitesh1.txt','r') as file6:
    print(file6.readlines())'''

#copying the content of one file into another using with keyword
with open('ajitesh1.txt','rb') as file7:
    with open('ajitesh3.txt','wb') as file8:
        buffer = file7.read()
        file8.write(buffer)
    
# printing line by line with "With" keyword
with open('ajitesh1.txt','rb') as file7:
    for line in file7:
        print(line)

# splittig the wordd in a file
with open('ajitesh1.txt','rb') as file9:
    for i in file9:
        line = i
        words = line.split()
        print(words)
        

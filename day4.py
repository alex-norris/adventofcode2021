#pull raw into list
with open('day4.txt','r') as txt:
    raw = txt.readlines()

#grab first line of calls
calls = raw.pop(0).replace('\n','').split(",")
#remove extra line break
raw.pop(0)

#convert calls to integers
for i in range(0,len(calls)): 
    calls[i] = int(calls[i])

#make a big string to process boards
boardStr = r''.join(raw)
#turn into a string that looks like a list...
boards = list(boardStr.replace('\n\n ','],[').replace('\n ',',').replace('\n\n','],[').replace('\n',',').replace('  ',',').replace(' ',',').split('],['))
#actually turn into a 2d list
for i in range(0,len(boards)):
    boards[i] = list(boards[i].split(','))
    for j in range(0,len(boards[i])):
        boards[i][j] = int(boards[i][j]) #convert to ints

print(boards)


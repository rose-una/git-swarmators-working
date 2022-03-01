#Create initial position with grid of cells
#PIFF file created here is fed into .xml file

lines = []

#Dimensions of grid
x = 230
y = 230

#cells_per_row = 10
#cells_per_col = 10
#Each cell is 22x22

cell_width = 22   #((x-1)/cells_per_row)-1
cell_height = 22  #((y-1)/cells_per_col)-1

#Define initial values outside of for loop
a1 = 0                    #initial x1
a2 = cell_width           #initial x2
b1 = 230 - cell_height    #initial y1
b2 = 230                  #initial y2
offset = cell_width + 1   #how far does position shift each time
cell_number = 0

#for each row
for i in range(0,10):
    y1 = b1 - (i*offset)
    y2 = b2 - (i*offset)
    
    for j in range(0,10):
        x1 = a1 + (j*offset)
        x2 = a2 + (j*offset)
        
        cell_number += 1      

        lines.append(str(cell_number)+' Cell '+str(x1)+' '+str(x2)+' '+str(y1)+' '+str(y2)+' 0 0')

print(lines)

#Update  cellgird.piff file in "swarmators - working" directory
#with open('cellgrid.piff', 'w') as f: #'a' adds the stuff to existing stuff in existing file
#    for line in lines:                #'w' deletes past and has just the stuff in existing file
#        f.write(line)
#        f.write('\n')
# Problem - 1

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()    


# Problem - 2 

#      5
#      4 4
#      3 3 3
#      2 2 2 2
#      1 1 1 1 1

for i in range(5,0,-1):
    for j in range(i,6):
        print(i,end=" ")
    print()    


# Problem - 3 

#          1
#         22
#        333
#       4444
#      55555

for i in range(1,6,1):
    for s in range(5,i-1,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()    


# Problem - 4

#          55555
#           4444
#            333
#             22
#              1

for i in range(5,0,-1):
    for j in range(i,6,1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(i,end=" ")
    print()    


#   PYRAMID PATTERNS

# problem - 1

#           1 
#         2 2 2 
#       3 3 3 3 3 
#     4 4 4 4 4 4 4 
#   5 5 5 5 5 5 5 5 5 


for i in range(1,6,1):
    for s in range(i,6,1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    for k in range(2,i+1,1):
        print(i,end=" ")
    print() 


# Problem - 2

#  5 5 5 5 5 5 5 5 5 
#    4 4 4 4 4 4 4 
#      3 3 3 3 3 
#        2 2 2 
#          1 

for i in range(5,0,-1):
    for s in range(i,6,1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(i,end=" ")
    for k in range(i,1,-1):
        print(i,end=" ")    
    print()    

# Problem - 3

#          5 
#        4 4 4 
#      3 3 3 3 3 
#    2 2 2 2 2 2 2 
#  1 1 1 1 1 1 1 1 1 


for i in range(5,0,-1):
    for s in range(i,0,-1):
        print(" ",end=" ")
    for j in range(i,6,1):
        print(i,end=" ")
    for k in range(4,i-1,-1):
        print(i,end=" ")    
    print()    



# problem - 4

#  1 1 1 1 1 1 1 1 1 
#    2 2 2 2 2 2 2 
#      3 3 3 3 3 
#        4 4 4 
#          5 


for i in range(1,6,1):
    for s in range(1,i+1,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(i,end=" ")
    for k in range(4,i-1,-1):
        print(i,end=" ")    
    print()   
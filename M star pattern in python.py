n = 8
for i in range(n):
    for j in range(n):
        if (j==0 or j==(n-1)):
            if (i+j<=(n-1) or i+j>=(n-1)):
                print("* ",end = " ")
                
        
        
        elif (j==i):
            print("* ",end=" ")
               
              
        else:
            print("  ",end=" ")
        
        
            
    print(end="\n")

def swapdata():
    file1=input("Enter file name")
    file2=input("Enter file name")
    with open(file1,'r')as a:
        dataa=a.read()
        a.close()
    with open(file2,'r')as b:
        datab=b.read()
        b.close()
    with open(file1,'w')as a:
        a.write(datab)
        a.close()
    with open(file2,'w')as b:
        b.write(dataa)
        b.close()
        
    
    

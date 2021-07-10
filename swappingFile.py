# mam I referred to a youtube video,this project was very hard-
# I tried doing it alone for 2 hours and I couldn't get it :(

def swapFileData():

    file1 = input('Enter the original file: ')
    file2 = input('Enter the file to be swapped: ')

    with open(file1,'r') as a:
        data_a = a.read()   
    with open(file2,'r') as b:
        data_b = b.read()


    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)
        
swapFileData()

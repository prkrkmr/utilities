# Name : Prakhar Kumar
# Email : prkrkmr@gmail.com
# File Sorter


import os 
li = []
li1 = []
li = os.listdir('./')
print "Sorting"
for i in li : 
    if os.path.isfile(i) == True and i[0] != '.':
        a = i.split('.')[-1]
        if os.path.exists(a):
            if os.path.isfile('./'+a+'/'+i) == True and i.split('.')[0][-1].isdigit() == False:
                os.rename(i,'./'+a+'/'+i.split('.')[0]+'1.'+i.split('.')[-1])
            if os.path.isfile('./'+a+'/'+i) == True and i.split('.')[0][-1].isdigit() == True:
                os.rename(i,'./'+a+'/'+i.split('.')[0].strip(i.split('.')[0][-1])+str(int(i.split('.')[0][-1])+1)+'.'+i.split('.')[-1])
        else:
            os.mkdir(a)
            os.rename(i,'./'+a+'/'+i)
print "Sorted"
print "Thank You for using it."

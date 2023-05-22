d={"py":'python',
   "js":'javascript',
   "c":'C',
   'cc':"C++",
   'java':"Java"}
inp =input("Input file name: ")
ext= inp.split('.')[1]
for keys in d:
    if ext==keys:
     print ("File extension="+d[keys])
     break

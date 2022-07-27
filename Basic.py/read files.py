# r = read() --> كاتبه انا ما ذى واطبع  الملف اقراء 
# w = wright -->ا لملف جوه اكتب
# a = append -->ا لملف اخر فى حاجه اضافه
# r+ --> الوقت بنفس واقراء اكتب
# readable() --> True,False <--- للقراءه قابل الملف لو 
# readline() --> ويطبعه ىسطر اول  يقراء 
# readlines() --> list داخل ويطبعه ىسطر كل  يقراء 

# البدايه
files = open("read files.txt","r") # الملف وامتداد اسم قيمه اول قيمتين تاخذ

print(files.read()) # كاملا الملف قراء

print(files.readline()) # hamada
print(files.readline()) # sayed


# النهايه
files.close()
#file_hanling-assesments

print('-----------------------------')

print("file_handing Asesment:")

print("-----------------------------")

txt1 = "Python"
txt2 = "File Handling"
txt3 = "is fun!"


with open('data.txt','w') as txtdata:
    txtdata.writelines(txt1)
    txtdata.writelines(txt2)
    txtdata.writelines(txt3)

print("file created successfully")






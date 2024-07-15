# please copy the java file name with all the directories in terminal or in the ouput for e.g
#  "Project/src/main/java/com/eCommerece/Controller.java"
# the newly created file with semicolon inserted will be created in the same folder where the java file (file to be inserted with semicolon) is located


try:
    file_name = input(str())
    if file_name == None or file_name == '':
        raise Exception("The file name given was not found ,please check the given file name and then try again....")
    clone_name = file_name.split(".")
    clone_name[-2] = clone_name[-2] + "WithSemicolonInserted"
    clone_name = '.'.join(clone_name)

    file1 = open(clone_name,"w")

    with open(file_name, 'r') as file:
        data = file.readlines()
        data1 = data

        for j,i in enumerate(data):

            i1 =  i
            i = i.strip()

            if i == '' or i[0] == '}' or i[0] == ')':
                continue
            
            if i == 'else{':
                continue

            if (i.find('import') != -1 or i.find('package') != -1) and i[-1] != ';':
                i += ';\n'
                data1.remove(i1)
                data1.insert(j,i)
                continue
            
            if i[0] == '/':
                continue

            if i[0] =='@':
                i += '\n'
                data1.remove(i1)
                data1.insert(j,i)
                continue

            if  i.find('return') != -1 and i[-1] != ';':
                i += ';\n'
                data1.remove(i1)
                data1.insert(j,i)
                continue
            if (i.find('public') != -1 or i.find('private') != -1 or i.find('protected') != -1) and i[-1] != ';' and i[-1] not in ['{','}',')',',']:
                i += ';\n'
                data1.remove(i1)
                data1.insert(j,i)
                continue

            if (i.find('public') == -1 and i.find('private') == -1 and i.find('protected') == -1) and i[-1] != ';':
                i += ';\n'
                data1.remove(i1)
                data1.insert(j,i)
                continue

    file1.writelines(data1)    
    file1.close()  
    file.close()

except FileNotFoundError:
    print("The file name given was not found ,please check the given file name and then try again....")

    



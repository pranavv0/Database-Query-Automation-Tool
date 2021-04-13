def run(tasks, group):
    dbhost= host(group)
    for i in dbhost:
        if tasks["type"]=="database":
            mycursor = i.cursor()
            mycursor.execute("SHOW DATABASES")
            flag=1
            for x in mycursor:
                if x[0]== tasks["name"]:
                    flag=0
                    print("Database {} already exists".format(tasks["name"]))
            if flag == 1:                         
                exe=i.cursor()
                exe.execute("CREATE DATABASE {0}".format(tasks["name"]))
                print("Database {} created Successfully".format(tasks["name"]))
        if tasks["type"]=="table":
            mycursor = i.cursor()
            mycursor.execute("SHOW TABLES")
            flag=1
            for x in mycursor:
                if x[0]==tasks["name"]:
                    flag=0
                    print("Table {} already exists".format(tasks["name"]))
            if flag==1:
                if checkKey(tasks, "columns"):
                    sep=",".join(tasks["columns"])                
                    exe=i.cursor()
                    exe.execute("CREATE TABLE {0}( {1} )".format(tasks["name"], sep) )
                    print("Table {} Created Successfully".format(tasks["name"]))
                else:
                    print("ERROR: A table must have at least 1 column, {} has no column".format(tasks["name"]))
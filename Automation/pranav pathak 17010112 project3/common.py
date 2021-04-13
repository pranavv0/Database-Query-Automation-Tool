from yaml import safe_load
def load(filePath):
    with open(filePath, 'rb') as f:
        data = f.read()
        k = safe_load(data)
        
    return k

def dbConnection(host, user, password, database=""):
    import mysql.connector
    host=host
    username=user
    password=password
    database=database
    mydb = mysql.connector.connect(host="{0}".format(host), username="{0}".format(username),password="{0}".format(password),database="{0}".format(database))
    return mydb



def connection(hosts, group):
    h=[]
    for i in hosts:
        if i['group']==group:
            host=list(i.keys())
            host.remove("group")
            for j in host:
                if "database" in list(i[j].keys()):
                    h.append(dbConnection(i[j]["host"],i[j]["user"],i[j]["passwd"],i[j]["database"]))
                else:
                    h.append(dbConnection(i[j]["host"],i[j]["user"],i[j]["passwd"]))
            return h


        
def host(group):
    hosts= load("hosts.yml")
    hostsCon=connection(hosts, group)
    return hostsCon

def checkKey(dict, key):      
    if key in dict.keys(): 
        return True 
    else: 
        return False 
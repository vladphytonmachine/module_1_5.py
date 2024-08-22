immutable_var = 1 , "два " , True , 4
print (immutable_var)
print ( type ( immutable_var))
#immutable_var [1]=2 # попытка изменить обьект в кортеже ведет к ошибке т.к. он также как и список относится к типу коллекций но без возможности изменять обьекты
mutable_list=[1 ,"два" , True , 4]
print(mutable_list)
mutable_list[0]="one"
print(mutable_list)
mutable_list.append("five")
print(mutable_list)
mutable_list.extend ("six")
mutable_list.extend (["seven" , "eight"])
print(mutable_list)
mutable_list.remove (True)
print(mutable_list)
print ("два" in mutable_list)
print ("one" not in mutable_list)
print(mutable_list[0:3:2])
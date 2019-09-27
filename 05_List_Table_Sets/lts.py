#List
l = ["Bob","Rolf","Anne"]
#Tuble and we can't modify,Add,Remove the tuble this diff list and tuble
t = ("Bob","Rolf","Anne")
#Set can Add,modify,Remove but can't add dublicate element
s = {"Bob","Rolf","Anne"}

l[0] = 'aboulmagd'
print(l[0])

#tuble can't edit
#t[0] = 'aboulamgd'
#print(t[0])

#add to list usinf append method
l.append('smith')
print(l)

l.remove("Anne")
print(l)

# Notice that it's add and not append when working with sets
s.add("smith")
print(s)
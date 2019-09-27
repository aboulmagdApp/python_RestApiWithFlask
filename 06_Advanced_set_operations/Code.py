friendes = {"aboulmagd","Rolf","Anne","smith"}
abroad = {"Bob","Anne"}

local_friends = friendes.difference(abroad)

#using union
friendes_union = friendes.union(abroad)

#print(local_friends)

#print(friendes_union)

art = {"Bob","Jen","Rolf","Charlie"}
science = {"Bob","Jen","Adam","Anne"}

both = art.intersection(science)
print(both)
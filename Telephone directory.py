#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pymongo')


# In[ ]:


import pymongo


# In[ ]:


client=pymongo.MongoClient("mongodb://localhost:27017")


# In[ ]:


mydbs=client["Telephone_Directory"]


# In[ ]:


mycol=mydbs["Client"]


# In[ ]:


mydoc=mylist = [
  { "name": "Amy", "address": "Apple st 652","Number":"7708401047"},
  { "name": "Hannah", "address": "Mountain 21","Number":"8808401047"},
  { "name": "Michael", "address": "Valley 345","Number":"8858401047"},
  { "name": "Sandy", "address": "Ocean blvd 2","Number":"9998401047"},
  { "name": "Betty", "address": "Green Grass 1","Number":"8899401047"},
  { "name": "Richard", "address": "Sky st 331","Number":"6677401047"},
  { "name": "Susan", "address": "One way 98","Number":"8787401047"},
  { "name": "Vicky", "address": "Yellow Garden 2","Number":"7708401234"},
  { "name": "Ben", "address": "Park Lane 38","Number":"7708401048"},
  { "name": "William", "address": "Central st 954","Number":"7708401857"},
  { "name": "Chuck", "address": "Main Road 989","Number":"7708401041"},
  { "name": "Viola", "address": "Sideway 1633","Number":"7708581047"}
]


# In[ ]:


x=mycol.insert_many(mydoc)



# In[77]:


curser=mydbs.Client.find({})


# In[78]:


for doc in curser:
    print(curser)


# In[52]:


one_record=mycol.find_one()
print(one_record)


# In[53]:


# update_one() updating exsisting document

h=mycol.update_one({"name":"Amy"},{"$set":{"address":"15-west street Canada"}})


# In[54]:


updated_document=mycol.find_one()


# In[55]:


print(updated_document)


# In[79]:


#delete_one()

d=mycol.find_one({"name":"Sandy"})


# In[80]:


print(d)


# In[81]:


d_=mycol.delete_one({"name":"Sandy"})


# In[82]:


print(d_)


# In[83]:


# to check that deleted doc
d1=mycol.find_one({"name":"Sandy"})
print(d1)


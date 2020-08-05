
# coding: utf-8

# In[10]:


fruta = "banana"
letra = "a"

i = 0

while i < len(fruta)-1:
    if fruta[i] == letra:
        print (fruta[i])
    else:
        print ("_")
    i += 1


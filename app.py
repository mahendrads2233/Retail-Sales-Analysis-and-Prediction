#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI


# In[2]:


from fastapi import FastAPI

app_fast = FastAPI()

@app_fast.get("/home")
def home():
    return {"name": "Mahendra", "Age": 77}

@app_fast.get("/Items")

def items():
    
    return {'cars' : ['Nissan'],  'Engg' : 675}

@app_fast.get("/Item(item_id):int")

def items(item_id):
    return {"id":item_id , 'cars' : ['Nissan'],  'Engg' : 675}


# In[ ]:





# In[ ]:





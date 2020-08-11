#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Use command /MathDept for full set of profs")
find_handler = CommandHandler('find_a_prof',find)
dispatcher.add_handler(find_handler)


# In[ ]:


def Dept(update, context):
    # should return names of profs along with message
    context.bot.send_message(chat_id=update.effective_chat.id,text="Kindly use these commands /n/Quan - for results garnered from forms /n/Qual - for results garnered from Ateneo Profs to Pick")
Dept_handler = CommandHandler('MathDept',Dept)
dispatcher.add_handler(Dept_handler)


# In[ ]:


def ProfNameQuali(update,context):
    name_of_prof=update.message.text
    if name_of_prof.upper() in profDict:
        #return Mico's results
        context.bot.send_message(chat_id=update.effective_chat.id,text="Your prof's grade is {}".format(profDict[name_of_prof.upper()]))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Could not Find Prof ://")


# In[ ]:


def Quali(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Type in your prof's name")
Quali_handler = CommandHandler('Qual',Quali)
dispatcher.add_handler(Quali_handler)


# In[ ]:


Quali_finder_handler = MessageHandler(Filters.text & (~Filters.command), ProfNameQuali)
dispatcher.add_handler(Quali_finder_handler)


# In[ ]:


def ProfNameQuanti(update,context):
    name_of_prof=update.message.text
    if name_of_prof.upper() in profDict:
        #return Alvin's results
        context.bot.send_message(chat_id=update.effective_chat.id,text="Your prof's grade is {}".format(profDict[name_of_prof.upper()]))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Could not Find Prof ://")


# In[ ]:


def Quanti(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Type in your prof's name")
Quanti_handler = CommandHandler('Quan',Quanti)
dispatcher.add_handler(Quanti_handler)


# In[ ]:


Quanti_finder_handler = MessageHandler(Filters.text & (~Filters.command), ProfNameQuanti)
dispatcher.add_handler(Quanti_finder_handler)


# In[ ]:





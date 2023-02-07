#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pygame')


# In[3]:


from pygame import mixer


# In[4]:


mixer.init()


# In[6]:


mixer.music.load("Desktop\MUSIC\Mahalaya - Original _ Mahishasura Mardini _ Birendra Krishna Bhadra _ Durga Puja (256 kbps).mp3")
mixer.music.set_volume(0.7)
mixer.music.play()


# In[8]:


while True: 
    print("Press 'p' to pause") 
    print("Press 'r' to resume") 
    print("Press 'e' to exit ") 
    print("Press 'q' to queue") 
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause()
        print("Eawww!! your song is paused.")
    elif query == 'r':
        mixer.music.unpause()
        print("Hurrah!! you played the song.")
    elif query == 'e':
        mixer.music.stop()
        print("I think you pressed exit.")
    elif query == 'q':
        mixer.music.queue('Music/wedont.mp3')
        print("yuhhh! Song added, wait till previous one ended.")
    break


# In[ ]:




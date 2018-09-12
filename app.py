# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:17:16 2018

@author: strix
"""
import instaloader
L = instaloader.Instaloader()
L.login('straxico', '498154724')        # (login)
profile = instaloader.Profile.from_username(L.context, 'guilan.fanni')
list=[]
i=0
for followee in profile.get_followees():
    #user=[]
    i+=i
    #user.append(followee.biography)
    #user.append(followee.username)
    #user.append(followee.userid)
    #user.append(followee.full_name)
    #user.append(followee.followers)
    #user.append(followee.followees)
    #list.append(user)
    list.append(followee.biography)
    print(i)

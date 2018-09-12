# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:17:16 2018

@author: strix
"""
import instaloader
L = instaloader.Instaloader()
L.login('#####USERNAME#######', '#####PASSWORD#####')        # (login)
profile = instaloader.Profile.from_username(L.context, '#####user who get followers bio#####')
list=[]
i=0
for followee in profile.get_followees():
    #user=[]
    i+=1
    #user.append(followee.biography)
    #user.append(followee.username)
    #user.append(followee.userid)
    #user.append(followee.full_name)
    #user.append(followee.followers)
    #user.append(followee.followees)
    #list.append(user)
    bio=followee.biography
    list.append(bio)
    print(i)
    print(bio)

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:17:16 2018
@author: strix
"""
import csv
import instaloader
YOUR_USER_NAME="#########"
YOUR_PASSWORD="#########"
TARGET_USERNAME="#########"

L = instaloader.Instaloader()
L.login(YOUR_USER_NAME, YOUR_PASSWORD)        # (login)
profile = instaloader.Profile.from_username(L.context,TARGET_USERNAME)
mylist=[]
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
    #mylist.append(user)
    bio=followee.biography
    mylist.append(bio)
    print(i)
    print(bio)

with open("{}.csv".format(TARGET_USERNAME), 'w',encoding="utf-8") as myfile:
     wr = csv.writer(myfile)
     wr.writerow(mylist)
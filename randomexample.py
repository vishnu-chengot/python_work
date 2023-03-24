import random

roll_agin ="yes"

while roll_agin =="yes" or roll_agin =="y":
   print("rolling the dice.....")
   print("the values are....")
   print(random.randint(1,6))
   roll_agin = input("roll the dice again (y/n)")
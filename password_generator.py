#!/bin/python3
import random
import pyperclip

def passwordGenerator(n):
  chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,-@"
  password = ""
  for i in range(n):
    password += random.choice(chars)
  pyperclip.copy(password)
  print("Password : {} copied to clipboard successfully !\n".format(password))
  return password

#Example : https://kith.com/products/nike-air-force-1-low-retro-nyc-black-white.
#ITEMID  : 34972212423
#INJECTIONPOINT : /cart/add/ + itemid

__author__ = 'Nico Holubek'
import time
import pyperclip

def URLGEN(site, itemid):
    URL = str(site) + "/cart/add/" + str(Itemid)
    return URL

site = input("SITEURL : ")
Itemid = input("ItemID : ")

URL = URLGEN(site, Itemid)

print (str(site) , "Backdoor link Created..")
time.sleep(1)
print (URL)
time.sleep(1)
print ("Copied to Clipboard")
pyperclip.copy(URL)
time.sleep(1)
print ("Enjoy your Pair ;)")
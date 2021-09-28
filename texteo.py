import pywhatkit as kit 
import random
lines = open("insultos.txt").read().splitlines()
linea = random.choice(lines)
kit.sendwhatmsg_instantly("+573117860823",linea,10)
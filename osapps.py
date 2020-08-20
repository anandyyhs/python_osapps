import os

while True:
	print("What is your requirement : "  , end='')
	p = input()


	if ((("run" in p)  or ("open" in p) or ("execute" in p)) and (( not ("do not" in p)) and ( not ("dont" in p)))):
	  if (("chrome" in p) or ("browser" in p)) : 
	    os.system("chrome")

	  elif (("notepad" in p) or ("editor" in p) ) :
	    os.system("notepad")

	  elif  (("player" in p) and ("media" in p)):
	    os.system("wmplayer")
	  
       	  elif  (("player" in p) and ("media" in p)):
	    os.system("wmplayer")

	elif  ("exit" in p)  or ("quit" in p):
	    break

	else:
	  print("This do not support")


from Tkinter import *
import tkFileDialog
 
def browse(): 
	master = Tk()
	master.withdraw() #hiding tkinter window
 
	file_path = tkFileDialog.askopenfilename(title="Open file", filetypes=[("txt file",".txt"),("All files","*")])
 	'''
	if file_path != "":
		print "you chose file with path:", file_path
 
	else:
   		print "you didn't open anything!"
 	'''
	return file_path
	master.quit()

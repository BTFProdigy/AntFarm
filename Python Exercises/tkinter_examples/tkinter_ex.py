from tkinter import *


# function for button click
def click():
	entered_text = textentry.get()
	text_output.delete(0.0, END)
	try:
		definition = my_dictonary[entered_text]
	except:
		definition = 'Frazzled! Sorry looks like I don\'t know that word.'
	text_output.insert(END, definition)


# exit function
def close_window():
	window.destroy()
	exit(0)


# main window
window = Tk()
window.title("Babies first window")
window.configure(background="black")

# image
image_llama = PhotoImage(file='./llama.gif')
Label(window, image=image_llama, bg='black').grid(row=0, column=0, sticky=W)

#label 0
Label(window, 
	text='Enter the word you would like a definition for:',
	bg='black',
	fg='white',
	font='none 12 bold').grid(row=1, column=0, sticky=W)

# text entry box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2,column=0, sticky=N)

# submit button
Button(window,
	text='SUBMIT',
	width=6,
	command=click).grid(row=3, column=0, sticky=N)

# label 1
Label(window,
	text='\nDefinition',
	bg='black',
	fg='white',
	font='none 12 bold'
	).grid(row=4, column=0, sticky=N)

# text box
text_output = Text(window, width=75, height=4, wrap=WORD, background='white')
text_output.grid(row=5, column=0, sticky=N)

# dictonary
my_dictonary = {
	'algorithm':'Step by step instructions to complete a task',
	'bug':'A gap in the code that causes the program to fail',
}

# exit label
Label(window,
	text='\nExit',
	bg='black',
	fg='white',
	font='none 12 bold'
	).grid(row=6, column=0, sticky=N)

# submit button
Button(window,
	text='Exit',
	width=6,
	command=close_window).grid(row=7, column=0, sticky=N)
# window main loop
window.mainloop()


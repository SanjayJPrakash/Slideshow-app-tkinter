from tkinter import *
from PIL import ImageTk, Image

def next(img_no):
    global label
    global forwardbutton
    global backbutton
    global exitbutton
    label.grid_forget() # deletes the previous image
                          # to delete buttons we can use backbutton.forget()
    label = Label(image=list_image[img_no])
    

	
    label.grid(row=1,column=0,columnspan=3)
    forwardbutton=Button(root,text="Forward",command=lambda:next(img_no+1))
    backbutton=Button(root,text="Back",command=lambda:next(img_no-1))

    
    #backbutton=Button(root, text="Back",command=lambda:next(img_no-1))

    if img_no==3:
        forwardbutton=Button(root, text="Forward",command=lambda:next(0))
    if img_no==0:
        backbutton=button_back = Button(root, text="Back", command=lambda:next(3))
    



    backbutton.grid(row=5,column=0)
    
    forwardbutton.grid(row=5,column=2)



root = Tk()
root.title("Image viewer")
root.geometry("700x700")
image1=ImageTk.PhotoImage(Image.open(r"C:\Users\New User\Pictures\ford.jpg"))
image2=ImageTk.PhotoImage(Image.open(r"C:\Users\New User\Pictures\images.jpg"))
image3=ImageTk.PhotoImage(Image.open(r"C:\Users\New User\Pictures\bird.jpg"))
image4=ImageTk.PhotoImage(Image.open(r"C:\Users\New User\Pictures\pic.jpg"))

list_image=[image1,image2,image3,image4]

label = Label(image=image1)
label.grid(row=1,column=0,columnspan=3)


backbutton = Button(root,text="Back",command=lambda:next(3))
exitbutton = Button(root,text="Exit",command=root.quit)
forwardbutton=Button(root,text="Forward",command=lambda:next(1))

backbutton.grid(row=5,column=0)
exitbutton.grid(row=5,column=1)
forwardbutton.grid(row=5,column=2)

root.mainloop()




import tkinter as tk

def show_message():
    message_label.config(text= "🎉 Happy birthday! 🥳 \n 🎁 Have a wonderful day! 🎂")

root = tk.Tk()
root.title("Birthday button")
root.geometry("300x300")

#Title label
title_label = tk.Label(root, text="Birthday App 🧁", font=("Arial", 16))
title_label.pack(pady=10)

#Button
wish_button = tk.Button(root,text="Click for a surprise! 🎊", command=show_message)
wish_button.pack(pady=10)

#Message label (initially empty)
message_label = tk.Label(root, text="", font=("Arial", 16))
message_label.pack(pady=10)

root.mainloop()




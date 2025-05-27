import tkinter as tk

shopping_list=[]

window = tk.Tk()
window.title = "Shopping List"
window.geometry("600x400")
shoppinglabel = tk.Label(window,text="Shopping List")
shoppinglistlabel = tk.Label(window, text=f"{shopping_list}")
add_item = tk.Entry(window)


def hasnumber(text):
    split_parts = text.strip().split(" ", 1)
    if len(split_parts) == 2 and split_parts[0].isdigit():
        quantity = int(split_parts[0])
        item = split_parts[1].strip()
    else:
        quantity = 1
        item.strip()
    return item, quantity

def add_clicked():
    global shopping_list
    shopping_list.append(add_item.get().strip())


addbutton = tk.Button(window, text = "Add", command=add_clicked)

shoppinglabel.pack()
shoppinglistlabel.pack()
addbutton.pack()
add_item.pack()
window.mainloop()


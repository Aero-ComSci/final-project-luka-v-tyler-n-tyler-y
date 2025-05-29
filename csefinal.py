import tkinter as tk


from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float


# Prices
burger_prices = {
    'banana bread': 2,
    'slice of watermelon': 1.25,
    'Vanilla Ice Cream': 3,
    'Chocolate Ice Cream' : 3,
    'Strawberry Ice Cream' : 3
}


drink_prices = {
    'orange juice': 1.00,
    'lemonade': 1.50,
    'iced tea': 2.25,
    'iced coffee' : 2.25
}


fries_prices = {
    'cookies': 1.00,
    'popsicle': 1.25,
    'chips': 1.50,
    'corn' : 1.00
}


condiment_prices = {
    'Ketchup Packet': 0.25,
    'mustard' : 0.25,
    'relish' : 0.25,
    'chimoy' : 0.25,
    'tajin' : 0.25
}


# list
order = []


# Functions
def add_item(name, price):
    def click():
        order.append(Item(name, price))
        update_order_list()
    return click


def remove_item():
    selected = order_list.curselection()
    if selected:
        index = selected[0]
        del order[index]
        update_order_list()


def clear_order():
    order.clear()
    update_order_list()
    total_label.config(text="Total: $0.00")


def update_order_list():
    order_list.delete(0, tk.END)
    for item in order:
        order_list.insert(tk.END, item.name)


def submit_order():
    total = sum(item.price for item in order)

    # count burgers
    burger_count = sum(1 for item in order if item.name in burger_prices)
    drink_count = sum(1 for item in order if item.name in drink_prices)
    fries_count = sum(1 for item in order if item.name in fries_prices)

    #find the lowest number to make it a discount
    combo = min(burger_count, drink_count, fries_count)

    #combo itself
    total = total - combo * 1.00 

    #make the total stop at 2 decimals
    total_label.config(text=f"Total: ${total:.2f}")


# GUI 
root = tk.Tk()
root.title("Order Up!")
root.geometry("500x800")


# Burger 
burger_frame = tk.LabelFrame(root, text="Foods", padx=10, pady=10)
burger_frame.pack(fill="x", padx=10, pady=5)


for burger, price in burger_prices.items():
    tk.Button(burger_frame, text=f"{burger} (${price})", command=add_item(burger, price)).pack(side='left', padx=5)


# Drink 
drink_frame = tk.LabelFrame(root, text="Drinks", padx=10, pady=10)
drink_frame.pack(fill="x", padx=10, pady=5)


for drink, price in drink_prices.items():
    tk.Button(drink_frame, text=f"{drink} (${price})" , command=add_item(drink, price)).pack(side='left', padx=5)


# Fries
fries_frame = tk.LabelFrame(root, text="snacks", padx=10, pady=10)
fries_frame.pack(fill="x", padx=10, pady=5)


for fries, price in fries_prices.items():
    tk.Button(fries_frame, text=f"{fries} (${price})", command=add_item(fries, price)).pack(side='left', padx=5)


# condiments
condiments_frame = tk.LabelFrame(root, text="Condiments Packets", padx=10, pady=10)
condiments_frame.pack(fill="x", padx=10, pady=5)


for condiments, price in condiment_prices.items():
    tk.Button(condiments_frame, text=f"{condiments} (${price})", command=add_item(condiments, price)).pack(padx=5, side="left")


# Order List
list_frame = tk.LabelFrame(root, text="Current Order", padx=10, pady=10)
list_frame.pack(fill="both", expand=True, padx=10, pady=10)


order_list = tk.Listbox(list_frame, width=50, height=15)
order_list.pack()


#Buttons
tk.Button(root, text="Remove Selected Item", bg="red", fg="white", command=remove_item).pack(pady=5)
tk.Button(root, text="Clear Order", bg="orange", fg="black", command=clear_order).pack(pady=5)
tk.Button(root, text="Submit Order", font=("Arial", 14), bg="green", fg="white", command=submit_order).pack(pady=10)


# Total Label
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 16))
total_label.pack(pady=10)


root.mainloop()



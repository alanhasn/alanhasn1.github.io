import tkinter as tk
from tkinter import ttk
import requests
import webbrowser



def save_website(url, name):
    response = requests.get(url)
    content = response.text
    filename = f"{name}.html"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

    return filename, name, url

def open_file(event):
    item = tree.selection()[0]
    filename = tree.item(item, "text")
    webbrowser.open_new_tab(filename)

root = tk.Tk()
root.title("Offline Website Saver")
root.geometry("800x400")


# Create a custom style for the Treeview widget
style = ttk.Style()
style.configure("Treeview", background="#f0f0f0", foreground="black", rowheight=25, font=("Arial", 12))

# Apply the custom style to the Treeview widget
tree = ttk.Treeview(root, columns=("Name", "URL", "File"), show='headings', style="Treeview")

tree = ttk.Treeview(root, columns=("Name", "URL", "File"), show='headings')
tree.heading("Name", text="Name")
tree.heading("URL", text="URL")
tree.heading("File", text="File")
tree.pack()

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(root, width=50)
name_entry.pack()

def save_website_offline():
    url = url_entry.get()
    name = name_entry.get()
    saved_website = save_website(url, name)
    filename, name, url = saved_website
    tree.insert("", "end", text=filename, values=(name, url, filename))

tree_button = tk.Button(root, text="Save Website Offline", command=save_website_offline)
tree_button.pack()
tree_button.config(font=("Arial", 12), bg="blue", fg="white")

tree.bind('<Double-1>', open_file)

root.mainloop()



# import tkinter as tk
# from tkinter import ttk
# import requests
# import webbrowser

# def save_website(url, name):
#     response = requests.get(url)
#     content = response.text
#     filename = f"{name}.html"

#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(content)

#     return filename, name, url

# def open_file(event):
#     item = tree.selection()[0]
#     filename = tree.item(item, "text")
#     webbrowser.open_new_tab(filename)

# root = tk.Tk()
# root.title("Offline Website Saver")
# root.geometry("800x400")

# # Allow window to be resizable
# root.pack_propagate(False)

# # Create a custom style for the Treeview widget
# style = ttk.Style()
# style.configure("Treeview", background="#f0f0f0", foreground="black", rowheight=25, font=("Arial", 12))

# # Apply the custom style to the Treeview widget
# tree = ttk.Treeview(root, columns=("Name", "URL", "File"), show='headings', style="Treeview")
# tree.heading("Name", text="Name")
# tree.heading("URL", text="URL")
# tree.heading("File", text="File")
# tree.pack()

# url_label = tk.Label(root, text="Enter URL:")
# url_label.pack()

# url_entry = tk.Entry(root, width=50)
# url_entry.pack()

# name_label = tk.Label(root, text="Enter Name:")
# name_label.pack()

# name_entry = tk.Entry(root, width=50)
# name_entry.pack()

# def save_website_offline():
#     url = url_entry.get()
#     name = name_entry.get()
#     saved_website = save_website(url, name)
#     filename, name, url = saved_website
#     tree.insert("", "end", text=filename, values=(name, url, filename))

# tree_button = tk.Button(root, text="Save Website Offline", command=save_website_offline)
# tree_button.pack()
# tree_button.config(font=("Arial", 12), bg="blue", fg="white")

# tree.bind('<Double-1>', open_file)

# root.mainloop()

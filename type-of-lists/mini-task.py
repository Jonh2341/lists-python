import tkinter as tk 

# Example idea: A program that stores quiz questions in a dictionary, asks the user, and checks answers.

# Practice: Build a small program that manages a shopping list (add/remove items with functions).

# --1

# questions_dic = {
#     "first_q": "what is 2 + 2 ", 
#     "second_q": "Capital of Germany? ", 
#     "third_q": "the best man's friend? ",
# }

# answers_dic = {
#     "first_q": "4", 
#     "second_q": "Berlin", 
#     "third_q": "dog",
# }

# def ask_user(questions, answers):
#     for a, q in questions.items():
#         user_answer = input(q)
#         correct_answer = answers[a]

#         if user_answer.strip().lower() == correct_answer.lower():
#             print("that's right!")
#         else:
#             print("that's wrong :(")
        


# ask_user(questions_dic, answers_dic)

# --1

# --2

# "Pasta", "Tomato", "Cheese", "Vine"

# addProduct(shopping_list, "Vine")
# removeProduct(shopping_list, "Vine")

# print(shopping_list)

root = tk.Tk()
root.title('Shopping list')

shopping_list = []

def addProduct(product):
    shopping_list.append(product.lower())

def removeProduct(product, uiEl):
    shopping_list.remove(product.lower())
    uiEl.destroy()
    print(shopping_list)

label = tk.Label(root, text="Shopping list: ")
label.pack()

def on_click():
    product_name = entry.get().lower() 
    shopping_list.append(product_name)
    productLabel = tk.Label(root, text=entry.get() + '                 ')
    productLabel.pack(pady=10, fill='x')
    deleteBtn = tk.Button(productLabel, text="remove", bg="red", 
    command=lambda p=product_name, l=productLabel: removeProduct(p, l))
    deleteBtn.pack(side="right")

    print(shopping_list)

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Add", bg="green" ,command=on_click)
button.pack()

root.mainloop()

# ---


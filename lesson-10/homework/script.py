## Exercise 1. ToDo List Application
from datetime import date

class Task:
    def __init__(self, title, description, due_date, status='incomplete'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = 'complete'
                break

    def list_all(self):
        for task in self.tasks:
            print(f"{task.title}: {task.status}")

    def incomplete(self):
        for task in self.tasks:
            if task.status == 'incomplete':
                print(task.title)

# Main CLI
def main():
    todo = ToDoList()
    while True:
        print("1. Add task\n2. Mark complete\n3. List all\n4. Incomplete\n5. Exit")
        choice = input()
        if choice == '1':
            title = input("Title: ")
            desc = input("Desc: ")
            due = date.today()
            task = Task(title, desc, due)
            todo.add_task(task)
        elif choice == '2':
            title = input("Title: ")
            todo.mark_complete(title)
        elif choice == '3':
            todo.list_all()
        elif choice == '4':
            todo.incomplete()
        elif choice == '5':
            break

if __name__ == "__main__":
    main()

## Exercise 2. Simple Blog System
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all(self):
        for post in self.posts:
            print(f"{post.title} by {post.author}")

    def by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post.title)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                break

    def latest(self, n=5):
        for post in self.posts[-n:]:
            print(post.title)


## Exercise 3. Simple Banking System
class Account:
    def __init__(self, acc_num, name, balance=0):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_num] = account

    def check_balance(self, acc_num):
        return self.accounts.get(acc_num).balance if acc_num in self.accounts else None

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            self.accounts[acc_num].balance += amount

    def withdraw(self, acc_num, amount):
        if acc_num in self.accounts and self.accounts[acc_num].balance >= amount:
            self.accounts[acc_num].balance -= amount

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts and self.accounts[from_acc].balance >= amount:
            self.accounts[from_acc].balance -= amount
            self.accounts[to_acc].balance += amount



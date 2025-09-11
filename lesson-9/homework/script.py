#1. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
      
#2. Person Class
from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # date object
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
#3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b if b != 0 else "Division by zero"
#4. Shape and Subclasses
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        return self.a + self.b + self.c

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
#5. Binary Search Tree Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
#6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
#7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
#8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}  # item: (price, quantity)

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] = (price, self.items[item][1] + quantity)
        else:
            self.items[item] = (price, quantity)

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(price * qty for price, qty in self.items.values())
#9. Stack with Display
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def display(self):
        print(self.items)
#10. Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None
#11. Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}  # acc_num: balance

    def add_account(self, acc_num, name, balance=0):
        self.accounts[acc_num] = {'name': name, 'balance': balance}

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            self.accounts[acc_num]['balance'] += amount

    def withdraw(self, acc_num, amount):
        if acc_num in self.accounts and self.accounts[acc_num]['balance'] >= amount:
            self.accounts[acc_num]['balance'] -= amount

    def get_balance(self, acc_num):
        return self.accounts.get(acc_num, {}).get('balance', 0)


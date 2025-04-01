# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by using pythons built-in operations. 
#                 They allow developers to define or customize the behavious of objects

class Book:

  def __init__(self,title,author,num_pages):
    self.title=title
    self.author=author
    self.num_pages=num_pages

  def __str__(self):                          # returns a string representation of the object or else without this and only init, when you perform print(book1) it will return a memory address
    return f"'{self.title}' by {self.author}"

  def __eq__(self,other):                     # gives two objects are equal based on title and author without this, two objects with exact same descriptions would be treated as unequal
    return self.title == other.title and self.author==other.author
  
  def __lt__(self,other):
    return self.num_pages<other.num_pages
  
  def __gt__(self,other):
    return self.num_pages<other.num_pages
  
  def __add__(self,other):
    return f"{self.num_pages + other.num_pages} pages"

  def __contains__(self,keyword):
    return keyword in self.title or keyword in self.author
  
  def __getitem__(self, key):
    if key == "title":
      return self.title
    elif key == "author":
      return self.author
    elif key == "num_pages":
      return self.num_pages
    else:
      return f"key {key} was not found"
  
book1=Book("The Hoobit", "J. R. R. Tolkien", 310)
book2=Book("Harry Potter", "J.K. Rowling", 220)
book3=Book("The Hoobit", "J. R. R. Tolkien", 450)

print(book1)
print(book1==book3)
print(book2.num_pages<book3.num_pages)
print(book1.num_pages>book2.num_pages)

print(book1+book2)

print("Harry" in book2)
print("Rowling" in book2)

print(book3['title'])
print(book2['author'])
print(book1['num_pages'])
print(book1['audio'])
import webbrowser

t = []
url = ""
buffer = ""

name = str(input("enter the name of the book: "))
t.append(name)

author = str(input("enter the name of the author: "))
t.append(author)

genre = str(input("enter the primary genre of the book: "))
t.append(genre)

book_data = tuple(t)

print(book_data)

str1 = book_data[0].split()
for i in range(len(str1)):
    buffer = buffer + str1[i] + "+"

url = "https://www.amazon.in/s?k=" + buffer + "&i=stripbooks"
print("url: ",url)
webbrowser.open(url, new=0)

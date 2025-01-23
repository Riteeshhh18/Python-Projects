import pyshorteners

url = input("Enter Any URL: ")

def shorturl(url):
    s= pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shorturl(url)
import emoji

def emojize():
    x = input("Input: ")
    print(emoji.emojize(x, language="alias"))

emojize()
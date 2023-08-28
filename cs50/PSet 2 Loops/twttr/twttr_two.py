def main():
    sentence = input("Input: ")
    print(shorten(sentence))
    
    

def shorten(word):
    vowels = ["a","e", "o", "u", "i"]
    output = ""
    for i in word:
        if i.lower() in vowels:
            pass
        else:
            output += i
    return output


if __name__ == "__main__":
    main()
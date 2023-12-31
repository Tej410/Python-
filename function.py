# def greet(first_name,last_name):
#     print(f'Hello {first_name} {last_name}!')
# greet("Smith",last_name="Will")



def show_emoji(message):
    emojis = {
    ":)" : "😀",
    ":(" : "😞",
    ";)" : "😉"
    }
    words = message.split(" ")
    string = ""
    for word in words:
        string += emojis.get(word,word) + " "
    return(string)
sentence = input(">");
print(show_emoji(sentence))
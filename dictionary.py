# numbers = {
#     1: "One",
#     2: "Two",
#     3: "Three",
#     4: "Four",
#     5: "Five",
#     6: "Six",
#     7: "Seven",
#     8: "Eight",
#     9: "Nine",
#     0: "Zero"
# }


# phone = input("Phone: ")
# string = ""
# for digit in phone:
#     string += numbers[int(digit)] + " "
    

# print(string)


emojis = {
    ":)" : "😀",
    ":(" : "😞",
    ";)" : "😉"
}
message = input(">");
words = message.split(" ")
string = ""
for word in words:
    string += emojis.get(word,word) + " "
print(string)

def replace_word():
    str="hello youtube, just for you we still learning. Thanks for your support"
    replace_w=input("Replace word: ")
    replace_with=input("Replace with: ")
    print("Before\n",str)
    str=str.replace(replace_w,replace_with)
    print("After\n",str)

while True:
    replace_word()
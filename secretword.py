secret_word = "chupacabra"
word = input("enter the secret word")
while word != secret_word:
    if word == secret_word:
        print("you have successffully left the loop")
    break
print ("enter another word:")

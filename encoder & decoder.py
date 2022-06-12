def encrypt (text1, shift1):
    cyber_text =''
    for x in range(0, len(text1)):
        new_encode = alphabet.index(text1[x])
        position = new_encode + shift1
        if  position > 26:
            position -= 26
            letter = alphabet[position]
        else:
             letter = alphabet[position]
        cyber_text += letter
    print(f'here is the encode result : {cyber_text} ')
    
def decrypt (text2, shift2):
    real_text =''
    for x in range(0, len(text2)):
        new_encode = alphabet.index(text2[x])
        position = new_encode - shift2
        if position > 26:
            position += 26
            letter = alphabet[position]
        else:
             letter = alphabet[position]
        real_text += letter
    print(f'the cyber text is {real_text} ') 









while next:
      alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      if direction == 'encode':
          encrypt(text,shift)
      elif direction == 'decode':
          decrypt(text, shift)
      a = input('do you want to contiue "yes" or "no" ')
      if a == 'no':
        next = False
        print('bye')

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.   


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
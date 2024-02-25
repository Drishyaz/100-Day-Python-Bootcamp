# LIVE DEMO: https://replit.com/@guardianblossom/caesar-cipher#main.py
def caesar(text,shift,direction):
  if direction == 'decode':
    shift *= -1
    
  cipher_text = ""
  for letter in text:
    if letter in alphabet:
      index = alphabet.index(letter)
      cipher_text += alphabet[index+shift]
    else:
      cipher_text += letter
  print(f"The {direction}d text is {cipher_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo as logo
print(logo)

end_of_game = False
while not end_of_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #incase the shift number is more than the no. of alphabets
  shift = shift % 26
  #text = hello, shift = 3, cipher = khoor

  caesar(text=text, shift=shift, direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    end_of_game = True
    print("Goodbye")

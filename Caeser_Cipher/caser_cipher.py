import caesar_cipher_art
print(caesar_cipher_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(original_text, Shift_amount, Encode_Decode):
    Outcome = ""
    if Encode_Decode == "Decode":
        Shift_amount *= -1


    for letter in original_text:
        if letter not in alphabet:
            Outcome += letter
        else:

            Shifted = alphabet.index(letter) + Shift_amount
            Shifted %= len(alphabet)
            Outcome = alphabet[Shifted]
    print(f"Your Encoded Or Decoded mes is {Outcome}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,Shift_amount=shift,Encode_Decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
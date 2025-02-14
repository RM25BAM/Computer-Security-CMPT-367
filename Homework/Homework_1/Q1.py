def main():
    user_input = input("Enter your plaintext for encryption: ")
    ans_C, shift = shift_Cipher(user_input)
    ans_V, key, key_size = vigenere_Cipher(user_input)
    ans_P = product_Cipher(user_input, shift, key, key_size)
    print(f"")
def shift_Cipher(sentence):
    sentence = sentence.upper()
    punct = f",.'"
    sentence = sentence.replace(' ', '')
    #alphabet = ['A','B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ans = ''
    shift = int(input("Enter the key: "))
    for i in sentence:
        if i in punct:
            continue
        formula = ((ord(i) - 65 + shift) % 26) + 65
        ans += chr(formula)
    return ans, shift
def vigenere_Cipher(user_input):
    key = []
    # for the vigenere Cipher based on the block seperate every character based on block then do the key for each char ( in this case 5)
    key_size = int(input("Enter the key size: "))
    for i in range(key_size):
        key_value = int(input("Enter the key value: "))
        key.append(key_value)
    user_input = user_input.upper()
    user_input = user_input.replace(' ', '').replace("'", "").replace(".", "").replace(",", "")
    #user_input = ' '.join([user_input[i:i+5] for i in range(0, len(user_input), 5)])
    ans = ''
    key_index = 0  
    for i in user_input:
        if i.isalpha():
            formula = ((ord(i) - 65 + key[key_index % len(key)]) % 26) + 65
            ans += chr(formula)
            key_index += 1
    return ans, key, key_size
def product_Cipher(user_input, shift, key):
    #apply both sequentially that is the product cipher
    user_input = user_input.upper()
    user_input = user_input.replace(' ', '').replace("'", "").replace(".", "").replace(",", "")
    ans = ''
    for i in user_input:
        formula = ((ord(i) - 65 + shift) % 26) + 65 
        ans += chr(formula)
    final = ''
    key_index = 0  
    for i in ans:
        formula = ((ord(i) - 65 + key[key_index % len(key)]) % 26) + 65
        final += chr(formula)
        key_index += 1 
    return final 
main()
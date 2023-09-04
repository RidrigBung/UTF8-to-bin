text = input("Enter your text and it will be transformed in bin: ")

bin_list = []
for char in text:
    bin_list.append(bin(ord(char))[2:].rjust(8, '0'))

bin_text = ' '.join(bin_list)
print("Your text in bin:", bin_text)

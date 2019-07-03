letter = input()
if letter>="a" and letter<="z":
    if letter in("a", "e", "i", "o", "u"):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")

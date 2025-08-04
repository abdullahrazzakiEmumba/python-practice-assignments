try:
    sentence = input("Enter string:")
    vowels = ['a','e','i','o','u']
    result = {}
    for vowel in vowels:
        count = sum(1 if x==vowel else 0 for x in sentence)
        print(vowel," occurs ",count,"times in the sentence")
except Exception as e:
    print(e)
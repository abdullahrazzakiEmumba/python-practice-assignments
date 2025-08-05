try:
    name = input("Enter file name:")
    with open(name,'r') as file:
        text = file.read()
        words = text.split(' ')
        count={}
        for word in words:
            count[word.lower()] = count.get(word.lower(),0)+1
        print(count)
except Exception as e:
    print(e)
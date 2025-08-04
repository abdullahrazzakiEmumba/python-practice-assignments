try:
    value = float(input("Enter temperature:"))
    unit = (input("Enter unit (C or F):")).lower()
    if unit not in ["c","f"]:
        raise Exception("Invalid unit please enter c or f")
    result = None
    newUnit = 'Celsius'
    if unit == 'c':
        result = (value * 9/5)+32
        newUnit="Farenheight"
    else:
        result = (value*5/9)-32
    print("Temperature in ",newUnit," is ",result)
except Exception as e:
    print(e)
import re
try:
    value = input("Enter value")
    value_type = input("Enter type (int, float or email):").lower()
    if value_type not in ["int","float","email"]:
        raise Exception("type must be one of (int,float,email)")
    result=True
    if value_type=="int":
        try:
            int_value = int(value)
        except:
            result=False
    elif value_type=='float':
        try:
            float_value = float(value)
        except:
            result=False
    else:
        res = re.search(r'^\S+@\S(.)\S+$',value)
        result = True if res else False
    print(result)

except Exception as e:
    print(e)
try:
    values = input("Enter comma separated values:").split(",")
    int_values = [int(x) for x in values]
    total_sum = sum(int_values)
    average  = total_sum/len(int_values)
    maximum = max(int_values)
    rev = int_values[::-1]
    print("Sum is:",total_sum)
    print("Average is:",average)
    print("Maximum is:",maximum)
    print("Reverse values are",','.join([str(x) for x in rev]))
except Exception as e:
    print(e)
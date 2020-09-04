temperature = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temperature = float(temperature)
print(f"{temperature}\N{degree sign} in Celsius is equivalent to {temperature*1.8+32}\N{degree sign} Fahrenheit.")
temperature = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temperature = float(temperature)
if unit == "F" or unit == "f":
  print("Converting Fahhrenheit to Celsius.")
elif unit == "C" or unit == "c":
  print("Converting Celsius to Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
print(f"{temperature}\N{degree sign} in Celsius is equivalent to {temperature*1.8+32}\N{degree sign} Fahrenheit.")
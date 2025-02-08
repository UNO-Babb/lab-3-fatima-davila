#TempConvert.py
#Name:Fatima Davila
#Date:2/6/14
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature

  farenheit = float(input("give me a temperature in fahrenheit : "))
  
  #Convert that temperature to celsius, rounding to 1 decimal percision
  celsius = (farenheit- 32) / 1.8
  print(f"tempC :", "{celsius:.2f}")
  #Output converted temperature.
  tempF = 80
  
  tempC = tempF / 2

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
 main()

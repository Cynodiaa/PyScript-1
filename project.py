def mergeNumber():
  numberText = input("Give an integer between 0 and 1000: ")

  if numberText.isnumeric() == False:
    return print("Given value is not an positive integer.")
  if int(numberText) > 1000:
    return print("Value should be in range of 0 and 1000.")

  reducedNumber = 0
  for number in [*numberText]:
    reducedNumber += int(number)

  return print(f'Sum of all digits of {numberText}: {reducedNumber}')

mergeNumber()
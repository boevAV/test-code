def cDigits(num):
    return len(str(num))

def fNumbers(N):
    count = 0
    num = 0
    while count < N:
        nDigits = cDigits(num)
        if nDigits > 0 and num % nDigits == 0:
            print(num)
            count += 1
        num += 1

print("Добро пожаловать!\n")

while True:
  try:
    N = int(input("Задайте, пожалуйста, число:\n>"))
    break
  except ValueError:
    print("Извините, но это не число!")

fNumbers(N)

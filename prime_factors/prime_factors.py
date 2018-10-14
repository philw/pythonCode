def factorise(number):
  # check whether the number is prime
  prime = True
  factor = 1
  root = int(number**0.5)
  # check for factors up to the square root
  while prime and factor < root:
    factor += 1
    if number % factor == 0:
      prime = False
  # if it's prime, add it to the list
  if prime:
    factors.append(number)
  # if it's not prime, factorise it and its pair
  else:
    factorise(factor)
    factorise(int(number/factor))

#validate input
value = 0
while value < 1:
  value = input("Give me a positive integer:")
  try:
    value = int(value)
  except:
    print("That's not a whole number.")
    value = 0
# do the factorisation
factors = []
factorise(value)
print("The prime factors of",value,"are",factors)
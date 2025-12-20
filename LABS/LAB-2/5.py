def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % 1 == 0:
      return False
  return True
print(is_prime(2))

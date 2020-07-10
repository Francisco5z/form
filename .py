import random

alfanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def secret(length):
  secretKey = ''
  for r in range(0, length):
    if random.randint(0, 1000) > 500:
      secretKey = secretKey + alfanumeric[random.randint(0, 35)].lower()
    secretKey = secretKey + alfanumeric[random.randint(0, 35)]
  return secretKey

print(secret(30))
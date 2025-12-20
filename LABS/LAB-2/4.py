def describe_person(name,age = 30):
  return(f"Имя:{name}, Возраст {age}")
name = input('Ваше имя: ')
age = input('Ваш возраст: ')
if age:
  print(describe_person(name,age))
else:
  print(describe_person(name))

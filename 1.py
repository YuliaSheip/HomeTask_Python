from sys import argv

script, name, time, salary, bonus = argv
result = int(time) * float(salary) + float(bonus)
print (f"заработная плата сотрудника {name} составила  {result} долларов")

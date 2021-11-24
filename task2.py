reading = int(input("Сколько вы потратили на чтение этой книги? Введите время в секундах:"))
hour = reading // 3600
minute = (reading % 3600) // 60
seconds = (reading % 3600) % 60
if hour < 10:
     hour =str(0) + str(hour)
if minute < 10:
    minute = str(0)+ str(minute)
if seconds <10:
    seconds =str(0)+ str(seconds)
print(hour,":",minute,":",seconds)
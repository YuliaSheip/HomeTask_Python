revenue = int(input("Введите Вашу выручку в долл. США"))
expenses = int(input("Введите Ваши убытки в долл. США"))
profit = revenue - expenses
effectiveness = round(profit/revenue*100, 2)

while revenue < 0:
    revenue = int(input("Выручка должна иметь положительное значение или равняться нулю.Введите Вашу выручку в долл. США"))
while expenses < 0:
    expenses = int(input("Убытки должны иметь положительное или нулевое значение.Введите Ваши убытки в долл. США"))
if revenue > expenses:
    print("Поздравляю. Ваша компания работает с прибылью. Ваша прибыль -", profit, "долл США")
    print("Рентабельность выручки составила", effectiveness, "%")
    staff = int(input("Сколько у Вас сотрудников?"))
    profit_per_member = round(profit / staff, 2)
    while staff <= 0:
        staff = int(input("Сколько у Вас сотрудников?"))
    print("На одного сотрудника приходится", profit_per_member, "долл США прибыли")
if revenue == expenses:
    print("Ваша выручка покрывает убытки, однако прибыли нет")
elif expenses > revenue:
    print("К сожалению, вы убыточны. Прибыль отрицательная и составляет", profit, "долл США")
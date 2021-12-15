import json

result_list = []
dict_profit = {}
dict_loss = {}

with open("my_file7.txt") as f_obj:
    average_profit_list = []
    content = f_obj.readlines()
    for line in content:
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_profit.update({name: profit})
        else:
            dict_loss.update({name : profit})
    result_list.append(dict_profit)
    result_list.append(dict_loss)
    result_list.append({"average_profit": sum(average_profit_list)/len(average_profit_list)})
with open("file7.json", "w") as f_obj:
    json.dump(result_list, f_obj)






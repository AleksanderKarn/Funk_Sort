import csv


def get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv'):
    '''функция открывает заранее отсортированный
     файл по дате и находит в нем значение по
      заданным в параметрах  фильтрам и записывает
       результат в файл dump.csv'''
    ## список отсортированных значений по дате
    dict_ = []
    ##открываю файл с отсортированными значениями по дате
    with open('sort_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            dict_.append(row)
    ## поиск в ключах словаря соответствующих фильтрам значений
    for i in dict_:
        if i['date'] == date and i['Name'] == name:
            result = i
            ## запись результата в файл
            with open(filename, 'w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=(result.values()), delimiter='|')
                w.writeheader()
            return result


y = get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv')
print(y)

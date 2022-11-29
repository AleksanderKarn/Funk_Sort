import csv

def select_sorted(sort_columns="high", limit=None, group_by_name=False, order='asc', filename='dump.csv'):
    '''Функция по заданным параметрам сортирует данные
     в заданном файле и записывает отсортированный результат
      в новый файл'''
    d_ = []  ## список для словарей (d) с значениями
    ## открываем исходный файл
    with open('all_stocks_5yr.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ## записываю файл построчно циклом в виде списка словарей
        for row in reader:
            d_.append(row)
    ## проверка наличия фильтра для сортировки и его значения
    if order =='desc':
        sort_list = sorted(d_, key=lambda x: x[sort_columns], reverse=True)
    else:
        sort_list = sorted(d_, key=lambda x: x[sort_columns])
    ## проверка наличия указанного лимита записываемых в файл строк, и его значения при наличии
    if limit != False:
        result = sort_list[:limit]
    else:
        result = sort_list
    ## записываю файл в csv формат
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=(result[0].keys()), delimiter='|')
        w.writeheader()
        for i in result:
            w.writerow(i)


select_sorted(sort_columns='high', limit=10, order='desc', filename='dump.csv')

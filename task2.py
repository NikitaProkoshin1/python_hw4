#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление. Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(kwargs_to_dict(name='Иван', sername='Иванов', weight=40,
                     months=['Июнь', 'Июль', 'Август'],
                     courses={'python': 'ver 3.11', 'c#': 'ver 2.5'}))

import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
     
    data = read_csv('./app_01/world_population.csv')
    print(data[0])                              # muestra el primer elemento de la lista de diccionarios:

# pasar la lista a leida desde el csv a un diccionario:

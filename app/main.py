import utils_1
import read_csv
import charts


def run():
    data = read_csv.read_csv('world_population.csv')
    # Para filtrar por paises de sudamerica:
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
        
    country = input('Type Country => ')

    result = utils_1.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils_1.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels, values)
    

if __name__ == '__main__':
    run()


import pandas as pd

# Створіть DataFrame з наданими даними
data = {
    'Посада': ['Junior Software Engineer', 'Senior Software Engineer', 'Software Engineer', 'System Architect',
               'Technical Lead'],
    'min': [100, 1300, 500, 3000, 1425],
    'max': [1250, 9200, 5400, 5000, 6200]
}

aggregated_tab = pd.DataFrame(data)


def fill_avg_salary(row):
    return (row['min'] + row['max']) / 2


aggregated_tab['avg'] = aggregated_tab.apply(fill_avg_salary, axis=1)

print(aggregated_tab)

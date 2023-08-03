import matplotlib.pyplot as plt
'''
def generate_bar_chart():
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

if __name__ == '__main__':
    generate_bar_chart()
'''

# si no quiero valores estaticos, sino que pueva variarlos en cada llamada de la funcion:
def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}_bar.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
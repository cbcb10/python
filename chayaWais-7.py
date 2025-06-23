import matplotlib.pyplot as mplt

if __name__ == '__main__':
    x_values = list(range(1, 11))
    y_values = [x ** 3 for x in x_values]
    y_values_divide = [x / 3 for x in x_values]

    mplt.subplot(1, 2, 1)
    mplt.plot(x_values, y_values, marker='o', color='b', linewidth='2')
    mplt.title('Cubed values',color='b')
    mplt.xlabel('basis numbers')
    mplt.ylabel('power numbers')
    mplt.subplot(1, 2, 2)
    mplt.plot(x_values, y_values_divide, marker='o', color='y')
    mplt.title('Divided values', color='y')

    # Show the plot
    mplt.grid(True)
    mplt.style.use('bmh')
    mplt.xlabel('basis numbers')
    mplt.ylabel('divided numbers')
    mplt.show()

    print(mplt.style.available)

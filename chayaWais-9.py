import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = {'Apples': [30], 'Bananas': [21]}
    df = pd.DataFrame(data)

    print(df)
    print()

    data2 = {'Apples': [35, 41], 'Bananas': [21, 34]}
    index = ['2017 sales', '2018 sales']
    df2 = pd.DataFrame(data2, index=index)
    print(df2)
    print()

    data3 = [1, 2, 3, 4]
    index2 = ['a', 'b', 'c', 'd']
    df3 = pd.Series(data3, index2)
    print(df3)
    print()

    data4 = ['4 cups', '1 cup', '2 large', '1 can']
    index3 = ['Flour', 'Milk', 'Eggs', 'Spam']
    df4 = pd.Series(data4, index=index3, name='Dinner')
    print(df4)
    print()

    food = ['Milk', 'Coffe', 'Candy', 'Yogurt']
    randCalories = np.random.randint(50, 1000, size=4)
    randTimes = np.random.randint(1, 4, size=4)
    df5 = pd.DataFrame({
        'Product': food,
        'Calories': randCalories,
        'Times per day': randTimes
    })
    print(df5)

    df6 = pd.DataFrame()
    print(df6)




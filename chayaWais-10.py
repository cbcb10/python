import pandas as pd
import numpy as np

if __name__ == '__main__':
    print()

    customers = np.array([f"customer{i}" for i in range(1, 21)])
    persons = np.random.randint(1, 5, size=20)
    days = np.random.randint(2, 15, 20)
    extras = np.random.randint(400, 1700, 20)
    data = {'Persons': persons, 'Days': days, 'Extras': extras}
    df = pd.DataFrame(data, index=customers)
    df['Paywvat'] = 300 * df['Persons'] + 400 * df['Days'] + df['Extras']
    df['Pay'] = df['Paywvat'] * 1.17
    new_customer = {'Persons': 2, 'Days': 7, 'Extras': 567, 'Paywvat': 5678, 'Pay': 8765}
    new_custore_df = pd.DataFrame([new_customer], index=['Customer21'])
    df = pd.concat([df, new_custore_df])
    print(df)

    highest_extra = df['Extras'].max()
    lowest_day = df['Days'].min()
    count_one_person = (df['Persons'] == 1).sum()
    print()
    print(f"The highest extra is: {highest_extra}")
    print(f"The lowest number of days is: {lowest_day}")
    print(f"Number of transactions that have one person in a room are: {count_one_person}")

    filtered_df = df[df['Paywvat'] > 5000]
    sum_persons = filtered_df['Persons'].sum()

    # Print the names and sum of persons
    print("\nCustomers with Paywvat more than 5000 and the sum of persons:")
    print(filtered_df[['Persons']])

    avg_paywvat = df['Paywvat'].mean()
    print(f"\nThe average price before VAT of all transactions is: {avg_paywvat:.2f}")

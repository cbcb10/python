import random
import numpy as np

import matplotlib.pyplot as mplt

if __name__ == '__main__':
    x = [1, 3, 56, 4, 22, 3, 43, 22, 3, 5, 3, 56]
    y = [2, 65, 34, 32, 35, 32, 25, 56, 2, 43, 32, 23]

    mplt.scatter(x, y, color="blue")
    mplt.show()

    courses = {
        "python": 5,
        "computer organization": 3,
        "cloudC": 7,
        "operation systems": 4,
        "c#": 6
    }

    rand_values = np.random.randint(1, 10, size=len(courses))
    rand_values2 = np.random.randint(1, 10, size=len(courses))

    mplt.figure(figsize=(8, 6))
    mplt.barh(list(courses.keys()), list(courses.values()), color='yellow')
    mplt.xlabel('num of assignments')
    mplt.ylabel('courses names')
    mplt.title('number of assignments of any course to the coming month')
    mplt.show()

    mplt.figure(figsize=(8, 6))
    mplt.bar(list(courses.keys()), list(rand_values), color='r')
    mplt.xlabel('num of assignments')
    mplt.ylabel('courses names')
    mplt.title('number of assignments of any course to the coming month')
    mplt.show()

    mplt.figure(figsize=(8, 6))
    mplt.subplot(1, 2, 1)
    mplt.barh(list(courses.keys()), list(rand_values), color='b')
    mplt.ylabel('courses names')
    mplt.title('number of assignments of any course to the coming month')

    mplt.subplot(1, 2, 2)
    mplt.barh(list(courses.keys()), list(rand_values2), color='pink')
    mplt.xlabel('num of assignments')
    mplt.ylabel('courses names')

    mplt.gca().yaxis.tick_right()
    mplt.gca().yaxis.set_label_position("right")
    mplt.show()

    mplt.figure()
    data = np.random.rand(1000)
    mplt.hist(data, color='white', edgecolor='black')
    mplt.show()

    mplt.figure()
    data = np.random.normal(100, 200, 1000)
    mplt.hist(data, color='black')
    mplt.show()

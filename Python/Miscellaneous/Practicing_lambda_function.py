if __name__ == "__main__":
    a_list = [1, 2, 3, 4, 5]

    # anonymous function lambda
    square = lambda x: x**2
    cube = lambda x: x**3
    print([square(i) for i in a_list])

    # map function in conjunction with lambda function
    print(list(map(square, a_list)))

    # filter function in combination with lambda function
    print(list(filter(lambda x: x%2 != 0, a_list)))

    name_list = ["benjamin franklin", "sanggi lee", "bohwa shin", "thomas jefferson"]

    #anonymous function lambda: 2
    only_last_names = lambda x: x.split()[1]

    # using map function with lambda function #2
    print(list(map(only_last_names, name_list)))

    # using filter function to single out western names from korean ones
    print(list(filter(lambda x: len(x.split()[1]) > 4, name_list)))


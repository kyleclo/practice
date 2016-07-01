def answer(numbers):
    first_pirate = 0
    max_size = 5000

    count = 0
    count_per_pirate = [0] * max_size

    #  Let 'count_per_pirate' save past states of 'count'
    #  Then upon seeing the same pirate again,
    #    'loop_size' = num pirates seen between Now and Prev occurrence
    current_pirate = first_pirate
    while True:
        count += 1

        if count_per_pirate[current_pirate] == 0:
            count_per_pirate[current_pirate] = count

        else:
            loop_size = count - count_per_pirate[current_pirate]
            return loop_size

        current_pirate = numbers[current_pirate]

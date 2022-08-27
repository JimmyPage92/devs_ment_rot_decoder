"""Zad 3.
Napisz funkcję sortującą metodą quick sort listę podanych elementów.
Otestuj jej poprawne działanie."""


def quick_sort(sequence):
    lenght = len(sequence)
    if lenght <= 1:
        return "za malo elementów-",sequence
    else:
        p = sequence.pop()
        # (p) to jest element wg ktorego bedziemy dzielic nasza liste

    nums_greater_than_p = []
    nums_lower_than_p = []

    for elem in sequence:
        if elem > p:
            nums_greater_than_p.append(elem)

        else:
            nums_greater_than_p.append(elem)


    return nums_lower_than_p + [p] + nums_greater_than_p


print(quick_sort([42,20,13,4,80,99,124]))
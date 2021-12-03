from typing import List


def count_greater_than(arr: List[int]) -> int:
    """Count the number greater than.

    Args:
        arr (List[int]): the input data.

    Return:
        int : The number greater than.
    """
    return sum([n > arr[i-1] for i, n in enumerate(arr)])


def count_greater_than_sliding(arr: List[int], n=3) -> int:
    """Count greater than with a sliding window.

    Args:
        arr (List[int]): The input data.
        n (int): the size of the sliding window.

    Return:
        int: the amount greater than.
    """
    return count_greater_than([sum(arr[i:i+n]) for i in range(len(arr)-n+1)])


def read_advent_data(fpath: str) -> List[int]:
    """Read the input data and put in useful data structure.

    Args:
        fpath (str): the path to the file containing input data.

    Return:
        List[int]: the input data in useful data structure.
    """
    return list(
            map(int, map(lambda x: x.strip(), open(fpath, 'r').readlines()))
        )


if __name__ == '__main__':
    # Part 1
    print(count_greater_than(read_advent_data('./data/dec1-1.csv')))

    # Part 2
    print(count_greater_than_sliding(read_advent_data('./data/dec1-2.csv')))

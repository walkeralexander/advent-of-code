from collections import Counter
from typing import List, Union, Dict


def read_advent_data(fpath: str) -> List[Union[str, int]]:
    """Read the input data and convert to a useful data structure.

    Args:
        fpath (str): the path to the file.

    Returns:
        List[Dict[str, int]]: A list of dictionaries keyed by direction str and
            with values of magnitude.
    """
    data = open(fpath, 'r').readlines()
    data = map(lambda x: x.strip().split(), data)
    data = list(map(lambda x: {x[0]: int(x[1])}, data))
    return data


def tabulate_position(data: List[Dict[str, int]]) -> int:
    """Tabulate the position for problem 1.

    Args:
        data (List[Dict[str, int]]): the input data.

    Return:
        int : the position times the depth.
    """
    aggregate = Counter()
    for dd in data:
        aggregate.update(dd)
    return (aggregate['down'] - aggregate['up']) * aggregate['forward']


def tabulate_position2(data: List[Dict[str, int]]) -> int:
    """Tabulate the position for problem 2.

    Args:
        data (List[Dict[str, int]]): the input data.

    Return:
        int : the position times the depth.
    """
    aim, dep, pos = 0, 0, 0
    for dd in data:
        k, v = list(dd.items())[0]
        if k == 'down':
            aim += v
        elif k == 'up':
            aim -= v
        elif k == 'forward':
            pos += v
            dep += v * aim
    return dep * pos


if __name__ == '__main__':
    data = read_advent_data('./data/dec2-1.csv')
    print(tabulate_position(data))

    data = read_advent_data('./data/dec2-2.csv')
    print(tabulate_position2(data))

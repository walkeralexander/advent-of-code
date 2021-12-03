from typing import List
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)


def read_input(fpath: str) -> List[str]:
    data = open(fpath, 'r').readlines()
    data = map(lambda x: x.strip(), data)
    data = map(lambda x: list(map(lambda i: int(i), x)), data)
    return list(data)


def bin2int(arr: np.ndarray) -> int:
    return np.sum(arr * np.power(2, np.arange(arr.shape[0])[::-1]))


def find_power_consumption(data: np.ndarray) -> str:
    gamma = np.median(data, axis=0).astype(bool)
    epsilon = np.invert(gamma)
    return bin2int(gamma) * bin2int(epsilon)


def argmax(arr: np.ndarray) -> int:
    return 1 if (len(arr) > 1) and (arr[0] == arr[1]) else np.argmax(arr)


def life_support(data: np.ndarray, co2: bool=False, i: int=0, idx: np.ndarray=None):
    idx = np.arange(data.shape[0]) if idx is None else idx
    criteria = np.argmin if co2 else argmax
    subset = data[idx, i]
    _, freqs = np.unique(subset, return_counts=True)
    new_idx = idx[np.where(subset == criteria(freqs))[0]]
    return data[new_idx].ravel() if new_idx.shape[0] == 1 else life_support(data, co2, i+1, new_idx)


if __name__ == '__main__':
    # Part 1
    file1 = 'data/dec3-1.csv'
    data = np.array(read_input(file1)).astype(bool)
    power = find_power_consumption(data)
    logging.info(f'Power Consumption is {power}.')

    # Part 2
    file2 = 'data/dec3-2.csv'
    data = np.array(read_input(file2))
    co2 = life_support(data, co2=True)
    oxy = life_support(data, co2=False)
    logging.info(f'Life Support Rating is {bin2int(co2) * bin2int(oxy)}')

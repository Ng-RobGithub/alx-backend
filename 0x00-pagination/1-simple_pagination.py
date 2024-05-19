#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"


def __init__(self):
    """Initializes a new Server instance and loads the dataset."""
    self.__dataset = None
    self.load_dataset()


def dataset(self) -> List[List]:
    """Cached Dataset"""
    if self.__dataset is None:
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            self.__dataset = dataset[1:]
            return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Retrieves a page of data from the dataset."""
    assert isinstance(page, int) and isinstance(page_size, int)
    assert page > 0 and page_size > 0

    start, end = self.index_range(page, page_size)
    return self.__dataset[start:end]


@staticmethod
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indices for the given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


if __name__ == "__main__":
    server = Server()
    page_data = server.get_page(1, 10)
    print(page_data)

#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"


def __init__(self):
    """Initializes a new Server instance and loads the dataset."""
    self.__dataset = None


def dataset(self) -> List[List]:
    """Cached Dataset"""
    if self.__dataset is None:
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            self.__dataset = dataset[1:]
            return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Get a page of the dataset.

        Args:
            page (int): The page number to retrieve. Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: The requested page of the dataset.
                        An empty list if the page is out of range.
        """
    assert isinstance(page, int) and page > 0
    "page must be a positive integer "
    assert isinstance(page_size, int) and page_size > 0
    "page size must bepositive integer"

    dataset = self.dataset()
    total_items = len(dataset)
    total_pages = math.ceil(total_items / page_size)

    if page < 1 or page > total_pages:
        return []

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return dataset[start_index:end_index]

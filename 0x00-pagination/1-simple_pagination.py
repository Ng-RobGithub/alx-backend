#!/usr/bin/env python3
""" Simple Pagination """
import csv
from typing import List

# Corrected import statement for the helper function
from simple_helper_function import index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"


def __init__(self):
    self.__dataset = None


def dataset(self) -> List[List]:
    """Cached dataset"""
    if self.__dataset is None:
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
            return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Get the page of the dataset"""
    assert type(page) is int and page > 0
    assert type(page_size) is int and page_size > 0

    start, end = index_range(page, page_size)
    return self.dataset()[start:end]

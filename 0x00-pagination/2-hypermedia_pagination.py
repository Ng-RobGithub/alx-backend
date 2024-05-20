#!/usr/bin/env python3
"""
Hypermedia Pagination Module
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"


def __init__(self):
    self.__dataset = None


def dataset(self) -> List[List]:
    """Cached dataset
    """
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
    "Page must be a positive integer"
    assert isinstance(page_size, int) and page_size > 0
    "Page size must be a positive integer"

    dataset = self.dataset()
    total_items = len(dataset)
    total_pages = math.ceil(total_items / page_size)

    if page < 1 or page > total_pages:
        return []

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return dataset[start_index:end_index]


def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
    """Get a page of the dataset with hypermedia pagination.

    Args:
    page (int): The page number to retrieve. Default is 1.

    page_size (int): The number of items per page. Default is 10.

    Returns:

    Dict: A dictionary containing the following key-value pairs:
    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
    """
    dataset = self.get_page(page, page_size)

    total_items = len(self.dataset())
    total_pages = math.ceil(total_items / page_size)

    next_page = page + 1 if page < total_pages else None
    prev_page = page - 1 if page > 1 else None

    return {
        'page_size': len(dataset),
        'page': page,
        'data': dataset,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages
        }

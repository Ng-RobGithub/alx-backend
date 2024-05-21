0x01-caching

What is Caching?
Caching involves storing copies of data in a temporary storage location, or cache, so that subsequent requests for that data can be served more quickly. 
Types of Caches:
1. Memory Cache (RAM Cache): Stores data in the system’s main memory (RAM).
2. Disk Cache: Stores data on a disk, like an SSD or HDD.
3. CPU Cache: Small, high-speed memory located inside the CPU.
4. Web Cache: Stores web documents (HTML pages, images) to reduce server load, bandwidth usage, and perceived lag.
5. Application Cache: Used by applications to store frequently accessed data to improve performance. 
Purpose of a Caching System:
1. Improves Performance 2. Reduces Latency 3. Minimizes Network Load 4. Enhances Scalability
Cache Replacement Policies:
1. FIFO (First In, First Out). 2. LIFO (Last In, First Out). 3. LRU (Least Recently Used)
4. MRU (Most Recently Used) 5. LFU (Least Frequently Used)
TASKS
0. Basic dictionary
Create a class BasicCache that inherits from BaseCaching and is a caching system
1. FIFO caching
Create a class FIFOCache that inherits from BaseCaching and is a caching system
2. LIFO Caching
Create a class LIFOCache that inherits from BaseCaching and is a caching system
3. LRU Caching
Create a class LRUCache that inherits from BaseCaching and is a caching system
4. MRU Caching
Create a class MRUCache that inherits from BaseCaching and is a caching system:
5. LFU Caching
Create a class LFUCache that inherits from BaseCaching and is a caching system:

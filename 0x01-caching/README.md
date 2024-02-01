# Advanced Caching Systems Project

## Description
This project is a Python-based caching system implementing various strategies like FIFO, LIFO, LRU, MRU, and Basic caching. It's designed to showcase different data management techniques and their applications in optimizing software performance.

## Installation
To set up the project:
1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd [project directory]`
3. Run the script: `python3 <script_name>.py`

## Usage
You can interact with the caching system through the command line. Here are some common commands:
- `put <key> <value>`: Adds an item to the cache.
- `get <key>`: Retrieves an item from the cache.
- `show`: Displays the current state of the cache.

## Caching Strategy Explanations
- **Basic Caching:** A simple caching system without any limit.
- **FIFO (First In, First Out):** Discards the oldest cache entry first.
- **LIFO (Last In, First Out):** Discards the most recently added entry first.
- **LRU (Least Recently Used):** Discards the least recently used entry first.
- **MRU (Most Recently Used):** Discards the most recently used entry first.

Each strategy is beneficial in different scenarios, depending on the specific needs of data access patterns.

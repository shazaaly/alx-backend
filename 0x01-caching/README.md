# ALX Software Engineering Program - Caching Systems

This repository contains a collection of Python implementations of caching systems developed as part of the ALX Africa Software Engineering program, Cohort 13.

![ALX Africa Logo](https://www.alx.app/static/media/logo.dc354d89.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Tasks](#tasks)
3. [Usage](#usage)
4. [Repository Structure](#repository-structure)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

Implementing various caching systems using Python. These caching systems are designed to demonstrate your understanding of different caching algorithms, including Basic Cache, FIFO Cache, LIFO Cache, LRU Cache, and LFU Cache.

This repository serves as a collection of  implementations for each caching system. Each task is structured as a separate Python script with its respective class definition and logic.

## Tasks

Here is a list of the caching systems implemented in this repository:

1. **Task 0: Basic Cache**
   - Create a class `BasicCache` that inherits from `BaseCaching`.
   - This caching system doesn't have a limit.
   - Implement the `put` method to assign the item value for the given key.
   - Implement the `get` method to return the value linked to the key.

2. **Task 1: FIFO Cache**
   - Create a class `FIFOCache` that inherits from `BaseCaching`.
   - Implement the `put` method to assign the item value for the given key.
   - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the first item (FIFO algorithm).
   - Implement the `get` method to return the value linked to the key.

3. **Task 2: LIFO Cache**
   - Create a class `LIFOCache` that inherits from `BaseCaching`.
   - Implement the `put` method to assign the item value for the given key.
   - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the last item (LIFO algorithm).
   - Implement the `get` method to return the value linked to the key.

4. **Task 3: LRU Cache**
   - Create a class `LRUCache` that inherits from `BaseCaching`.
   - Implement the `put` method to assign the item value for the given key.
   - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the least recently used item (LRU algorithm).
   - Implement the `get` method to return the value linked to the key.

5. **Task 4: MRU Cache**
   - Create a class `MRUCache` that inherits from `BaseCaching`.
   - Implement the `put` method to assign the item value for the given key.
   - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the most recently used item (MRU algorithm).
   - Implement the `get` method to return the value linked to the key.

6. **Task 5: LFU Cache (Advanced)**
   - Create a class `LFUCache` that inherits from `BaseCaching`.
   - Implement the `put` method to assign the item value for the given key.
   - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the least frequency used item (LFU algorithm).
   - If multiple items have the same least frequency, use the LRU algorithm to discard the least recently used item.
   - Implement the `get` method to return the value linked to the key.


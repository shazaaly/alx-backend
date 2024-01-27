


def get_paginated_data(page, page_size, total_items):
    data = fetch_data(page, page_size)  # Your function to get the data
    last_page = math.ceil(total_items / page_size)

    hypermedia = {
        "self": f"http://example.com/data?page={page}&page_size={page_size}",
        "first": f"http://example.com/data?page=1&page_size={page_size}",
        "last": f"http://example.com/data?page={last_page}&page_size={page_size}",
        "next": f"http://example.com/data?page={page + 1}&page_size={page_size}" if page < last_page else None,
        "prev": f"http://example.com/data?page={page - 1}&page_size={page_size}" if page > 1 else None
    }

    return {"data": data, "pagination": hypermedia}

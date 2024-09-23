from math import ceil

def get_total_pages(total_items, per_page):

    return ceil(total_items / per_page)

def paginate_list(items, page, per_page):
    if len(items) == 0:
        return []
    start = (page - 1) * per_page
    end = (page * per_page) 
    return items[start:end]
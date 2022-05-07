# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

        ...

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        items = self.item_count()
        page_items = self.items_per_page

        if (items % page_items) == 0:
            return items / page_items

        else:

            return (items // page_items) + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        print(f'page_index: {page_index}', f'page_count: {self.page_count()}', f'collection: {self.collection}')
        if (page_index > self.page_count() -1) or page_index < 0:
            return -1
        elif page_index == self.page_count()-1:
            if (self.item_count() % self.items_per_page) == 0:
                return self.items_per_page
            else:
                return self.item_count() % self.items_per_page
        print('final else')
        return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        print(f'item_index: {item_index}', f'page_count: {self.page_count()}', f'collection: {self.collection}')
        if not self.collection or (item_index >self.item_count()-1):
            return -1
        print(item_index, self.item_count()-1, 'dd')
        if 0 < item_index <= self.items_per_page:
            return 0
        elif (item_index > self.item_count()-1) or item_index < 0:
            return -1
        else:
            res = item_index // self.items_per_page
            return res


collection = range(1, 25)
heper = PaginationHelper(collection, 10)

print(heper.page_count(), 'page_count')
print(heper.page_item_count(3), 'page_item_count')
print(heper.page_index(24),'page_index')

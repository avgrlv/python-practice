class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}

    @property
    def cache(self):
        least_recently_used = next(iter(self.cache_dict))
        return least_recently_used, self.cache_dict[least_recently_used]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            del self.cache_dict[key]
        elif len(self.cache_dict) == self.capacity:
            del self.cache_dict[next(iter(self.cache_dict))]
        self.cache_dict[key] = value

    def get(self, key):
        if key in self.cache_dict:
            value = self.cache_dict[key]
            del self.cache_dict[key]
            self.cache_dict[key] = value
            return value

    def print_cache(self):
        print("Текущий кэш:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

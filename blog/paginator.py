class Pagination:
    def __init__(self, posts, per_page):
        self.posts = posts
        self.per_page = per_page
        self.result = self.pagination()
        self.pager = len(self.result)

    def pagination(self):
        res = []
        for i in range(0, len(self.posts), self.per_page):
            r = []
            for j in range(i, i + self.per_page):
                if j >= len(self.posts):
                    break
                r.append(self.posts[j])
            res.append(r)
        return res

    def get_page(self, page_number: int):
        if page_number >= self.pager:
            return self.result[-1]
        return self.result[page_number - 1]


    def the_last(self,last):
        if last == self.pager:
            return True
        return False

    def the_first(self, first):
        if first == 1:
            return True
        return False

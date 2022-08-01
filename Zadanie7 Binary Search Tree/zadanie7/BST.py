import collections


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def wstaw(self, value):
        if value == self.value:
            return  # jeśli node już istnieje

        if value < self.value:
            if self.left:
                self.left.wstaw(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.wstaw(value)
            else:
                self.right = BSTNode(value)

    def szukaj(self, value):
        if self.value == value:
            return True

        if value < self.value:
            if self.left:
                return self.left.szukaj(value)
            else:
                return False

        if value > self.value:
            if self.right:
                return self.right.szukaj(value)
            else:
                return False


    def usun(self, val):
        if val < self.value:
            if self.left:
                self.left = self.left.usun(val)
        elif val > self.value:
            if self.right:
                self.right = self.right.usun(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.value = min_val
            self.right = self.right.usun(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.value
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.value
        return self.left.find_min()


    def drukuj(self):
        elements = []
        if self.left:
            elements += self.left.drukuj()

        elements.append(self.value)

        if self.right:
            elements += self.right.drukuj()

        return elements


def level_order(tree):
    result = []

    # zwraca Null jeśli drzewo jest puste
    if tree is None:
        return result

    # inicjalizacja kolejki
    queue = collections.deque()
    queue.append(tree)

    # iterowanie po kolejce póki nie jest pusta
    while queue:
        currSize = len(queue)
        currList = []

        while currSize > 0:
            # usunięcie elementu z kolejki
            currNode = queue.popleft()
            currList.append(currNode.value)
            currSize -= 1

            if currNode.left is not None:
                queue.append(currNode.left)
            if currNode.right is not None:
                queue.append(currNode.right)

        # dodawanie currList do wyniku po każdej iteracji
        result.append(currList)

    return result


def build_tree(elements):
    root = BSTNode(elements[0])

    for i in range(1,len(elements)):
        root.wstaw(elements[i])

    return root


with open('data.txt') as f:
    for line in f:
        tab = [i for i in line.split()]


# 500
tab500 = [tab[i] for i in range(0, 500)]
tree500 = build_tree(tab500)
result500 = level_order(tree500)
print('\nWydruk kontrolny 5 pierwszych poziomów drzewa:\n')
for i in range(0, 5):
    print(result500[i])
height500 = len(result500)
# 1000
tab1000 = [tab[i] for i in range(0, 1000)]
tree1000 = build_tree(tab1000)
result1000 = level_order(tree1000)
height1000 = len(result1000)
# 2000
tab2000 = [tab[i] for i in range(0, 2000)]
tree2000 = build_tree(tab2000)
result2000 = level_order(tree2000)
height2000 = len(result2000)
print("\nWysokość drzewa zawierającego 500 słów:", height500)
print("Wysokość drzewa zawierającego 1000 słów:", height1000)
print("Wysokość drzewa zawierającego 2000 słów:", height2000)

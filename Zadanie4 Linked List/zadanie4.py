# Lista dwukierunkowa, niecykliczna, bez wartownika
class Node:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def wstaw(self, y):
        x = Node(y)
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def drukuj(self):
        temp = self.head
        while (temp):
            print(temp.key)
            temp = temp.next

    def szukaj(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x
    # None - elementu nie ma na liście
    def usun(self, x):
        temp = self.head
        while temp is not None:
            if temp.key == x:
                if temp.prev is None:
                    if temp.next is not None:
                        temp.next.prev = None
                        self.head = temp.next
                    else:
                        self.head = None
                elif temp.next is None:
                    temp.prev.next = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                break
            else:
                temp = temp.next

    def odwroc(self):
        if (self.head is not None):
            prevNode = self.head
            curNode = self.head.next
            prevNode.next = None
            prevNode.prev = None

            while (curNode != None):
                tempNode = curNode.next
                curNode.next = prevNode
                prevNode.prev = curNode
                prevNode = curNode
                curNode = tempNode
            self.head = prevNode


def bezpowtorzen(L):
        L2 = LinkedList()
        temp = L.head
        while temp is not None:
            if L2.szukaj(temp.key) is None:
                L2.wstaw(temp.key)
            temp = temp.next
        L2.odwroc()
        return L2

def scal(L1, L2):
    L2.odwroc()
    temp = L2.head
    while temp is not None:
        L1.wstaw(temp.key)
        temp = temp.next
    return L1



# L1 = LinkedList()
# L1.wstaw('abc')
# L1.wstaw('Ala')
# L1.wstaw('abc')
# L1.wstaw('Ala')
# L1.wstaw('ma')
# L1.wstaw('kota')
# L1.wstaw('psa')
# L1.wstaw('i')
# L1.wstaw('psa')
# L1.wstaw('oraz')
# L1.wstaw('chomika')
# L1.drukuj()
# L1.usun('i')
# L1.drukuj()
# k = L1.szukaj('ma')
# print(k)
# print(k.key)
# bezpowtorzen(L1).drukuj()
# L2 = bezpowtorzen(L1)
# scal(L1, L2).drukuj()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next
    
    def setValue(self, value):
        self.value = value
    
    def setNext(self, new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        temp = Node(value)
        if self.head == self.tail:
            self.tail = temp
        temp.setNext(self.head)
        self.head = temp

    def append(self, value):
        temp = Node(value)
        self.tail.setNext(temp)
        self.tail = temp

    def add_after(self, prev_node, value):
        temp = Node(value)
        temp.setNext(prev_node.getNext())
        prev_node.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, value):
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        
        return found

    def remove(self, value):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getValue() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def print_list(self):
        current = self.head
        values = []
        while current != None:
            values.append(current.getValue())
            current = current.getNext()
        print(' '.join(map(str, values)))


def shuffle_linked_list(linkedlist):
    '''
        Complexity - O(n^2).
        
        Input:
        linkedlist: UnorderedList
        Output:
        Parsed parameters in the form of list of pairs (param_name, param_value).
    '''
    # пытаемся вставить с между a и b
    a = linkedlist.head
    b = linkedlist.head.getNext()
    b_index = 2
    n = linkedlist.size()
    for i in range(n, (n + 1) / 2, -1):
        c = b
        for _ in range(b_index, i):
            c = c.getNext()
        c.setNext(b)
        a.setNext(c)
        a = b
        b = b.getNext()
        b_index += 1
    b.getNext().setNext(None)
    return linkedlist


# Example
my_list = UnorderedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.add(6)

mylist.print_list()
# 6 5 4 3 2 1
shuffle_linked_list(mylist).print_list()
# 6 1 5 2 4 3
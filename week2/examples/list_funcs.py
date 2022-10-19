#!/usr/bin/bash


from typing import List


def main():
    # list_append_example()
    # list_insert_example()
    # list_remove_example()
    # list_pop_example()
    pass

def list_append_example():
    app_list = ["apple",1,"orange",True,"grapes"]
    print("\t",app_list)
    app_list.append("pear")
    print("pear\t",app_list)
    app_list.append("guava")
    print("guava\t",app_list)
    app_list.append(0)
    print("0\t",app_list)
    app_list.append(True)
    print("True\t",app_list)

def list_insert_example():
    ins_list = ["apple","cherries","banana","orange","grapes"]
    print("\t",ins_list)
    ins_list.insert(0,"pear")
    print("pear\t",ins_list)
    ins_list.insert(1,"guava")
    print("guava\t",ins_list)


def list_remove_example():
    rmv_list = ["apple","apple","cherries","banana","banana","orange"]
    print("\t",rmv_list)
    rmv_list.remove("cherries")
    print("-cherries\t",rmv_list)
    rmv_list.remove("apple")
    print("-apple\t",rmv_list)
    rmv_list.remove("apple")
    print("-apple\t",rmv_list)

def list_pop_example():
    pop_list = ["apple","cherries","banana","orange","grapes","pear","guava","durian"]
    print("\t",pop_list)
    popped = pop_list.pop()
    print("pop()\t",pop_list)
    popped = pop_list.pop()
    print("pop()\t",pop_list)
    popped = pop_list.pop(0)
    print("pop(0)\t",pop_list)
    mid = len(pop_list)//2
    popped = pop_list.pop(mid)
    print("pop mid\t",pop_list)
    pop_list.clear()
    print("cleared\t",pop_list)

if __name__ == "__main__":
    main()
#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list1 = dir(hidden_4)
    for name in list1:
        if name[:2] != "__":
            print(name)

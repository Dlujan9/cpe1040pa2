if __name__ == '__main__':
    def cap_join():
        cap_list = []
        cap_list.append("calvin")
        cap_list.append("and")
        cap_list.append("hobbes")
        cap_list.append("are")
        cap_list.append("the")
        cap_list.append("first")
        cap_list.append("spacemen")
        cap_list.append("on")
        cap_list.append("mars")

        print(" ".join(cap_list))
        cap_new = " ".join(cap_list)
        cap_new = cap_new.title()

        print(cap_new)

if __name__ == '__main__':
    cap_join()


# You can also use this shorter code
if __name__ == '__main__':
    def cap_join():
        cap_list = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"]

        print(" ".join(cap_list))
        cap_new = " ".join(cap_list)
        cap_new = cap_new.title()

        print(cap_new)


if __name__ == '__main__':
    cap_join()
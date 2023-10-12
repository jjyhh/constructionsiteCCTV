def Press_Enter_to_Continue1():
    print("")
    input("\tPress Enter Key to Continue . . .")
    print("")


def Press_Enter_to_Continue2():
    import os

    os.system('pause')


if __name__ == '__main__':
    print("****START****")

    print("방법 1" + "=" * 100)
    Press_Enter_to_Continue1()

    print("방법 2" + "=" * 100)
    Press_Enter_to_Continue2()

    print("****END****")
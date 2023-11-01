class BaiHat:
    def __init__(self, tenBH, url):
        self.tenBH = tenBH
        self.url = url


def inputSong():
    tenBH = input("Nhap ten bai hat: ")
    url = input("Nhap url bai hat: ")
    bh = BaiHat(tenBH, url)
    # print("Done!")
    return bh


def inputSongs():
    list = []
    i = 0
    n = int(input("Nhap so luong bai hat: "))
    while (True):
        if (i >= n):
            break
        list.append(inputSong())
        i += 1
    return list


def addFile(bh, file):
    # with open("playlists.txt", "w") as file:
    file.write((bh.tenBH) + "\n")
    file.write((bh.url) + "\n")


def addListToFile(list):
    with open("playlists.txt", "w") as file:
        n = len(list)
        file.write(str(n) + "\n")
        for i in range(n):
            addFile(list[i], file)


def readFile(file):
    # with open("playlists.txt", "r") as file:
    tenBH = file.readline()
    url = file.readline()
    bh = BaiHat(tenBH, url)
    return bh


def readLists():
    list = []
    with open("playlists.txt", "r") as file:
        n = int(file.readline())
        for i in range(n):
            bh = readFile(file)
            list.append(bh)
        return list


def printSong(name):
    print("Ten bai hat: ", name.tenBH, end="")
    print("url bai hat: ", name.url, end="")


def printlists(list):
    n = len(list)
    for i in range(n):
        printSong(list[i])


def main():
    # bh = inputSong()
    # addFile(bh)
    # bh2 = readFile()
    # printSong(bh2)

    bh = inputSongs()
    addListToFile(bh)
    bh2 = readLists()
    printlists(bh2)


main()

import os
import random
import csv
import glob


def getEntries(path_shuffled):
    pathCSV = "basi-yarasi-dataset/BasiYarasiListes-formatted.csv"
    fileCSV = open('BasiYarasiListes-formatted-shuffled.csv', 'w', newline='\n')

    writer = csv.writer(fileCSV)
    # for (dirpath, dirnames, filenames) in os.walk(path_shuffled):
    #     # file_list = os.path.splitext(filenames)[0]
    #     print(filenames)

    indices = []
    file_list = glob.glob(path_shuffled + "*")
    for f in file_list:
        base = os.path.basename(f)
        indices.append(os.path.splitext(base)[0])

    print(len(indices))

    # with open(pathCSV, encoding="utf8", errors='ignore') as f:
    #     for row in csv.reader(f):
    #         # print(file_list)
    #         writer.writerow(row)

def main():
    # path = "basi-yarasi-dataset"
    # if not os.path.exists("/shuffled-dataset"):
    #     os.system('mkdir shuffled-dataset')
    #
    # count = 0
    # while count < 540:
    #     file = random.choice(os.listdir(path))
    #     print(file)
    #     # os.system('cp basi-yarasi-dataset/{} shuffled-dataset/'.format(file))
    #     os.system("cp basi-yarasi-dataset/" + file + " shuffled-dataset/" )
    #     count += 1
    getEntries("shuffled-dataset/")


if __name__ == "__main__":
    main()
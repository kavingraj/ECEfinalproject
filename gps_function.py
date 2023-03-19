import pandas as pd

def gps(path):
    if path == '001':
        csvfile1 = pd.read_csv('path1.csv')
        print(csvfile1)
        return False
    elif path == '002':
        csvfile2 = pd.read_csv('path2.csv')
        print(csvfile2)
        return False
    elif path == '003':
        csvfile3 = pd.read_csv('path3.csv')
        print(csvfile3)
        return False
    else:
        print('NOTHING!!!')
    return True

if __name__ == '__main__':
    gps(decoded_text)

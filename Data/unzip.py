import zipfile
import os

def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir("data"):
        pass
    else:
        os.mkdir("data")
    for names in zip_file.namelist():
        zip_file.extract(names,"data")
    zip_file.close()

if __name__ == '__main__':
    file = 'D:/GLA Lessons/MSc Project/Data/test/data.zip'
    un_zip(file)

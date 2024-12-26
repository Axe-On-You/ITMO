from json import loads
from dicttoxml import dicttoxml
import codecs


def json2xml(string):
    return dicttoxml(loads(string), attr_type=False, return_bytes=False)

if __name__ == "__main__":
    with codecs.open("C://Users/pmih0/Desktop/Информатика/Лабораторные/Лабораторная 4/data/in.json", "r", "utf_8_sig") as f:
        data = f.read()
    with codecs.open("C://Users/pmih0/Desktop/Информатика/Лабораторные/Лабораторная 4/data/out2.xml", "w", "utf_8_sig") as f:
        print(json2xml(data), file=f)
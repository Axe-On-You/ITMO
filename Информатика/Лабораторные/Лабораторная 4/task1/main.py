from json_parser import parse_json, dump2xml
import codecs


if __name__ == "__main__":
    with codecs.open("C://Users/pmih0/Desktop/Информатика/Лабораторные/Лабораторная 4/data/in.json", "r", "utf_8_sig") as f:
        data = f.read()
    with codecs.open("C://Users/pmih0/Desktop/Информатика/Лабораторные/Лабораторная 4/data/out1.xml", "w", "utf_8_sig") as f:
        header = '<?xml version="1.0" encoding="UTF-8" ?>'
        print(header+dump2xml(parse_json(data)), file=f)
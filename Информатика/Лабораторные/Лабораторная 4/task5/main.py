import sys
import codecs

sys.path.append("C://Users/pmih0/Desktop/Информатика/Лабораторные/Лабораторная 4")

import time
from task1.json_parser import parse_json, dump2xml
from task2.main import json2xml
from task3.json_parser_re import parse_json as parse_json_regex


main_task_parser = lambda x: dump2xml(parse_json(x))
regex_task_parser = lambda x: dump2xml(parse_json_regex(x))


def test(f, string):
    start_time = time.time()
    for _ in range(100):
        f(string)
    return time.time() - start_time


if __name__ == "__main__":
    with codecs.open("C://Users/pmih0/Desktop/Информатика/Лабораторные/Лабораторная 4/data/in.json", "r", "utf_8_sig") as f:
        data = f.read()

    print(
        f"Own Parser: {test(main_task_parser, data)} seconds",
        f"Own Parser with Regex: {test(regex_task_parser, data)} seconds",
        f"Python JSON Lib + dicttoxml: {test(json2xml, data)} seconds",
        sep="\n",
    )


"""
1. 通过 with 可以自动关闭文件流
2. open打开文件的几种模式，
r 只读，
w只写（会清空原本的内容）
r+ 可读可写,
w+
a  追加，文件尾追加
"""

with open("a.txt","r") as f:
    text = f.read()

print(text)
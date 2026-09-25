# 파이썬 기초 10: 파일 읽고 쓰기 (임시 파일 사용 후 삭제)
import os
import tempfile

path = os.path.join(tempfile.gettempdir(), "study_demo.txt")

with open(path, "w", encoding="utf-8") as f:
    f.write("첫째 줄\n")
    f.write("둘째 줄\n")

with open(path, "a", encoding="utf-8") as f:
    f.write("셋째 줄\n")

with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())

os.remove(path)
print("삭제 완료:", not os.path.exists(path))

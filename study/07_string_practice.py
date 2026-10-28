# 파이썬 기초 7: 문자열 연습

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")


def reverse_words(s):
    return " ".join(reversed(s.split()))


print(is_palindrome("Never odd or even"))
print(is_palindrome("Python"))
print(count_vowels("Hello World"))
print(reverse_words("I love python"))
print("a,b,c".split(","), "-".join(["2026", "10", "28"]))
print("  strip me  ".strip(), "python".capitalize(), "abc".startswith("a"))

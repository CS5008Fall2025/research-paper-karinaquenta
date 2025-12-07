"""
Added a small demo script to show how the rabin_karp function works.
This is a helper for running my examples.
"""

from rabin_karp import rabin_karp

def demo():
    text = "abracadabra"
    pattern = "abra"
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    result = rabin_karp(text, pattern)
    print(f"Matches found at indices: {result}")

    text2 = "aaaaa"
    pattern2 = "aa"
    print("\nSecond example:")
    print(f"Text:    {text2}")
    print(f"Pattern: {pattern2}")
    print(f"Matches found at indices: {rabin_karp(text2, pattern2)}")

if __name__ == "__main__":
    demo()
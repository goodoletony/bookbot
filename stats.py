def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()


def get_word_count(text: str) -> int:
    return len(text.split())



def get_char_count(text: str) -> dict[str, int]:
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1    
    return counts


def sort_chars(char_counts):
    items = [{"char": ch, "num": n} for ch, n in char_counts.items()]
    items.sort(key=lambda d: d["num"], reverse=True)
    return items

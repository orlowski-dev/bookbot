def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict:
    result = {}

    for word in text.split():
        for char in word:
            tmp = char.lower()
            if tmp in result:
                result[tmp] += 1
            else:
                result[tmp] = 1

    return result


def sort_on(items):
    return items["num"]


def sort_dict(data: dict) -> list:
    new_list = []

    for k, v in data.items():
        new_list.append({"char": k, "num": v})

    new_list.sort(reverse=True, key=sort_on)

    return new_list

def char_count(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = {}
    lower = str.lower()
    for c in lower:
        if c not in alphabet:
            continue
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

def main():
    filename = 'books/frankenstein.txt'
    contents = None

    with open(filename) as f:
        contents = f.read()

    chars = char_count(contents)

    print(f"--- Begin report of {filename} ---")
    print(f"{len(contents.split())} words found in the document")
    print('\n'.join([f"The '{k}' character was found {v} times" for k, v in chars.items()]))
    print("--- End report ---")

main()

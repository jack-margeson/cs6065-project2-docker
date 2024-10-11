import os
import re
from collections import Counter
import socket


def count_words(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    words = re.findall(r"\b\w+\b", text)
    return len(words), Counter(words)


def handle_contractions(text):
    contractions = {
        "it's": "it is",
        "couldn't": "could not",
        "i'm": "I am",
        "can't": "can not",
        "won't": "will not",
        "i'll": "I will",
        "you're": "you are",
        "that's": "that is",
    }
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text


def main():
    data_dir = "./"
    files = ["IF.txt", "AlwaysRememberUsThisWay.txt"]
    total_word_count = 0
    word_counts = {}

    for file in files:
        file_path = os.path.join(data_dir, file)
        word_count, counter = count_words(file_path)
        total_word_count += word_count
        word_counts[file] = counter

    # Top 3 words in IF.txt
    top_3_if = word_counts["IF.txt"].most_common(3)

    # Handle contractions and find top 3 words in AlwaysRememberUsThisWay.txt
    with open(os.path.join(data_dir, "AlwaysRememberUsThisWay.txt"), "r") as file:
        text = file.read()
    text = handle_contractions(text)
    words = re.findall(r"\b\w+\b", text)
    counter = Counter(words)
    top_3_always_remember = counter.most_common(3)

    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Write results to result.txt
    with open(os.path.join(data_dir, "output/" "result.txt"), "w") as result_file:
        for file, counter in word_counts.items():
            result_file.write(f"Total word count in {file}: {sum(counter.values())}\n")
        result_file.write(f"Total word count across both files: {total_word_count}\n")
        result_file.write(f"Top 3 words in IF.txt: {top_3_if}\n")
        result_file.write(
            f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_3_always_remember}\n"
        )
        result_file.write(
            f"IP address of the machine running the container: {ip_address}\n"
        )

    # Print the contents of result.txt
    with open(os.path.join(data_dir, "output/" "result.txt"), "r") as result_file:
        print(result_file.read())


if __name__ == "__main__":
    main()

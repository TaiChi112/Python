import threading
import time
def has_duplicate(words):
    """
    Checks if there are any duplicate words in the list.
    Returns a tuple (True, word) if a duplicate is found, otherwise (False, None).
    """
    for index, word in enumerate(words):
        if word in words[index + 1:]:
            return True, word
    return False, None

## Without list comprehension
def find_bad_words(file_path, bad_words_count):
    bad_word_lines = []
    line_number = 1
    try:
        print('Thread1 Start working')
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                words_in_line = [word.strip('.?",\'').lower() for word in line.strip().split()]
                found_bad_word = False
                for bad_word in bad_words_count:
                    count_in_line = words_in_line.count(bad_word)
                    if count_in_line > 0:
                        bad_words_count[bad_word] += count_in_line
                        found_bad_word = True
                if found_bad_word:
                    bad_word_lines.append(line_number)
                line_number += 1
            for word, count in bad_words_count.items():
                print(f'{word}: {count} words')
            print(bad_word_lines)
            print('Thread1 Finished working')
    except Exception as e:
        print(e.__class__)


def find_repeat_lines_with_duplicates(file_path):
    duplicate_lines = []
    line_number = 1
    try:
        print('Thread2 Starts working')
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                words_in_line = [word.strip('.?,"\'').lower() for word in line.strip().split()]
                has_dup, dup_word = has_duplicate(words_in_line)
                if has_dup:
                    duplicate_lines.append(line_number)
                line_number += 1
                time.sleep(0.04)
            print(duplicate_lines)
            print('Thread2 Finished working')
    except Exception as e:
        print(e.__class__)


def find_lines_exceeding_limit(file_path, word_limit):
    lines_exceeding_limit = []
    line_number = 1
    try:
        print('Thread3 Starts working')
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                words = [word.strip('.?",\'').lower() for word in line.strip().split()]
                if len(words) > word_limit:
                    lines_exceeding_limit.append(line_number)
                line_number += 1
                time.sleep(0.08)
            print(lines_exceeding_limit)
            print('Thread3 Finished working')
    except Exception as e:
        print(e.__class__)


# Set the word limit per line
word_limit = 12

# Dictionary to count occurrences of each bad word
bad_words_count = {
    'fuck': 0,
    'bitch': 0,
    'cunt': 0,
    'damn': 0,
    'asshole': 0
}

# Path to the input file
input_file_path = './Assignment1/badword.txt'

# Create threads for each processing function
thread_find_bad_words = threading.Thread(
    target=find_bad_words,
    args=(input_file_path, bad_words_count)
)
thread_find_duplicate_lines = threading.Thread(
    target=find_repeat_lines_with_duplicates,
    args=(input_file_path,)
)
thread_find_lines_exceeding_limit = threading.Thread(
    target=find_lines_exceeding_limit,
    args=(input_file_path, word_limit)
)

# Start all threads
thread_find_bad_words.start()
thread_find_duplicate_lines.start()
thread_find_lines_exceeding_limit.start()

# Wait for all threads to finish
thread_find_bad_words.join()
thread_find_duplicate_lines.join()
thread_find_lines_exceeding_limit.join()
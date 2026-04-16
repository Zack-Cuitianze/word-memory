import argparse


def memorize_words(words):
    print("Starting memorization process...")
    for word in words:
        input(f"Memorize this word: {word}")
    print("Good luck with your memorization!")


def main():
    parser = argparse.ArgumentParser(description='Word Memorization CLI')
    parser.add_argument('words', nargs='+', help='Words to memorize')
    args = parser.parse_args()
    memorize_words(args.words)


if __name__ == '__main__':
    main()
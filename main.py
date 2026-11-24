import os


JOKE = "I asked my suitcase why it wouldn't close. It said, 'You won't read six novels in three days.' I took out the underwear."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(JOKE)
    print(len(JOKE))


if __name__ == "__main__":
    main()

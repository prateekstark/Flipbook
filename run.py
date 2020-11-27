import argparse
from book import Book


def main():
    parser = argparse.ArgumentParser(prog="flipc")
    parser.add_argument(
        "flip_filename",
        metavar="flip_filename",
        type=str,
        help="It is the flipbook file!",
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        metavar="output_filename",
        type=str,
        default="output.pdf",
    )
    parser.add_argument("-printbook", action="store_true", default=False)
    args = parser.parse_args()

    book = Book()
    book.read_flipbook("human_life_span.flip")

    if args.printbook:
        book.printbook()

    if ".gif" in args.output_filename:
        book.write_gif(args.output_filename)
    elif ".pdf" in args.output_filename:
        book.write_pdf(args.output_filename)
    else:
        print("Only supported extensions are gif and pdf!")

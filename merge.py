import argparse
from PyPDF2 import PdfMerger


def merge_pdfs(input_file_paths, output_file_path):
    result = PdfMerger()
    for file_path in input_file_paths:
        try:
            with open(file_path, "rb") as input_file:
                result.append(input_file)
        except FileNotFoundError:
            print(f"wrong input file path: {file_path}")
            exit(1)
    with open(output_file_path, "wb") as output_path:
        result.write(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This is an util to merge two pdf files into one"
    )

    required = parser.add_argument_group("required arguments")
    required.add_argument(
        "--input",
        "-i",
        required=True,
        nargs="+",
        type=str,
        help="A required input file path",
    )
    required.add_argument(
        "--output", "-o", required=True, type=str, help="A required output file path"
    )

    args = parser.parse_args()

    merge_pdfs(args.input, args.output)

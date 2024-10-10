import argparse

parser = argparse.ArgumentParser(description="Mitt script")


parser.add_argument("name", help="Ange ditt namn")
parser.add_argument("age", type=int, help="Ange ålder")
parser.add_argument("file", help="Ange en fil")

parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad info")

args = parser.parse_args()

if args.verbose:
    print(f"Hej, {args.name}. Din ålder {args.age}")
else:
    print(f"Hej, {args.name}")
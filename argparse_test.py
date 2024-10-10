import argparse

parser = argparse.ArgumentParser(description="Mitt script")

parser.add_argument("name", help="Ange ditt namn")

args = parser.parse_args()

print(f"Ditt namn är: {args.name}")
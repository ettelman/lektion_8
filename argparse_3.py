import argparse

parser = argparse.ArgumentParser(description="Mitt script")

parser.add_argument("name", help="Ange ditt namn")
parser.add_argument("age", type=int, help="Ange ålder")

parser.add_argument("-c", "--city", help="Ange vart du bor", default="Okänd stad")
parser.add_argument("--mode", choices=["enkel", "detaljerad"], help="Välj läge")

args = parser.parse_args()

if args.mode == "detaljerad":
    print(f"Hej, {args.name}. Din ålder {args.age}, Din stad: {args.city}")
else:
    print(f"Hej, {args.name}")
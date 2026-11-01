import argparse
from pathlib import Path
from .tracker import init_db

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--db", type=Path, default=Path("usb.db"))
    args = p.parse_args()
    conn = init_db(args.db)
    print(f"DB ready at {args.db}")

if __name__ == "__main__":
    main()

from typing import List,Dict

price: int = 100
tax: float = 1.1


def add_tax(price: int, tax: float) -> int:
    return int(price * tax)

if __name__ == "__main__":
    print(f"{add_tax(price, tax)}円")

sample_list: List[int] = [1, 2, 3]
sample_dict: Dict[str, int] = {"apple": 100, "banana": 200}
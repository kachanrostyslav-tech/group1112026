def calculate_discount(price: float, discount: float) -> float:
    """Return the price after applying a percentage discount."""
    return price * (1 - discount / 100)


def is_even(number: int) -> bool:
    """Return True when number is even, otherwise False."""
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    """Join a first name and last name with one space."""
    return f"{first_name} {last_name}"

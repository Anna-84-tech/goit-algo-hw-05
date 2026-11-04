import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generator function that analyzes the input text, identifies all real numbers
    that are clearly separated by spaces on both sides, and yields them as floats.
    """
    # Regular expression to find real numbers clearly separated by spaces.
    # \b ensures we match word boundaries, and we look for digits with an optional decimal part.
    pattern = r"\b\d+(?:\.\d+)?\b"
    
    # Find all matches in the text
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Function that uses the number generator function to calculate 
    and return the total sum of all extracted numbers in the input text.
    """
    # Sum up all numbers yielded by the generator function
    return sum(func(text))


# ==========================================
# Testing Block
# ==========================================
if __name__ == "__main__":
    # Test text from the assignment example
    sample_text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    print("--- Testing Generator Output ---")
    print("Extracted numbers:")
    for number in generator_numbers(sample_text):
        print(number)

    print("\n--- Testing Total Profit Sum ---")
    total_income = sum_profit(sample_text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    
    # # Expected output check
    # expected_sum = 1351.46
    # assert total_income == expected_sum, f"Expected {expected_sum}, but got {total_income}"
    # print("Test passed successfully!")
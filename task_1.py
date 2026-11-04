from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Creates and returns a fibonacci function that uses a cache
    to store and reuse previously calculated Fibonacci numbers.
    """
    # Initialize an empty dictionary to serve as the cache
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Calculates the n-th Fibonacci number using recursion and caching.
        """
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Return the value from cache if it was calculated before
        if n in cache:
            return cache[n]

        # Calculate the Fibonacci number recursively and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    return fibonacci


# === Testing block ===
if __name__ == "__main__":
    # Get the fibonacci function with closure cache
    fib = caching_fibonacci()

    # Test cases
    print("Testing Fibonacci calculations:")
    print(f"fib(10) = {fib(10)}")  # Expected output: 55
    print(f"fib(15) = {fib(15)}")  # Expected output: 610
    print(f"fib(0) = {fib(0)}")    # Expected output: 0
    print(f"fib(1) = {fib(1)}")    # Expected output: 1
    
    # Testing performance with larger numbers (utilizing cache effectively)
    print(f"fib(50) = {fib(50)}")  # Expected output: 12586269025 (calculated instantly due to cache)

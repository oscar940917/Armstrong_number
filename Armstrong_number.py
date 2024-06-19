def is_armstrong_number(num):
    digits = list(map(int, str(num)))
    n = len(digits)
    return num == sum(d ** n for d in digits)
def find_armstrong_numbers(n, m):
      armstrong_numbers = [num for num in range(n, m + 1) if is_armstrong_number(num)]
    return armstrong_numbers
def main():
    import sys
      input_data = sys.stdin.read().strip()
    n, m = map(int, input_data.split())
       armstrong_numbers = find_armstrong_numbers(n, m)
    if armstrong_numbers:
        print(" ".join(map(str, armstrong_numbers)))
    else:
        print("none")
if __name__ == "__main__":
    main()

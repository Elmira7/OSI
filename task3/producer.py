import random
import time

def generate_expression():
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    return f"{x} {operator} {y}"

def main():
    N = random.randint(120, 180)
    for _ in range(N):
        expression = generate_expression()
        print(expression, flush=True)
        time.sleep(1)

if __name__ == "__main__":
    main()

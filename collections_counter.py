from collections import Counter

if __name__ == "__main__":
    X = int(input())
    sizes = list(map(int, input().split()))
    inventory = Counter(sizes)
    customers = int(input())
    earnings = 0
    
    for _ in range(customers):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            earnings += price
            inventory[size] -= 1
    print(earnings)
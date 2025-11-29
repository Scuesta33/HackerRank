totalStamps = int(input("Cuántos sellos tienes? "))

distinct_countries = set()

for _ in range(totalStamps):
    distinct_countries.add(input("País: ").strip())

print("Países distintos:", len(distinct_countries))

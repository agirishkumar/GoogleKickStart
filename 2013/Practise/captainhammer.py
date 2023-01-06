from decimal import Decimal
from math import asin, pi
g = 9.8
testcases = int(input())
for i in range(1, testcases + 1):
    V, D = map(Decimal, input().split())
    θ = 90 * asin(Decimal(g) * D / (V ** 2)) / pi
    print(f"Case #{i}: {θ:.7f}", flush=True)
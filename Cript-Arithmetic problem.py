from itertools import permutations


def solve_cryptarithmetic():
    letters = 'SENDMORY'
    digits = range(10)

    # Check all permutations of 0-9 with length equal to the number of unique letters
    for perm in permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm

        # Skip permutations where S or M are zero since we don't want leading zeros
        if s == 0 or m == 0:
            continue

        # Calculate the numerical values for SEND, MORE, and MONEY
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            print(f"Solution: S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
            print(f"{send} + {more} = {money}")
            return

    print("No solution found.")


# Example usage:
solve_cryptarithmetic()

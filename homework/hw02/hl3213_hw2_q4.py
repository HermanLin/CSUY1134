def e_approx(n):
    total = 1
    facto = 1
    for x in range(1, n):
        total += 1 / facto
        facto *= x
    return total

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

main()
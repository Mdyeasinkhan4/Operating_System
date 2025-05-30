def calculate_available(resource, allocation, n, m):
    allocated = [0] * m
    for i in range(n):
        for j in range(m):
            allocated[j] += allocation[i][j]
    available = [resource[j] - allocated[j] for j in range(m)]
    return available


def is_safe_state(n, m, allocation, max_claim, available):
    finish = [False] * n
    work = available[:]
    executed_order = []

    print()
    while len(executed_order) < n:
        allocated_this_round = False
        for i in range(n):
            if not finish[i]:
                need = [max_claim[i][j] - allocation[i][j] for j in range(m)]
                if all(need[j] <= work[j] for j in range(m)):
                    print(f"All the resources can be allocated to Process {i + 1}")
                    work = [work[j] + allocation[i][j] for j in range(m)]
                    print("Available resources are:", ' '.join(map(str, work)))
                    print(f"Process {i + 1} executed?:y\n")
                    finish[i] = True
                    executed_order.append(i)
                    allocated_this_round = True
                    break
        if not allocated_this_round:
            break

    if len(executed_order) == n:
        print("System is in safe mode")
        print("The given state is safe state")
        return True
    else:
        print("System is NOT in safe mode")
        print("The given state is unsafe")
        for i in range(n):
            if not finish[i]:
                print(f"Process {i + 1} could not be completed")
        return False


def main():
    print("OUTPUT 1:\n")
    print("Enter the no. of processes and resources:", end=" ")
    n, m = map(int, input().split())

    print("\nEnter the claim matrix:")
    max_claim = [list(map(int, input().split())) for _ in range(n)]

    print("Enter the allocation matrix:")
    allocation = [list(map(int, input().split())) for _ in range(n)]

    print("Resource vector:", end=" ")
    resource = list(map(int, input().split()))
    print("Resource vector:", ' '.join(map(str, resource)))

    available = calculate_available(resource, allocation, n, m)

    is_safe_state(n, m, allocation, max_claim, available)

    print("\nExercise:")
    print("1. Extend the program to take a new Request[i][j] at runtime and check if it can be granted using the algorithm.")
    print("2. Modify the program to explicitly detect and label which process causes the system to be unsafe.")


if __name__ == "__main__":
    main()

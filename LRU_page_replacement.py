def lru_page_replacement(pages, capacity):
    memory = []
    page_hits = 0
    page_faults = 0

    for page in pages:
        if page in memory:
            page_hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

    total = page_hits + page_faults

    print("\nResults:")
    print("Page sequence:", pages)
    print("Memory capacity:", capacity)
    print("Page Hits:", page_hits)
    print("Page Faults:", page_faults)

# --- Main Program ---
if __name__ == "__main__":
    try:
        page_input = input("Enter the page sequence (space-separated): ")
        pages = list(map(int, page_input.strip().split()))
        capacity = int(input("Enter memory capacity: "))
        lru_page_replacement(pages, capacity)
    except ValueError:
        print("Invalid input. Please enter only integers.")

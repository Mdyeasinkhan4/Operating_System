def optimal_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    page_hits = 0

    print("\n--- Optimal Page Replacement ---\n")
    print(f"{'Step':<5} {'Page':<6} {'Frames':<20} {'Result'}")
    print("-" * 45)

    for i in range(len(pages)):
        page = pages[i]

        if page in frames:
            page_hits += 1
            result = "Hit"
        else:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Find the page with the farthest use in future
                future_uses = []
                for f in frames:
                    if f in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(f))
                    else:
                        future_uses.append(float('inf'))
                index_to_replace = future_uses.index(max(future_uses))
                frames[index_to_replace] = page
            result = "Fault"

        print(f"{i+1:<5} {page:<6} {str(frames):<20} {result}")

    print("\nTotal Page Faults:", page_faults)
    print("Total Page Hits:", page_hits)
    fault_rate = (page_faults / len(pages)) * 100
    print(f"Page Fault Rate: {fault_rate:.2f}%\n")


def run_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    index = 0
    test_cases = int(lines[index])
    index += 1

    for t in range(test_cases):
        print(f"\n=== Test Case {t + 1} ===")
        num_pages = int(lines[index])
        index += 1

        reference_string = list(map(int, lines[index].split()))
        index += 1

        frame_count = int(lines[index])
        index += 1

        pages = reference_string[:num_pages]
        optimal_page_replacement(pages, frame_count)


# Main function
if __name__ == "__main__":
    while True:
        mode = input("Choose input mode - manual (m) or file (f): ").strip().lower()
        if mode == 'f':
            file_path = input("Enter the file path (e.g., input.txt): ").strip()
            run_from_file(file_path)
        else:
            num_pages = int(input("Enter the number of pages: "))
            reference_string = input("Enter the page reference string (space-separated): ")
            pages = list(map(int, reference_string.strip().split()))[:num_pages]
            frame_count = int(input("Enter the number of frames: "))
            optimal_page_replacement(pages, frame_count)

        choice = input("Do you want to run again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting program.")
            break

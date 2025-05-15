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

        # Print the current step
        print(f"{i+1:<5} {page:<6} {str(frames):<20} {result}")

    print("\nTotal Page Faults:", page_faults)
    print("Total Page Hits:", page_hits)


# Main function
if __name__ == "__main__":
    # Get user input
    reference_string = input("Enter the page reference string (space-separated): ")
    pages = list(map(int, reference_string.strip().split()))

    frame_count = int(input("Enter the number of frames: "))

    optimal_page_replacement(pages, frame_count)

from collections import deque

def fifo_page_replacement(pages, frame_count):
    frames = deque()
    in_frames = set()
    page_faults = 0

    print("\nFIFO Page Replacement Simulation:\n")

    for page in pages:
        print(f"Page {page} -> ", end='')

        if page not in in_frames:
            page_faults += 1
            if len(frames) == frame_count:
                removed = frames.popleft()
                in_frames.remove(removed)
            frames.append(page)
            in_frames.add(page)
            print("Page Fault")
        else:
            print("Hit")

        print(f"Current Frames: {list(frames)}")

    print(f"\nTotal Page Faults: {page_faults}")


if __name__ == "__main__":
    n = int(input("Enter the number of pages: "))
    pages = list(map(int, input("Enter the page reference string (space-separated): ").split()))
    
    if len(pages) != n:
        print("Number of pages does not match input length!")
    else:
        frame_count = int(input("Enter the number of frames: "))
        fifo_page_replacement(pages, frame_count)

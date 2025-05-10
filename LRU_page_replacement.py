def lru_page_replacement(ref_string, num_frames):
    frames = []
    page_faults = 0
    page_hits = 0

    for page in ref_string:
        if page in frames:
            page_hits += 1
            frames.remove(page)
            frames.append(page)  # Move to most recently used
        else:
            page_faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)  # Remove least recently used
                frames.append(page)

        # Print current frame state, left-aligned, fill with -1
        display = frames + [-1] * (num_frames - len(frames))
        print(' '.join(str(x) for x in display))

    fault_rate = (page_faults / len(ref_string)) * 100
    print(f"\nNumber of page faults : {page_faults}")
    print(f"Page fault rate = {fault_rate:.6f}")


def read_input_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        ref_len = int(lines[0])
        ref_string = list(map(int, lines[1].strip().split()))
        num_frames = int(lines[2])
    return ref_len, ref_string, num_frames


if __name__ == "__main__":
    filename = 'input.txt'  # Must contain 12\n1 2 3 4 1 2 5 1 2 3 4 5\n3
    ref_len, ref_string, num_frames = read_input_from_file(filename)

    print("OUTPUT:")
    print(f"Enter length of the reference string: {ref_len}")
    print(f"Enter the reference string: {' '.join(map(str, ref_string))}")
    print(f"Enter no of frames: {num_frames}\n")

    lru_page_replacement(ref_string, num_frames)

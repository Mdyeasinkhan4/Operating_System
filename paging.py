# Function to calculate the front and rear address of given page number
class PagingMemoryManagement:
    @staticmethod
    def show_page_boundaries(page_num, page_size):
        front_address = page_num * page_size
        rear_address = front_address + page_size - 1
        return [front_address, rear_address]

    @staticmethod
    def calculate_physical_address(page_num, page_size, offset):
        return (page_num * page_size) + offset

# Main function
def main():
    print("Paging Memory System")

    # Input page size and number of pages
    page_size = int(input("Enter the page size (in bytes): "))
    total_pages = int(input("Enter the total number of pages: "))

    # Show the front and rear physical address for each page
    print("\nPage number boundaries:")
    for page_num in range(total_pages):
        boundaries = PagingMemoryManagement.show_page_boundaries(page_num, page_size)
        print(f"Page {page_num}: Front Address = {boundaries[0]}, Rear Address = {boundaries[1]}")

    # Option to find a physical address
    while True:
        find_address = input("\nCalculate Physical Address? (yes/no): ").strip().lower()
        if find_address == 'yes':
            user_page_num = int(input("Enter the page number: "))
            offset = int(input("Enter the offset: "))
            physical_address = PagingMemoryManagement.calculate_physical_address(
                user_page_num, page_size, offset
            )
            print(f"Physical address for page {user_page_num} with offset {offset}: {physical_address}")
        elif find_address == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

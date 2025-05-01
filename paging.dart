import 'dart:io';
// Function to calculate the front and rear address of given page number
class PagingMemoryManagement {
  static List<int> showPageBoundaries(int pageNum, int pageSize) {
    int frontAddress = pageNum * pageSize;
    int rearAddress = frontAddress + pageSize - 1;
    return [frontAddress, rearAddress];
  }

// calculate physical address based on page number, page size and offset
  static int calculatePhysicalAddress(int pageNum, int pageSize, int offset) {
    return (pageNum * pageSize) + offset;
  }
}
//main function
void main() {
  print("Paging Memory System");

//Input page size and number of pages
  stdout.write("Enter the page size (in bytes): ");
  int pageSize = int.parse(stdin.readLineSync()!);

  stdout.write("Enter the total number of pages: ");
  int totalPages = int.parse(stdin.readLineSync()!);

//Show the front and rear physical address for each page
  print("\nPage number boundaries:");

  for (int pageNum = 0; pageNum < totalPages; pageNum++) {
    List<int> boundaries = PagingMemoryManagement.showPageBoundaries(pageNum, pageSize);
        
    print(
        "Page $pageNum: Front Address = ${boundaries[0]}, Rear Address = ${boundaries[1]}");
  }

//Option to find a physical address
  while (true) {
    stdout.write("\nCalculate Physical Address? (yes/no): ");
    String? findAddress = stdin.readLineSync()?.toLowerCase();

    if (findAddress == 'yes') {
      stdout.write("Enter the page number: ");
      int userPageNum = int.parse(stdin.readLineSync()!);

      stdout.write("Enter the offset: ");
      int offset = int.parse(stdin.readLineSync()!);

      int physicalAddress = PagingMemoryManagement.calculatePhysicalAddress(
          userPageNum, pageSize, offset);
      print(
          "Physical address for page $userPageNum with offset $offset: $physicalAddress");
    } else if (findAddress == 'no') {
      break;
    } else {
      print("Invalid input. Please enter 'yes' or 'no'.");
    }
  }
}

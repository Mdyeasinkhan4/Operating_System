import 'dart:collection';
import 'dart:io';

void main() {
  // Input: Page reference string
  stdout.write('Enter the number of pages: ');
  int n = int.parse(stdin.readLineSync()!);

  List<int> pages = [];
  stdout.write('Enter the page reference string (space-separated): ');
  pages = stdin.readLineSync()!.split(' ').map(int.parse).toList();

  if (pages.length != n) {
    print('Number of pages does not match input length!');
    return;
  }

  // Input: Number of page frames
  stdout.write('Enter the number of frames: ');
  int frameCount = int.parse(stdin.readLineSync()!);

  Queue<int> frames = Queue<int>();
  Set<int> inFrames = {};
  int pageFaults = 0;

  print('\nFIFO Page Replacement Simulation:\n');

  for (int page in pages) {
    stdout.write('Page $page -> ');

    if (!inFrames.contains(page)) {
      // Page fault
      pageFaults++;

      if (frames.length == frameCount) {
        // Remove the oldest page
        int removed = frames.removeFirst();
        inFrames.remove(removed);
      }

      frames.addLast(page);
      inFrames.add(page);
      print('Page Fault');
    } else {
      print('Hit');
    }

    print('Current Frames: ${frames.toList()}');
  }

  print('\nTotal Page Faults: $pageFaults');
}

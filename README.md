# Virtual Memory Simulator
A Python application for simulating virtual memory. Physical memory is managed inherently.  
Demand paging is supported.  
  
## Installation
Move all .py files, to any desired directory.  

## Usage
Provide init and input files. Sample ones are provided.  
```bash
python main.py <init file> <input file>
```
  
Format for the init file is as follows:  
First line composed of triples of segment # s, length l, and page table frame # pt.  
```bash
0 1500 2 1 250000 6
```
The above defines segments (s = 0, l = 1500, pt = 2) and (s = 1, l = 250000, pt = 6).  
A negative page table frame # means that it is currently stored on disk and must be loaded  
in through demand paging.  

Second line composed of triples of segment # s, page # p, and frame # f.  
```bash
0 0 3 0 1 -11
```
The above defines page tables (s = 0, p = 0, f = 3) and (s = 0, p = 1, f = -11).  
A negative frame number means that it is currently stored on disk and must be loaded  
in through demand paging.  
  
Format for the input file is as follows:  
First line composed of virtual addresses separated by spaces.  
```bash
4 500 522
```
The above defines three virtual addresses 1540, 2036, and 2058.  
  
# Output  
Output is output-dp.txt, with physical memory addresses printed in a single line.
A -1 is printed when a given frame has not been allocated for either the segment  
page table.  

```bash
1540 2036 2058 -1 2059 4150 4116 4628 4625 5219 -1 28148 -1 5953 7680 30886 -1 30787 6642 6187 6754 6745
```

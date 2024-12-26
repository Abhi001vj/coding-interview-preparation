https://leetcode.com/discuss/interview-question/3293671/Advanced-Operating-Systems-FAANG-Interview-Questions-2023

https://cp-algorithms.com/data_structures/segment_tree.html

1. What is a deadlock?
A deadlock occurs when a set of processes are blocked because each process holds a resource and waits for another resource acquired by some other process in the same set. None of the processes in the set can proceed, and they are said to be in a “circular wait” situation.

Key Conditions (Coffman’s conditions)
Mutual Exclusion: Resources are non-shareable.
Hold and Wait: A process holding at least one resource is waiting to acquire more resources held by other processes.
No Preemption: Resources cannot be forcibly taken away from a process.
Circular Wait: A circular chain of processes exists, where each process holds a resource the next process needs.
Visualization
Imagine four cars at a four-way intersection, each one blocking the intersection, waiting for the other to move. None can move, hence a deadlock.

2. How do you prevent a deadlock?
Prevention
You ensure at least one of the Coffman’s conditions is never allowed to hold:

Mutual Exclusion: Sometimes you can make resources shareable (e.g., read-only files) if possible.
Hold and Wait: Require processes to request all required resources at once, or require a process to release all resources before requesting new ones.
No Preemption: If a process is holding a resource and requests another resource that is not immediately available, preempt the resources currently held.
Circular Wait: Impose a strict total ordering on resource types and require processes to request resources in an increasing or decreasing order of enumeration.
Avoidance
Another strategy is the Banker’s Algorithm, which checks resource allocation states before granting resources to ensure the system never enters an unsafe state.

3. What is synchronization?
Process synchronization refers to the coordination of processes (or threads) so that they do not interfere with each other when sharing data and resources. It’s a mechanism to ensure correctness, consistency, and predictability in concurrent executions.

4. What is a semaphore?
A semaphore is a synchronization primitive (an integer variable) that can be used to solve various concurrency problems. Dijkstra introduced two operations:

wait(P): Decrement the semaphore value. If the value is negative, the calling process is blocked.
signal(V): Increment the semaphore value. If there are blocked processes, unblock one.
Semaphores help protect critical sections by controlling access to shared resources.

Types of Semaphores
Counting semaphore: Can have an unrestricted domain (0 to N).
Binary semaphore (mutex): Can only be 0 or 1. Often used to implement mutual exclusion.
5. What is a race condition?
A race condition occurs when multiple processes or threads read and write shared data simultaneously, and the final outcome depends on the arbitrary order of operations. Avoiding race conditions typically requires synchronization (e.g., semaphores, locks).

Example: Two threads incrementing a global counter. If both read the counter’s value (say 100) before either writes, they both write 101, effectively missing one increment.

6. What are mutex locks?
A mutex lock (or simply “mutex”) is a mutual exclusion object that allows multiple program threads to share the same resource (e.g., a file) but not simultaneously. When one thread locks (acquires) the mutex, other threads attempting to acquire it are blocked until it is released.

In many systems, a binary semaphore can be used as a mutex.
Mutex usage pattern:
cpp
Copy code
pthread_mutex_lock(&mutex);
// Critical section
pthread_mutex_unlock(&mutex);
7. What is a process?
A process is a program in execution. It has:

Program code (text section)
Program counter, which indicates the current instruction.
CPU registers
Stack (for local variables and function calls)
Heap (for dynamically allocated memory)
Data section (global variables)
8. Difference between thread and process?
Aspect	Process	Thread
Address Space	Separate for each process	Shared among threads within a process
Overhead	Higher (requires context switch with memory context)	Lower (thread context switch is faster)
Creation	Slower (OS has to allocate resources)	Faster (shares process resources)
Communication	Inter-process communication (IPC) needed	Can communicate via shared memory in the same process
9. What is an orphan process?
An orphan process is a child process that continues to run even though its parent has terminated. In Unix-like systems, orphan processes are adopted by the init process (process ID 1).

10. Why is the CPU known as a resource allocator?
The CPU (or more generally, the operating system running on the CPU) allocates resources like CPU time, memory, file handles, I/O devices, etc., among competing processes or threads. The scheduler, which runs on the CPU, decides which process runs next, thus allocating CPU time slices.

11. What is the role of the kernel in an OS?
The kernel is the core of the operating system, with complete control over the system. It:

Manages memory (allocations, page tables),
Schedules processes and threads,
Handles interrupts and system calls,
Manages I/O devices through drivers,
Provides security and protection mechanisms (user mode, kernel mode).
12. What is the difference between paging and segmentation?
Paging: Divides memory into fixed-size blocks called pages (in logical memory) and frames (in physical memory).

Eliminates external fragmentation but can cause internal fragmentation.
The user does not see the division into pages.
Segmentation: Divides memory into variable-sized segments according to the logical divisions of a program (code, data, stack).

No internal fragmentation but can cause external fragmentation.
The user (and compiler) is aware of segment boundaries.
13. What is thrashing?
Thrashing occurs when a system spends more time swapping pages in and out of memory than actually executing processes. This happens when the working sets of active processes collectively exceed the available physical memory.

14. What is virtual memory?
Virtual memory is a memory management technique where a process’s logical address space can be larger than the physical memory. The OS uses disk storage (swap space) to simulate additional memory, and only needed pages are loaded into physical memory.

15. What is aging?
Aging is a technique used in scheduling to avoid starvation. The priority of a process is gradually increased the longer it waits in the ready queue, ensuring that lower-priority processes eventually get CPU time.

16. What is context switching?
A context switch is the act of saving the context (CPU registers, program counter, etc.) of the currently running process or thread, and restoring the context of another process or thread. This happens when the scheduler decides to switch execution.

17. Explain process synchronization?
Process synchronization ensures that concurrent processes or threads execute so that shared data remains consistent and system resources are used efficiently. Mechanisms include:

Mutexes and Semaphores
Monitors (high-level constructs in some languages)
Lock-free and wait-free data structures (advanced)
18. Mention any four scheduling algorithms and which is the best scheduling algorithm?
First Come, First Served (FCFS)
Shortest Job First (SJF) / Shortest Remaining Time First (SRTF)
Round Robin (RR)
Priority Scheduling
Which is best?

For general purpose and fairness: Round Robin (especially in time-sharing systems).
For minimizing average waiting time (theoretically optimal in some conditions): SJF.
There is no single “best” for all use cases; it depends on workload characteristics.
19. What is spooling?
SPOOLING (Simultaneous Peripheral Operations OnLine) is a technique where data is temporarily held to be used and processed by a device. It’s commonly used in print spooling: multiple processes send print jobs to a spool (directory), and the printer daemon processes them in order.

20. What is the use of the trap bit?
In some architectures, the trap bit (or trap flag) is used for debugging. When set, the CPU will execute in single-step mode, generating a trap after each instruction so a debugger can inspect registers and memory.

21. What is a bootstrap program?
The bootstrap program (or bootloader) is the first code that runs when a computer starts. It initializes the system (e.g., sets up CPU registers, memory map) and then loads the operating system kernel into memory and transfers execution to it.

22. Can a system run without an OS?
Yes, but only for extremely specialized or embedded systems, or when the program is small enough to directly interface with the hardware (e.g., firmware, microcontrollers). Modern general-purpose computing devices almost always require an OS.

23. What sockets do hackers use?
Hackers or attackers may use any TCP/UDP ports (commonly referred to as “sockets” when connected) that have vulnerabilities or are left open:

For example, port 22 (SSH), port 80 (HTTP), or port 443 (HTTPS) can be exploited if insecure.
Not a single specific socket is designated for hacking; it depends on the service vulnerabilities.
24. What are the types of semaphores?
Counting Semaphores: For any integer value (0 to N).
Binary Semaphores: Restricted to values 0 or 1, also called mutex.
25. What is compaction?
Compaction is a technique to deal with external fragmentation in memory. The OS shifts processes around physically in memory so that all free memory is in one contiguous block, thus allowing larger allocations.

26. How can you increase the priority of a process?
Dynamic Priority Adjustment (aging): The longer a process waits, the more priority it gains.
System calls: Some operating systems provide nice() or setpriority() calls to modify process priorities.
Scheduler-specific methods: In real-time or advanced scheduling, you might configure priorities explicitly.
27. What is disk scheduling?
Disk scheduling decides the order in which disk I/O requests are serviced. Common algorithms include:

FCFS
SSTF (Shortest Seek Time First)
SCAN and variants like C-SCAN, LOOK, C-LOOK
28. What is Belady’s anomaly?
Belady’s anomaly is when increasing the number of page frames results in more page faults in certain replacement algorithms like FIFO. This is counterintuitive, as you’d expect more frames to yield fewer page faults.

29. What is C-SCAN?
Circular SCAN (C-SCAN) is a disk scheduling algorithm. The head moves in one direction, servicing requests until it reaches the end of the disk. Then it jumps back to the beginning and continues. It provides a more uniform wait time compared to SCAN.

30. What is interprocess communication (IPC)?
IPC is a mechanism that allows processes to communicate and synchronize their actions. Methods include:

Pipes
Message Queues
Shared Memory + Semaphores
Sockets
Remote Procedure Calls (RPC)
31. What are real-time systems?
Real-time systems have strict timing constraints. They must respond to events within a guaranteed time frame. Examples:

Hard real-time: e.g., airbag systems, pacemakers
Soft real-time: e.g., video streaming, audio playback
32. What is a timestamp?
In distributed or concurrent systems, a timestamp is a sequence number that indicates the logical ordering of events. Often used in concurrency control (e.g., Lamport timestamps, Vector clocks).

33. What are the different cache mapping techniques?
Direct Mapping: Each block in main memory maps to only one possible cache line.
Associative Mapping: Any block can go into any cache line.
Set-Associative Mapping: A compromise between direct and associative, where the cache is divided into sets, and blocks can be placed in any line of a set.
34. What is response time and turnaround time?
Response Time: Time from the submission of a request until the first response is produced.
Turnaround Time: Total time to execute a process from submission to completion.
35. What are the different file accessing methods?
Sequential Access: Read/write sequentially (like a tape).
Direct/Random Access: Access any byte/block without reading in sequence.
Indexed Access: Uses an index to jump to specific blocks quickly.
36. What is memory management, and how is the OS responsible for it?
Memory management is the process of controlling and coordinating computer memory (RAM). The OS handles:

Allocation and deallocation of memory to processes,
Swapping pages in and out (virtual memory),
Fragmentation management.
37. Mention any two deadlock prevention algorithms.
Hold and Wait Prevention: Processes must request all resources at once.
Circular Wait Prevention: Impose an ordering of resources (R1 < R2 < … < Rn).
38. What is system software?
System software includes the operating system and other tools that manage computer resources at a low level. Examples: compilers, assemblers, linkers, device drivers, system utilities.

39. What is a critical section in the context of process synchronization?
A critical section is a segment of code where a process accesses shared resources (e.g., variables, files) that must not be accessed by more than one process simultaneously to avoid inconsistencies.

40. What is a deadlock avoidance algorithm, and how does it work?
A classic deadlock avoidance algorithm is the Banker’s Algorithm, which:

Analyzes each request.
Determines if granting it will lead the system into an “unsafe state.”
If it would lead to an unsafe state, the request is delayed until safe.
The system tries to ensure it always has enough resources in reserve to allow at least one process to complete.

41. What is the difference between preemptive and non-preemptive scheduling?
Preemptive: The OS can forcibly remove the CPU from a running process (e.g., Round Robin, SRTF).
Non-preemptive: Once a process has the CPU, it runs to completion or until it blocks (e.g., FCFS, SJF without preemption).
42. Explain the concept of paging in virtual memory.
Paging splits the logical address space of a process into fixed-size pages and physical memory into frames. The OS uses a page table to map logical page numbers to physical frame numbers. This abstraction helps manage fragmentation and simplifies memory allocation.

43. What is the purpose of a file system, and how does it work?
A file system organizes and provides metadata about how data is stored on storage devices. Responsibilities include:

Directory structure (hierarchical or flat),
File allocation tables, inodes, or other indexing structures,
File permissions and attributes,
Space management.
44. What is a system call, and how is it different from a regular function call?
A system call is a request from a user-level process to the kernel to perform privileged operations (e.g., I/O, process creation).

Regular function call stays in user space.
System call transitions from user mode to kernel mode (via a software interrupt or trap).
45. What is a thread pool, and how does it improve performance in multi-threaded applications?
A thread pool is a collection of pre-created threads. Instead of creating and destroying threads for each task (which is expensive), tasks are dispatched to available threads in the pool. This reduces overhead and improves responsiveness under high load.

46. Explain the concept of demand paging and how it improves the efficiency of virtual memory.
Demand paging only loads pages into physical memory when they are actually needed (i.e., upon a page fault). This:

Reduces the initial memory requirement for a process,
Allows multiple processes to share unused pages,
Improves apparent concurrency and memory utilization.
47. What is a cache hit and a cache miss, and how do they affect system performance?
Cache hit: The requested data is in the cache (fast to retrieve).
Cache miss: The requested data is not in the cache (must fetch from main memory or disk).
High hit rate improves performance significantly, while a high miss rate can degrade system performance because of the slower access time to main memory/disk.

48. What is the role of the memory manager in an operating system?
The memory manager:

Keeps track of which parts of memory are in use or free,
Allocates memory to processes and deallocates it when done,
Manages paging/swapping,
Handles protection and sharing (using page tables or segmentation).
49. What is the purpose of the process scheduler in an operating system, and how does it work?
The process scheduler decides which process (or thread) runs next on the CPU. It uses a scheduling algorithm (e.g., Round Robin, Priority, Multilevel Feedback Queue) based on policies like fairness, response time, throughput, etc. It might use:

Ready queue (for processes ready to run),
Scheduling criteria (priority, CPU burst times),
Preemption or non-preemption.
50. Explain the concept of a deadlock detection algorithm, and how is it used in practice?
Deadlock detection algorithms periodically check the state of the system for a circular wait. A common method:

Model processes, resources, and allocations in a wait-for graph,
Look for cycles in the graph.
If a deadlock is detected, the system might choose to kill or roll back processes to break the cycle.
51. What is the difference between a kernel thread and a user-level thread?
Kernel Thread: Managed by the OS kernel. A blocking system call by one kernel thread does not block others. Switching between kernel threads involves mode switches.
User-Level Thread: Managed by a thread library in user space. Fast to create and switch, but if one thread blocks on a system call, the entire process may block.
52. What is the difference between a semaphore and a mutex, and when would you use each one?
Mutex: Binary (only one resource instance). Typically used to protect critical sections when only one thread can access a shared resource at a time.
Semaphore: Can be counting or binary. Counting semaphores allow multiple permits (N resources). Use it when you have multiple instances of a resource that can be shared among multiple threads up to a limit.
53. How does virtual memory protect processes from interfering with each other?
Through address translation, each process has its own virtual address space mapped to physical memory. The OS ensures:

One process’s pages do not overlap with another’s (by controlling the page tables),
Access violations generate traps.
54. What is a context switch, and why is it an important operation in an operating system?
Context switch is the switching of the CPU from one process/thread to another. It is critical because:

It enables multitasking (logical concurrency),
It must be fast and efficient to avoid overhead,
It is performed by the scheduler.
55. How do you measure the performance of an operating system, and what metrics are used?
Common metrics:

Throughput: Number of processes/transactions completed per time unit.
CPU Utilization: How busy the CPU is.
Response Time: Time from request submission to first response.
Turnaround Time: Time from process submission to completion.
Waiting Time: Total time spent in the ready queue.
56. What is a device driver, and what is its role in an operating system?
A device driver is software that interfaces between the OS (and applications) and hardware devices (e.g., printers, disks, network cards). It:

Translates OS I/O requests into device-specific operations,
Manages device control registers,
Handles interrupts.
57. How does the operating system manage input/output operations, and what challenges does it face?
The OS uses:

Device drivers for device-specific control,
Interrupt handling to respond to device events,
Buffering, caching, and spooling for performance.
Challenges:

Asynchronous nature of I/O,
Different device speeds (slow vs. fast I/O),
Ensuring protection and concurrency control.
58. What is a trap, and how is it used in operating system design?
A trap (or software interrupt) is a mechanism for:

System calls from user mode to kernel mode,
Handling exceptions (e.g., divide-by-zero, invalid memory access).
The OS trap handler determines how to handle or report the error or request.
Helpful Resources and Visualizations
Operating System Concepts by Silberschatz, Galvin, and Gagne (a classic “dinosaur book”).
YouTube: CrashCourse on Operating Systems – Good for quick refreshers.
MIT’s 6.S081/6.828 (Operating System Engineering) – In-depth coverage with labs using xv6.
Diagrams for process states, paging, banker’s algorithm are widely available in OS textbooks and websites like GeeksforGeeks or TutorialsPoint.
"""
3. Simulate Stopwatch Program
    Desc -> Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
    a. I/P -> Start the Stopwatch and End the Stopwatch
    b. Logic -> Measure the elapsed time between start and end
    c. O/P -> Print the elapsed time.
"""
import time
run = True
while run:
    start = int(input("Enter 1 to Start: "))
    startTime = time.time()
    stop = int(input("Enter 0 to Stop: "))
    endTime = time.time()

    timeElapsed = endTime - startTime
    print("Time elapsed from Start to Stop is:", timeElapsed, "Seconds")
    run = False

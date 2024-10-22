jobs = [int(el) for el in input().split(', ')]
index = int(input())

clock_cycles = 0

while jobs:
    min_job_index = jobs.index(min(jobs))
    if min_job_index == index:
        clock_cycles += jobs[min_job_index]
        jobs[min_job_index] = float("+inf")
        break
    clock_cycles += jobs[min_job_index]
    jobs[min_job_index] = float("+inf")

print(clock_cycles)


from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def do_work(x):
    time.sleep(0.1)
    print(x)

jobs = []
# number of threads
n_jobs = 20

with ThreadPoolExecutor(max_workers=n_jobs) as e:
    for x in range(n_jobs):
        jobs.append(e.submit(do_work, x))
        # submit a job to execute a function
        # with an argument (x)


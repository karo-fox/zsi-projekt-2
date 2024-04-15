import statistics
import subprocess
import timeit

if __name__ == "__main__":
    times = []
    for _ in range(10_000):
        times.append(
            timeit.timeit(
                lambda: subprocess.run(["python", "-m", "main", "1"]), number=1
            )
        )
    print(statistics.mean(times))
    print(statistics.median(times))
    print(statistics.stdev(times))

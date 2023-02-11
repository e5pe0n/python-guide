import asyncio
import time


async def f():
    print(f"f() started at {time.strftime('%X')}")
    time.sleep(5)   # some task which could take much time on the process
    print(f"f() finished at {time.strftime('%X')}")


async def g():
    print(f"g() started at {time.strftime('%X')}")
    await asyncio.sleep(3)  # some async task
    print(f"g() finished at {time.strftime('%X')}")


async def main():
    task1 = asyncio.create_task(f())
    task2 = asyncio.create_task(g())

    print(f"main() started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"main() finished at {time.strftime('%X')}")

asyncio.run(main())

"""
main() started at 12:20:20
f() started at 12:20:20
f() finished at 12:20:25
g() started at 12:20:25
g() finished at 12:20:28
main() finished at 12:20:28

f() took 5s
g() took 3s
main() took 8s

`sleep(5)` in `f()` effects on the process where `main()` is running.
Thus the entire event loop pause due to the subprocess.
"""

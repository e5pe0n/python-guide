import asyncio
import time


async def f():
    print(f"f() started at {time.strftime('%X')}")
    proc = await asyncio.create_subprocess_exec("sleep", "5")
    await proc.wait()   # some subprocess
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
main() started at 12:10:57
f() started at 12:10:57
g() started at 12:10:57
g() finished at 12:11:00
f() finished at 12:11:02
main() finished at 12:11:02

f() took 5s
g() took 3s
main() took 5s

The subprocess spawned by `f()` run as a different process
to the process where `main()` is running.
Thus the entire event loop doesn't pause due to the subprocess.
"""

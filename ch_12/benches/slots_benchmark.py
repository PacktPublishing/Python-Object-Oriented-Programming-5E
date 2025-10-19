"""
Python 3 Object-Oriented Programming

Chapter 12. Advanced Python Design Patterns
"""
import argparse
from collections.abc import Callable
from functools import partial
import gc
import json
from pathlib import Path
from statistics import mean
import sys
import time
from textwrap import dedent

from inspector import get_object_size

import gps_messages
import gps_message_slots

Kb = 1024
Mb = Kb * Kb
Gb = Mb * Kb
Tb = Gb * Kb

def large_buffer(size: int = 512 * Kb) -> bytes:
    messages = dedent('''\
    $GPGGA,161229.487,3723.2475,N,12158.3416,W,1,07,1.0,9.0,M,,,,0000*18
    $GPGLL,3723.2475,N,12158.3416,W,161229.487,A,A*41
    $GPGSA,A,3,07,02,26,27,09,04,15,,,,,,1.8,1.0,1.5*33
    $GPVTG,309.62,T,,M,0.13,N,0.2,K,A*23
    $GPRMC,161229.487,A,3723.2475,N,12158.3416,W,0.13,309.62,120598,,*10
    ''')
    copies = (size + len(messages)) // len(messages)
    return (messages * copies).encode("ASCII")

def load_gps_messages(buffer_cls: type, client_cls: type, buffer_size: int | None = None) -> None:
    buffer = buffer_cls(large_buffer(buffer_size))
    c = client_cls(buffer)
    points = list(c.scan())
    return points

def profile(some_func: Callable[..., None], repeats: int = 10) -> None:
    with open(Path("profile.ndjson"), "w") as target:
        for i in range(repeats):
            # Run function...
            start = time.perf_counter()
            result = some_func()
            end = time.perf_counter()
            # Get memory use...
            sys._clear_internal_caches()
            gc.collect()
            data = {
                "list_elements": len(result),
                "memory": sys.getallocatedblocks(),
                "object_size": get_object_size(result),
                "time": (end - start) * 1_000
            }
            target.writelines(json.dumps(data, indent=None) + "\n")

def summarize():
    with open(Path("profile.ndjson")) as source:
        raw = [json.loads(line) for line in source]
    memory = [sample['memory'] for sample in raw]
    obj_size = [sample['object_size'] for sample in raw]
    run_time = [sample['time'] for sample in raw]
    elements = [sample['list_elements'] for sample in raw]
    print(f"{max(elements)=} items, {max(memory)=} blocks, {max(obj_size)=:,d} bytes, {mean(run_time)=:.3f} ms")

def get_options(argv: list[str] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", action='store', nargs='?', choices=('base', 'slots'), default='base')
    parser.add_argument("-s", "--size", action='store', default="512K")
    return parser.parse_args(argv)

def main() -> None:
    options = get_options()
    scale = {"K": Kb, "M": Mb, "G": Gb}
    try:
        if (scale_code := options.size[-1].upper()) in scale:
            size = int(options.size[:-1]) * scale[scale_code]
        else:
            size = int(options.size)
    except ValueError:
        sys.exit(f"invalid size: {options.size!r}")

    if options.case == "base":
        base = partial(load_gps_messages, gps_messages.Buffer, gps_messages.Client, size)
        profile(base)
        print("Baseline")
        summarize()

    elif options.case == "slots":
        slots = partial(load_gps_messages, gps_message_slots.Buffer, gps_message_slots.Client, size)
        profile(slots)
        print("__slots__")
        summarize()

    else:
        sys.exit("unknown case")

if __name__ == "__main__":
    main()


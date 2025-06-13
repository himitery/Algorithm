from typing import List


def solution(book_time: List[List[str]]) -> int:
    times, rooms = (
        sorted(
            [(time_to_num(start), time_to_num(end) + 10) for start, end in book_time],
            key=lambda time: time[0],
        ),
        [],
    )

    for start, end in times:
        allocated = False

        for idx, room_end in enumerate(rooms):
            if room_end <= start:
                rooms[idx] = end
                allocated = True
                break

        if not allocated:
            rooms.append(end)

    return len(rooms)


def time_to_num(time: str) -> int:
    hour, minute = map(int, time.split(":"))

    return hour * 60 + minute

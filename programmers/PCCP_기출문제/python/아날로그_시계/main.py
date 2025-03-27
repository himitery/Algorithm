def solution(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> int:
    h, m, s = (h1 * 30 + m1 / 2 + s1 / 120) % 360, (m1 * 6 + s1 / 10) % 360, (s1 * 6) % 360

    count = int(h == m or h == s or m == s)
    for idx in range((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1):
        nh, nm, ns = round(h + 1 / 120, 5), round(m + 1 / 10, 5), round(s + 6, 5)

        if nh == ns or nm == ns:
            count += 1
        else:
            for condition in [
                not h == s and (h - s) * (nh - ns) <= 0,
                not m == s and (m - s) * (nm - ns) <= 0,
            ]:
                count += int(condition)

        h, m, s = nh % 360, nm % 360, ns % 360

    return count

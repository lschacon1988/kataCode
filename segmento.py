def segments(seg, day, moth):
    count = 0
    len_segments = len(seg)
    range_segments = range(moth, len_segments + 1)

    for i in range_segments:
        temp = sum(seg[i - moth:i])

        if temp == day:
            count += 1

    return count


s = [1, 2, 1, 3, 2]
d = 3
m = 2

print('seg', segments(seg=s, day=d, moth=m))

def charmap(value):
    ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    step = 100 / len(ASCII_CHARS)
    idx = int(100 / value / step)
    if idx >= len(ASCII_CHARS):
        idx = len(ASCII_CHARS) - 1
    return ASCII_CHARS[idx]
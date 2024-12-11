def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    r = color[1:3]
    g = color[3:5]
    b = color[5:7]
    return (int(r, 16), int(g, 16), int(b, 16))


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    return list(map(from_hex_to_rgb, values))

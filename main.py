# Varnmouth morning forecast — assembled from small phrase chunks
# so the line can be tweaked piece by piece later.

CITY = "Varnmouth"

# weather in two acts: first the flakes, then the clear sky
_WEATHER_BITS = (
    "snow flurries",
    ", then blue sky",
)

# the commuter's small miracle at the stop
_STOP_BITS = (
    "The bus stop heater works today",
    " \u2014 miracles do happen before 9 AM",
)


def _join(parts):
    return "".join(parts)


def build_forecast():
    opening = "In " + CITY + ", "
    weather = _join(_WEATHER_BITS)
    stop = _join(_STOP_BITS)
    sentence = opening + weather + "." + " " + stop + "."
    return sentence


def main():
    line = build_forecast()
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()

def process_buffer_stream(
    packets: list,
    max_packet_limit: float = 250.0,
    alert_threshold: float = 800.0
) -> float:
    """ Обрабатывает поток сетевых пакетов и считает общий объём.
    Args:
        packets (list): Список размеров пакетов.
        max_packet_limit (float): Максимальный размер пакета.
        alert_threshold (float): Критический объём данных.

    Returns:
        float: Общий объём принятых пакетов.
    """
    total_volume: float = 0.0
    current_index: int = 0

    while current_index < len(packets):
        packet_size = packets[current_index]

        if packet_size <= 0.0:
            current_index += 1
            continue

        if packet_size >= alert_threshold:
            break

        if packet_size <= max_packet_limit:
            total_volume += packet_size

        current_index += 1

    return round(total_volume, 2)

print(process_buffer_stream.__doc__)
print(process_buffer_stream([45.5, -10.0, 120.0, 310.0, 85.0]))
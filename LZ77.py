


def lz77_compress(data, window_size, lookahead_buffer_size):
    compressed_data = []
    current_position = 0

    while current_position < len(data):
        match_length = 0
        match_offset = 0

        for i in range(1, min(lookahead_buffer_size, len(data) - current_position)):
            window_start = max(0, current_position - window_size)
            window_substr = data[current_position:current_position + i]
            match_index = window_start + window_substr.rfind(window_substr)

            if match_index >= current_position or data[match_index:match_index + i] != window_substr:
                break

            match_length = i
            match_offset = current_position - match_index

        if match_length > 0:
            compressed_data.append((match_offset, match_length, data[current_position + match_length]))
            current_position += match_length + 1
        else:
            compressed_data.append((0, 0, data[current_position]))
            current_position += 1

    return compressed_data



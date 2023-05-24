from LZ77 import lz77_compress

secret = ('password123', 'choko55')
match_data = ()
count = 0
saved_data = list()

check = True
window_size = 4
lookahead_buffer_size = 5
for i in range(3):
    data = input('Input your text -->:')

    saved_data.append(data)

    compressed_data = lz77_compress(data, window_size, lookahead_buffer_size)
    print("Compressed data:", compressed_data)
aa = len(saved_data)
for i in range(len(saved_data) - 1):

    if saved_data[i][:-1] == saved_data[i + 1][:-1]:
        print(f"guess{i} (n-1) matches with guess{i + 1}(n-1)")

    elif saved_data[i][:-1] == saved_data[i + 2][:-1]:
        print(f"guess{i + 1} (n-1) matches with guess{i + 2}(n-1)")
        if i + 2 >= len(saved_data) - 1:
            break
    else:
        print("No matching guess was found.")

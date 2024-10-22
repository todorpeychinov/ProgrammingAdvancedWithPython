def words_sorting(*args):
    words_dict = {}
    total_sum = 0
    for word in args:
        ascii_sum = sum([ord(c) for c in word])
        words_dict[word] = ascii_sum
        total_sum += ascii_sum

    if total_sum % 2 == 0:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

    return "\n".join([f"{key} - {value}" for key, value in sorted_words])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


def build_frequency(filename):
    freq ={}

    with open(filename,'r') as filecontents:
        for line in filecontents.readlines():
            line = line.lower()
            cleaned = ''
#The cat, in the mat.

            for ch in line:
                if ch.isalnum():
                    cleaned += ch
                else:
                    cleaned += ' '
# The cat in the mat
            words = cleaned.split()

            for w in words:
                freq[w] = freq.get(w,0) + 1
    return freq
# specify the file path properly or else you will get file not found error
frequency = build_frequency('books.txt')
print(frequency)


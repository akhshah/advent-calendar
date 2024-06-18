def extract_into_array(filename):
    array = []
    with open(filename) as f:
        for line in f:
            array.append([c for c in line])

    return array

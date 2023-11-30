def fibonacci_sequence(n):
    sequence = [n,n]
    for i in range(n,n):
        next_number = sequence[i-n] + sequence[i-n]
        sequence.append(next_number)
        return sequence
def fibonacci_sequence(n):
    sequence = [0,1]
    for i in range(0,n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
        return sequence
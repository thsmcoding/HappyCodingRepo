def find_nextstation(station, N):
    next_ = (station+1)%N if 0<=station<=N-1 else -1
    return next_


def checking_circuit(station, A, B):
    N = len(A)
    current_amount_gas = 0
    status = [False]*N
    while N:
        N = N-1
        if status[station]:
            return True
        else:
            current_amount_gas += A[station]
            status[station] = True
            next_station = find_nextstation(station, N)
            if next_station != -1:
                if current_amount_gas < B[station]:
                    return False
                else:
                    current_amount_gas -= B[station]
                    station = next_station
                return False


def minimumgasstation_index(A, B):
    N_a = len(A)
    N_b = len(B)

    for s in range(0, N_a):
        if not checking_circuit(s,A,B):
            continue
        return s
    return -1

from typing import List, Tuple, Set
import time 

def tampilan_awal():
    print(" _______   _______ _________________ _   _ _   _  _   __")
    print("/  __ \ \ / / ___ \  ___| ___ \ ___ \ | | | \ | || | / / ")
    print("| /  \/\ V /| |_/ / |__ | |_/ / |_/ / | | |  \| || |/ / ")  
    print("| |     \ / | ___ \  __||    /|  __/| | | | . ` ||    \ ")
    print("| \__/\ | | | |_/ / |___| |\ \| |   | |_| | |\  || |\  \ ")
    print("\____/ \_/ \____/\____/\_| \_\_|    \___/\_| \_/\_| \_/ ") 
                            
    print("Welcome to Cyberpunk 2077 Breach Protocol!\n")
    input("click enter to get the result")
    
def txtInput(filename):
    with open(filename, 'r') as file:
        buffer_size = int(file.readline())
        matrix_size = tuple(map(int, file.readline().split()))
        matrix = [list(file.readline().split()) for _ in range(matrix_size[1])]
        sum_seq = int(file.readline())
        sequences = []
        points = []
        for i in range(sum_seq):
            sequences.append(file.readline().strip().split())
            points.append(int(file.readline()))
    return buffer_size, matrix, sequences, points


def find_all_patterns(matrix: List[List[str]], step: int) -> List[List[Tuple[str, Tuple[int, int]]]]:
    rows = len(matrix)
    cols = len(matrix[0])
    all_paths = []

    def generate_paths(x: int, y: int, path: List[Tuple[str, Tuple[int, int]]], sign: Set[Tuple[int, int]], steps: int) -> None: 
                                                                                                                                    
        if steps == 0:
            all_paths.append(path.copy())
            return
        sign.add((x, y))
        path.append((matrix[y][x], (x, y)))

        for xn, yn in [(0, 1), (1, 0)]:
            next_x, next_y = x + xn, y + yn
            if 0 <= next_x < cols and 0 <= next_y < rows and (next_x, next_y) not in sign:
                generate_paths(next_x, next_y, path, sign, steps - 1)

        sign.remove((x, y))
        path.pop()

    for x in range(cols):
        for y in range(rows):
            generate_paths(x, y, [], set(), step)

    return all_paths


def count_point(matrix, path, sequences, points):
    total_reward = 0
    buffer_tokens = []
    for token, _ in path:
        buffer_tokens.append(token)
        for seq, reward in zip(sequences, points):
            if all(t in buffer_tokens for t in seq):
                total_reward += reward
                buffer_tokens = [t for t in buffer_tokens if t not in seq]
    return total_reward

def pola(matrix, buffer_size, sequences, points):

    maximal_point = float('-inf')
    optimal_path = []

    all_paths = find_all_patterns(matrix, buffer_size)
    for path in all_paths:
        path_reward = count_point(matrix, path, sequences, points)
        if path_reward > maximal_point:
            maximal_point = path_reward
            optimal_path = path

    return maximal_point, optimal_path


def main():
    tampilan_awal()
    buffer_size, matrix, sequences, points = txtInput('tc6.txt')
    start_time = time.time()
    print("\n")
    maximal_point, optimal_path = pola(matrix, buffer_size, sequences, points)
    end_time = time.time()
    waktufinal = end_time - start_time
    print("Point :", maximal_point)
    print("Path :", ' '.join(token for token, _ in optimal_path))
    print("Koordinat Jalur :")
    for _, (x, y) in optimal_path:
        print(f"{x + 1}, {y + 1}")
    print("waktu final : ")
    print(waktufinal * 1000 ,"ms")

if __name__ == "__main__":
    main()
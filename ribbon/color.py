# N is the length

def solve_ribbon_problem():
    with open("ribbon.in") as f:
        n, c = map(int, f.readline().split())
        colors = [int(f.readline().strip()) for _ in range(n)]
    
    # Initialize variables to store the best solution
    max_length = 0
    best_color = -1
    best_start_cut = 0
    best_end_cut = 0
    
    # Try to find the best solution by checking each color
    for color in range(1, c + 1):
        start = 0
        end = n - 1
        
        # Find the first and last occurrence of the current color
        while start < n and colors[start] != color:
            start += 1
        while end >= 0 and colors[end] != color:
            end -= 1
        
        # Calculate the length of the ribbon if both ends are the same color
        if start < end:
            length = end - start + 1
            if length > max_length:
                max_length = length
                best_color = color
                best_start_cut = start
                best_end_cut = n - end - 1
    
    # Write the results to the output file
    with open("ribbon.out", "w") as f:
        f.write(f"{max_length}\n")
        f.write(f"{best_color}\n")
        f.write(f"{best_start_cut}\n")
        f.write(f"{best_end_cut}\n")

# Call the function to solve the problem
solve_ribbon_problem()
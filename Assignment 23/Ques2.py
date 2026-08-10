import multiprocessing
def sum_even_numbers(n):
    """Calculates the sum of all even numbers from 1 to n using math."""
    # The count of even numbers up to n is n // 2
    count = n // 2
    # Sum formula for first 'count' even numbers: count * (count + 1)
    return count * (count + 1)

def main():
        # Sample input list
    input_list = [10,25,100, 1000, 5000, 10000]
    
    # Initialize a Pool with the default number of CPU cores
    with multiprocessing.Pool() as pool:
        # pool.map distributes the list items across processes automatically
        results = pool.map(sum_even_numbers, input_list)

 # Map the inputs to their respective outputs
    output_dict = dict(zip(input_list, results))
    print(output_dict)

if __name__ == '__main__':
    main()
import time

while True:
    try:
        # Monitor the file for changes
        with open("data.txt", "r") as file:
            data = file.read().strip()
        
        if data:
            # Perform complex math or AI computations
            result = f"Python processed: {data}"
            
            # Write the result back to the file
            with open("result.txt", "w") as result_file:
                result_file.write(result)
            
            # Signal C++ that processing is done (for example, by creating a flag file)
            with open("python_done.flag", "w") as flag_file:
                pass

            # Optional: Sleep to avoid continuous checking
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

import math

def increase_cpu_utilization():
    try:
        while True:
            # Perform a CPU-intensive operation
            result = 0
            for i in range(1000000):
                result += math.sqrt(i)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to stop the script
        pass
    finally:
        print("Exiting script.")

if __name__ == "__main__":
    try:
        increase_cpu_utilization()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


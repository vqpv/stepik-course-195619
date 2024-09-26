def calculate_high_low_avg(*args, log_to_console=False):
    high = max(args)
    low = min(args)
    avg = (high + low) / 2
    if log_to_console:
        print(f"high={high}, low={low}, avg={avg}")
    return avg

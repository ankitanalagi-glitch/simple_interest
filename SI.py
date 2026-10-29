def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    

    Formula: SI = (P * R * T) / 100
    
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")

    return (principal * rate * time) / 100


def main():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (% per year): "))
        time = float(input("Enter time (in years): "))

        interest = calculate_simple_interest(principal, rate, time)

        print(f"\nPrincipal Amount : {principal:.2f}")
        print(f"Rate of Interest : {rate:.2f}%")
        print(f"Time             : {time:.2f} years")
        print(f"Simple Interest  : {interest:.2f}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
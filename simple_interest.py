# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.

    :param principal: The principal amount (initial investment)
    :param rate: The annual interest rate (in percentage)
    :param time: The time the money is invested or borrowed for (in years)
    :return: The simple interest
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative")
    
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in percentage): "))
        time = float(input("Enter the time (in years): "))

        interest = calculate_simple_interest(principal, rate, time)
        print(f"The simple interest is: {interest}")
    except ValueError as e:
        print(e)

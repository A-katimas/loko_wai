
def test_temperature_input(temp_str: str):
    if temp_str.isdigit():
        if int(temp_str) < 0 :
            return (f"Error: {temp_str}°C is too cold for plants (min 0°C) ")
        elif int(temp_str)> 40 :
            return(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        else:
            return(f"Temperature {temp_str}°C is perfect for plants!")
    else:
        return(f"Error: '{temp_str}' is not a valid number")

def main():
     temperature= input("Testing temperature: ")
     print(test_temperature_input(temperature))


if __name__ == "__main__" :
	main()
def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """Return formatted text with optional prefix/suffix, capitalization, and length trimming."""
    if capitalize:
        text = text.capitalize()

    formatted = f"{prefix}{text}{suffix}"

    if isinstance(max_length, int) and max_length > 0:
        return formatted[:max_length]
    return formatted

def main():
    text = input("Text: ")
    prefix = input("Prefix (optional): ")
    suffix = input("Suffix (optional): ")
    
    cap_flag = input("Capitalize (y/n): ").strip().lower()
    capitalize = cap_flag == 'y'

    max_length = None
    length_input = input("Max length (press Enter to skip): ")
    if length_input.isdigit():
        max_length = int(length_input)
    elif length_input:
        print("Ignoring invalid length input.")

    try:
        output = format_text(text, prefix, suffix, capitalize, max_length)
        print("Formatted:", output)
    except Exception as e:
        print(f"Error formatting text: {e}")

if __name__ == "__main__":
    main()

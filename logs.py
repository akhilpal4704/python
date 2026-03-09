def read_log_lines(filepath):
    """
    Creates a generator that reads a log file, yielding valid, non-comment lines.
 
    Args:
        filepath (str): The path to the log file.
 
    Yields:
        str: A stripped, non-empty, non-comment line from the file.
 
    Raises:
        TypeError: If filepath is not a string.
        ValueError: If filepath is an empty string.
        FileNotFoundError: If the file at filepath does not exist.
    """
    # Input validation: Ensure the filepath is a non-empty string.
    if not isinstance(filepath, str):
        raise TypeError("Filepath must be a string.")
    if not filepath:
        raise ValueError("Filepath cannot be an empty string.")
 
    # Using 'with open' ensures the file is automatically closed.
    # A FileNotFoundError will be raised here if the path is invalid.
    with open(filepath, 'r') as file:
        # Iterating over the file object reads it line-by-line.
        for line in file:
            # Remove leading/trailing whitespace (including newlines).
            stripped_line = line.strip()
 
            # Check if the line is a comment (starts with '#') or is empty.
            if not stripped_line or stripped_line.startswith('#'):
                continue
 
            # If the line is valid, yield it.
            yield stripped_line
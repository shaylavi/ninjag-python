def ninja_io(args):
    """Return the inputs/outputs as a single string

    Args:
        args (str | list): a string or list of strings
    Returns:
        a string
    """
    if isinstance(args, str):
        return args
    elif isinstance(args, list):
        return " ".join(args)
    else:
        return ""

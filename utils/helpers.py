import yaml

def load_yaml_config(file_path):
    """
    Loads a YAML configuration file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed configuration.
    """
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Warning: Config file {file_path} not found. Using default settings.")
        return {}

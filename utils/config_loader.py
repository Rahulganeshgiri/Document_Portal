import yaml

def load_config(config_path: str=r"C:\Users\Rahul\OneDrive\Desktop\Document_Portal\config\config.yaml")  -> dict:
    with open(config_path,'r') as file:
        config=yaml.safe_load(file)
    print(config)
    return config

config=load_config(r"C:\Users\Rahul\OneDrive\Desktop\Document_Portal\config\config.yaml")
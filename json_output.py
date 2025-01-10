import json

def create_json_output(object_hierarchy):
    output_data = json.dumps(object_hierarchy, indent=4)
    return output_data

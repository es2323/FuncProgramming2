import json
from functools import singledispatch

# ----- Core Parser -----
@singledispatch
def parse_data(data):
    """Handles primitive types"""
    return data

@parse_data.register(dict)
def _(data):
    return {k: parse_data(v) for k, v in data.items()}

@parse_data.register(list)
def _(data):
    return [parse_data(item) for item in data]

# ----- Specialized Employee Parser -----
def parse_employee(data):
    return {
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "age": data["age"],
        "address": parse_data(data["address"])  # Reuses core parser
    }

def parse_department(data):
    return {
        "name": data["name"],
        "employees": [parse_employee(e) for e in data["employees"]]
    }

# ----- Smart Parser (Auto-detects structure) -----
def smart_parse(data):
    if isinstance(data, dict):
        # Detect employee structure
        if all(k in data for k in ["firstName", "lastName", "age", "address"]):
            return parse_employee(data)
        # Detect department structure
        elif "employees" in data and isinstance(data["employees"], list):
            return parse_department(data)
    return parse_data(data)  # Fallback to generic

# ----- Printer -----
def print_hybrid(data, indent=0):
    if isinstance(data, dict):
        if "firstName" in data:  # Employee
            print("  " * indent + f"Employee: {data['firstName']} {data['lastName']}")
            print("  " * (indent+1) + f"Age: {data['age']}")
            print("  " * (indent+1) + "Address:")
            print_hybrid(data["address"], indent + 2)
        elif "name" in data:  # Department
            print("  " * indent + f"Department: {data['name']}")
            print_hybrid(data["employees"], indent + 1)
        else:  # Generic dict
            for k, v in data.items():
                print("  " * indent + f"{k}:")
                print_hybrid(v, indent + 1)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print("  " * indent + f"Item {i}:")
            print_hybrid(item, indent + 1)
    else:
        print("  " * indent + str(data))

# ----- Example Usage -----
employee_json = '''
{
  "accounting": [{
    "firstName": "John",
    "lastName": "Doe",
    "age": 23,
    "address": {
      "street": "123 Main St",
      "zip": "12345"
    }
  }],
  "sales": [{
    "firstName": "Sally",
    "lastName": "Green",
    "age": 27,
    "address": {
      "street": "456 Main St",
      "zip": "23456"
    }
  }]
}
'''

generic_json = '''
{
  "system": {
    "components": ["CPU", "Memory"],
    "config": {
      "timeout": 30,
      "retries": 3
    }
  }
}
'''

# Parse and print employee data
print("\n=== Employee Structure ===")
employee_data = json.loads(employee_json)
parsed_employee = {k: [smart_parse(e) for e in v] for k, v in employee_data.items()}
print_hybrid(parsed_employee)

# Parse and print generic data
print("\n=== Generic Structure ===")
generic_data = json.loads(generic_json)
parsed_generic = smart_parse(generic_data)
print_hybrid(parsed_generic)



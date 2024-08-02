import json
import argparse

def get_top_attack_techniques(file_path, capability_group=None, technique_id=None, top_n=10):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Filter techniques by capability_group and technique_id
    techniques = [item for item in data['mapping_objects'] if 
                  (capability_group is None or item.get('capability_group') == capability_group) and
                  (technique_id is None or item.get('attack_object_id') == technique_id)]
    
    # Extract relevant data
    technique_list = [
        {
            'capability_id': technique['capability_id'],
            'score_category': technique['score_category'],
            'score_value': technique['score_value'],
            'attack_object_id': technique['attack_object_id'],
            'attack_object_name': technique['attack_object_name']
        }
        for technique in techniques
    ]
    
    # Sort the techniques by score value in descending order
    sorted_techniques = sorted(technique_list, key=lambda x: x['score_value'], reverse=True)
    
    # Get the top N techniques
    top_techniques = sorted_techniques[:top_n]
    
    return top_techniques

def list_capability_groups(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    capability_groups = set(item.get('capability_group') for item in data['mapping_objects'])
    
    print("Available Capability Groups:")
    for idx, group in enumerate(sorted(capability_groups), start=1):
        print(f"{idx}. {group}")

def list_attack_techniques(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Filter out entries where attack_object_id or attack_object_name is None
    attack_techniques = set((item.get('attack_object_id'), item.get('attack_object_name')) 
                            for item in data['mapping_objects'] 
                            if item.get('attack_object_id') and item.get('attack_object_name'))
    
    print("Available Attack Techniques:")
    for idx, (attack_id, attack_name) in enumerate(sorted(attack_techniques), start=1):
        print(f"{idx}. {attack_id}: {attack_name}")

def main():
    parser = argparse.ArgumentParser(description="Get the top attack techniques based on their score value")
    parser.add_argument('-i', '--input', required=True, help="Input JSON file")
    parser.add_argument('-cg', '--capability_group', help="Capability Group to filter")
    parser.add_argument('-t', '--technique', help="Attack Technique ID to filter")
    parser.add_argument('-n', '--number', type=int, default=10, help="Number of top techniques to retrieve")
    parser.add_argument('--list-groups', action='store_true', help="List all available capability groups")
    parser.add_argument('--list-attacks', action='store_true', help="List all available attack techniques")

    args = parser.parse_args()

    if args.list_groups:
        list_capability_groups(args.input)
    elif args.list_attacks:
        list_attack_techniques(args.input)
    else:
        top_techniques = get_top_attack_techniques(args.input, args.capability_group, args.technique, args.number)

        # Print the header
        print(f"{'Rank':<5}{'Capability Group':<60}{'Score Category':<25}{'Score Value':<15}{'Attack Object ID':<20}{'Attack Object Name':<35}")

        # Print the top techniques with ranking
        for rank, technique in enumerate(top_techniques, start=1):
            print(f"{rank:<5}{technique['capability_id']:<60}{technique['score_category']:<25}{technique['score_value']:<15}{technique['attack_object_id']:<20}{technique['attack_object_name']:<35}")

if __name__ == "__main__":
    main()

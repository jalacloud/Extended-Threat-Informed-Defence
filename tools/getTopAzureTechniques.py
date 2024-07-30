# Created by Jason Layton

import json
import argparse

def get_top_attack_techniques(file_path, capability_group, top_n=10):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Filter techniques by capability_group
    techniques = [item for item in data['mapping_objects'] if item.get('capability_group') == capability_group]
    
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

def main():
    parser = argparse.ArgumentParser(description="Get the top attack techniques based on their score value")
    parser.add_argument('-i', '--input', required=True, help="Input JSON file")
    parser.add_argument('-cg', '--capability_group', required=True, help="Capability Group to filter")
    parser.add_argument('-n', '--number', type=int, default=10, help="Number of top techniques to retrieve")

    args = parser.parse_args()

    top_techniques = get_top_attack_techniques(args.input, args.capability_group, args.number)

    # Print the header
    print(f"{'Rank':<5}{'Capability ID':<35}{'Score Category':<25}{'Score Value':<15}{'Attack ID':<20}{'Attack Name':<35}")

    # Print the top techniques with ranking
    for rank, technique in enumerate(top_techniques, start=1):
        print(f"{rank:<5}{technique['capability_id']:<35}{technique['score_category']:<25}{technique['score_value']:<15}{technique['attack_object_id']:<20}{technique['attack_object_name']:<35}")

if __name__ == "__main__":
    main()

# Created by Jason Layton (July 30th 2024)
# This script takes exported JSON files (layers) from MITRE ATT&CK Navigator and prints the top N techniques based on score.
# Techniques with a higher score overlap with other TA behaviours (techniques) and are commonly used among the chosen threat actors in their attack TTPs.

import json
import argparse

def get_top_attack_techniques(file_path, top_n=10):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the techniques
    techniques = data.get('techniques', [])
    
    # Extract relevant data
    technique_list = [
        {'techniqueID': technique['techniqueID'], 'tactic': technique['tactic'], 'score': technique['score']}
        for technique in techniques
    ]
    
    # Sort the techniques by score in descending order
    sorted_techniques = sorted(technique_list, key=lambda x: x['score'], reverse=True)
    
    # Get the top N techniques
    top_techniques = sorted_techniques[:top_n]
    
    return top_techniques

def main():
    parser = argparse.ArgumentParser(description="Get the top attack techniques based on their score")
    parser.add_argument('-i', '--input', required=True, help="Input JSON file")
    parser.add_argument('-n', '--number', type=int, default=10, help="Number of top techniques to retrieve")

    args = parser.parse_args()

    top_techniques = get_top_attack_techniques(args.input, args.number)

    # Print the header
    print(f"{'Rank':<5}{'TechniqueID':<15}{'Tactic':<25}{'Score':<10}")

    # Print the top techniques with ranking
    for rank, technique in enumerate(top_techniques, start=1):
        print(f"{rank:<5}{technique['techniqueID']:<15}{technique['tactic']:<25}{technique['score']:<10}")

if __name__ == "__main__":
    main()


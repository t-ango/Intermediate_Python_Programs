'''
Find Genes in a Genome Sequence

This program identifies and extracts genes from a given genome sequence. A gene is defined as a sequence starting with the codon "ATG" and ending with one of the stop codons ("TAG", "TAA", "TGA"). The extracted genes are returned as a list.

## Functions

### 1. `main()`
- Prompts the user to input a genome string.
- Calls the `find_genes` function to extract genes.
- Displays the extracted genes as a comma-separated string or a message indicating no genes were found.

### 2. `find_genes(genome)`
- Finds and extracts genes from the given genome string.
- Parameters:
  - `genome`: A string representing the genome sequence.
- Returns:
  - A list of gene sequences (strings) found in the genome.
- Logic:
  - Searches for the start codon "ATG".
  - Searches for the nearest stop codon ("TAG", "TAA", or "TGA") after each start codon.
  - Extracts the sequence between the start codon and the nearest stop codon.

## Example Usage
Enter a genome string: ATGAAATAGATGCCCTGA Output: AAA, CCC


## Applications
- Biological sequence analysis.
- Demonstrates basic string processing and pattern matching in Python.
'''

def main():
    genome_sequence = input("Enter a genome string: ").upper()
    genes = find_genes(genome_sequence)
    
    if genes:
        print(",".join(genes))
    else:
        print("No gene is found.")
        

def find_genes(genome):
    start_sequense = "ATG"
    stop_sequenses = ["TAG", "TAA", "TGA"]
    
    genes_found = []
    start_index = genome.find(start_sequense)
    
    while start_index != -1:
        end_index = -1
        for stop_sequense in stop_sequenses:
            stop_index = genome.find(stop_sequense, start_index + 3)
            if stop_index != -1:
                if end_index == -1 or stop_index < end_index:
                    end_index = stop_index
        
        if end_index != -1:
            genes_found.append(genome[start_index + 3:end_index])
        
        start_index = genome.find(start_sequense, start_index + 3)
    
    return genes_found


main()
'''
Find Genes in a Genome Sequence (Revised Version)

This program refines the process of identifying and extracting genes from a given genome sequence. 
It introduces additional constraints to ensure extracted genes are biologically valid and enhances 
error handling for edge cases.

## Functions

### 1. `main()`
- Prompts the user to input a genome string.
- Calls the `findGenes` function to extract genes.
- Displays the extracted genes or a message indicating no genes were found.

### 2. `findGenes(genome: str) -> list`
- Finds and extracts genes from the given genome string.
- Parameters:
  - `genome`: A string representing the genome sequence.
- Returns:
  - A list of gene sequences (strings) found in the genome or a list with the message `"No genes found"`.
- Improvements:
  - Ensures stop codons are in the correct reading frame relative to the start codon.
  - Excludes nested "ATG" sequences within extracted genes.
  - Validates that extracted genes contain only valid nucleotide letters (`A`, `T`, `G`).

## Example Usage
Enter a genome string: ATGAAATAGATGCCCTGA Output: ['AAA', 'CCC']


## Key Enhancements
1. Moved the `"if genes_found"` check from `main` to `findGenes`.
2. Corrected an issue where the program failed to return `"No genes found"`. Modified `return "No genes found"` to `return ["No genes found"]` to ensure consistent return types.
3. Addressed incorrect output for sequences with invalid reading frames by adding the condition `(stop_index - start_index) % 3 == 0`.
4. Fixed output errors for nested "ATG" sequences by adding the condition `"ATG" not in gene`.
5. Improved validation by ensuring extracted genes contain only valid nucleotide letters using `all(letter in "ATG" for letter in gene)`.

## Applications
- Improved biological sequence analysis with stricter gene validation.
- Demonstrates refined string processing and debugging in Python.
'''

def main():
    genome_sequence = input("Enter a genome string: ").upper()
    genes = findGenes(genome_sequence)
    print (genes)
        

def findGenes(genome:str)-> list:
    
    start_sequense = "ATG"
    stop_sequenses = ["TAG", "TAA", "TGA"]
    
    genes_found = []
    start_index = genome.find(start_sequense)
    
    while start_index != -1:
        end_index = -1
        for stop_sequense in stop_sequenses:
            stop_index = genome.find(stop_sequense, start_index + 3)
            if stop_index != -1 and (stop_index - start_index)%3 == 0:
                if end_index == -1 or stop_index < end_index:
                    end_index = stop_index
        
        if end_index != -1:
            gene = genome[start_index + 3: end_index]
            if "ATG" not in gene and all(letter in "ATG" for letter in gene):
                genes_found.append(genome[start_index + 3:end_index])
        
        start_index = genome.find(start_sequense, start_index + 3)
    
    if genes_found:
        return ",".join(genes_found)
    else:
        return ["No genes found"]
    

main()



    
    




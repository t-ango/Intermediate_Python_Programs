# Gene Finder Project

This project identifies genes from a genome sequence based on biological constraints. 
It includes an original implementation, a reworked version with enhanced functionality, and a suite of unit tests to validate the functionality.

---

## Files in the Folder

1. **`find_genes.py`**:
   - The original implementation of the gene-finding function.
   - Extracts genes starting with "ATG" and ending with one of the stop codons ("TAG", "TAA", "TGA").
   - Outputs the extracted genes as a comma-separated string.

2. **`find_genes_reworked.py`**:
   - A refined version of the original implementation with the following enhancements:
     - Validates reading frame alignment between start and stop codons.
     - Ensures genes do not contain nested "ATG" sequences.
     - Filters out sequences with invalid nucleotide letters.
     - Improves return handling for cases with no genes found.

3. **`test_find_genes.py`**:
   - A suite of unit tests for the `findGenes` function in `find_genes_reworked.py`.
   - Covers edge cases, typical scenarios, and error handling.
   - Uses the `unittest` module for testing.

---

## Features

### Gene Finder
- Extracts valid genes from genome sequences.
- Enforces biological constraints:
  - Start codon: `"ATG"`.
  - Stop codons: `"TAG"`, `"TAA"`, `"TGA"`.
  - Valid nucleotide letters: `"A"`, `"T"`, `"G"`.

### Unit Testing
- Comprehensive test suite ensures correctness and reliability.
- Validates function behavior across:
  - Empty inputs.
  - Invalid and valid genome sequences.
  - Complex sequences with overlapping or multiple genes.

---

## How to Run

1. **Run the Gene Finder**:
   - Original Implementation:
     ```bash
     python3 find_genes_original.py
     ```
   - Reworked Implementation:
     ```bash
     python3 find_genes_reworked.py
     ```

2. **Run Unit Tests**:
   ```bash
   python3 test_find_genes_reworked.py

**Example Output**

Input:

Enter a genome string: ATGTTTTGAATGGGGTAA
Output (Reworked):

TTT,GGG

**Applications**

Biological sequence analysis.
Demonstrates iterative development and test-driven practices.
Provides a foundation for more complex genomic analysis tools.

**Requirements**

Python 3.x

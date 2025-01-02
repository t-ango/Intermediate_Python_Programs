'''
Unit Tests for Gene Finder (Reworked Version)

This file contains unit tests for the `findGenes` function in the reworked `find_genes_reworked.py` file. These tests validate the function's behavior across various edge cases and typical scenarios.

## Test Cases

### 1. Empty String
- Input: `""`
- Expected Output: `["No genes found"]`
- Verifies that the function correctly handles empty genome strings.

### 2. Rubbish String
- Input: `"I AM A STRING WITH NO GENES WHATSOEVER"`
- Expected Output: `["No genes found"]`
- Ensures the function can handle strings with no valid gene sequences.

### 3. Simple Gene
- Input: `"ATGTTTGGGTAG"`
- Expected Output: `"TTTGGG"`
- Tests extraction of a valid gene.

### 4. Multiple Start Codons
- Input: `"ATGTTTTAATGATAG"`
- Expected Output: `"TTT"`
- Checks that the function handles overlapping genes correctly.

### 5. Less Than 3 Letters in Gene
- Input: `"ATGAATGA"`
- Expected Output: `["No genes found"]`
- Ensures genes shorter than 3 letters are excluded.

### 6. No Start Codon
- Input: `"TTTTGA"`
- Expected Output: `["No genes found"]`
- Verifies the function's behavior when there is no "ATG" start codon.

### 7. Two Valid Genes
- Input: `"ATGTTTTGAATGGGGTAA"`
- Expected Output: `"TTT,GGG"`
- Tests extraction of multiple genes from a genome sequence.

### 8. No Stop Codon
- Input: `"ATGTTTGGG"`
- Expected Output: `["No genes found"]`
- Ensures the function returns no genes if there is no valid stop codon.

### 9. Long Genome String
- Input: `"TGTTATGTTTGGGAAATTTGGGAAATTTGGGAAAGGGTTTTGATTTGGGAAATGTTTGGGAAATGATT"`
- Expected Output: `"TTTGGGAAATTTGGGAAATTTGGGAAAGGGTTT,TTTGGGAAA"`
- Validates the function's performance and correctness on long sequences.

### 10. Multiple Start Codons Without Stop Codon
- Input: `"TTATGATGGGGTAG"`
- Expected Output: `"GGG"`
- Ensures that only valid genes are extracted.

### 11. Invalid Letters in Gene
- Input: `"ATGMDFTAG"`
- Expected Output: `["No genes found"]`
- Tests the function's ability to ignore invalid gene sequences containing non-nucleotide letters.

## Framework
- The `unittest` module is used to structure and run the tests.

## Running the Tests
Run the tests using:
```bash
python3 test_find_genes_reworked.py
Applications

Ensures correctness and reliability of the findGenes function across edge cases.
Demonstrates best practices in unit testing and test-driven development. '''

from find_genes_reworked import findGenes
import unittest   # The test framework

class Test_genome(unittest.TestCase):
    def test_emty_string(self):
        result = findGenes("")
        self.assertEqual(result[0], "No genes found")    

    def test_rubbish_string(self):
        result = findGenes("I AM A STRING WITH NO GENES WHATSOEVER")
        self.assertEqual(result[0], "No genes found")

    def test_findgenes_string(self):
        result = findGenes("ATGTTTGGGTAG")
        self.assertEqual(result, "TTTGGG")

    def test_findgenes_string2(self):
        result = findGenes("ATGTTTTAATGATAG")
        self.assertEqual (result,"TTT")

    def test_lessthan3letters_string(self):
        result = findGenes("ATGAATGA")
        self.assertEqual (result[0], "No genes found")

    def test_no_start_string(self):
        result = findGenes("TTTTGA")
        self.assertEqual (result[0], "No genes found")

    def test_2genestrings(self):
        result = findGenes ("ATGTTTTGAATGGGGTAA")
        self.assertEqual (result, "TTT,GGG")

    def test_no_stop_string(self):
        result = findGenes ("ATGTTTGGG")
        self.assertEqual (result [0], "No genes found")

    def test_long_string(self):
        result = findGenes("TGTTATGTTTGGGAAATTTGGGAAATTTGGGAAAGGGTTTTGATTTGGGAAATGTTTGGGAAATGATT")
        self.assertEqual (result, "TTTGGGAAATTTGGGAAATTTGGGAAAGGGTTT,TTTGGGAAA")

    def test_2starts_string(self):
        result = findGenes("TTATGATGGGGTAG")
        self.assertEqual (result, "GGG")

    def test_wrongletters(self):
        result = findGenes("ATGMDFTAG")
        self.assertEqual (result[0], "No genes found")

    

if __name__ == '__main__':

    unittest.main()
# 🧬 Bioinformatics Analysis of blaTEM-1 Beta-Lactamase Gene

## 📁 Project Overview

This project investigates the **blaTEM-1** beta-lactamase gene using basic bioinformatics tools and Python scripting. It serves both as a learning exercise and a portfolio project to demonstrate bioinformatics skills.

---

## 📌 Objectives

- Search for homologs of the blaTEM-1 gene using NCBI BLAST.
- Retrieve and analyze homologous sequences.
- Perform basic sequence analysis (length, GC content, translation).
- Document workflow and results clearly.

---

## 🛠️ Tools & Technologies

- **Operating System:** Windows 11
- **Languages:** Python 3.11
- **Libraries:** BioPython
- **Tools Used:** NCBI BLASTn, Clustal Omega (later), matplotlib (optional)

---

## 🔄 Workflow Summary

### 🔍 Phase 1: Retrieve Reference Sequence
- Downloaded blaTEM-1 DNA sequence in FASTA format from NCBI.

### 🚀 Phase 2: BLAST Homolog Search
- Used NCBI BLASTn to search for similar sequences.
- Saved 3 hits for downstream analysis.

### 🧪 Phase 3: Sequence Analysis
- Parsed sequences using **BioPython**.
- Calculated:
  - Sequence lengths
  - GC content
  - Protein translation (first 30 amino acids)
- Saved results to `results/summary.txt`.

### 📊 Phase 4: [To be added]
- Multiple Sequence Alignment using Clustal Omega
- Mutation analysis and visualization

---

## 📂 Folder Structure
blaTEM1_project/
├── data/ # FASTA files (reference + hits)
├── scripts/ # Python scripts
├── results/ # Text output (summary.txt)
└── portfolio/ # Project write-up (summary.md)

---

## 📈 Sample Output

Example from `results/summary.txt`:
> OZ043779.1
Length: 142113 bp
GC content: 50.85%
First 30 aa (protein): VDKSSGELVTLTPNNNNTVQPVALMRLGVF 

---

## ✅ Skills Demonstrated

- Navigating public sequence databases
- Automating sequence analysis in Python
- File organization and reproducible workflow design
- Clear documentation of computational biology workflows

---

## 🚧 Next Steps

- Perform multiple sequence alignment (MSA)
- Visualize conserved regions and mutations
- Extend project to include phylogenetics or functional annotation

---

## 🙋‍♂️ Author

**Okurut Sylas**  
Final-year student, Biochemistry & Chemistry  
Makerere University


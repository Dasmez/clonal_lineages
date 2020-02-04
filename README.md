# clonal_lineages
Fall research project (Bioinformatics Institute)

Exploring properties of amino acids in immunoglobulin clonal lineages


Description: 
An antibody repertoire can be viewed as a collection of clonal lineages. Each clonal lineage presents a result of somatic hypermutagenesis and clonal selection and thus can be described as an evolutionary tree. The goal of this project is to analyze somatic hypermutations appearing in expanded clonal lineages and reveal associations between immunoglobulin positions and properties of amino acids generated through the mutation process.    

Goals:

(1) constructing evolutionary trees on various repertoire-sequencing datasets using IgEvolution tool;

(2) finding positions in immunoglobulins demonstrating strong selection for the certain trait of amino acid (hydrophobicity / size / charge / etc);

(3) designing an approach for estimating statistical significance of the results  


Research stages:

1. 1_clonal_tree_colouring.py takes as an input 2 files - lineage..._shms.txt (information about vertices and edges) and lineage..._seqs.txt (sequencing information) files.
Examples of files format are in master branch (lineage_example_seqs.txt and lineage_example_shms.txt)
As the main output file you will obtain an image of clonal tree (each aminoacid coloured with its own colour) - tree_example.pdf. Another output file (result.txt) is the list of all vertices from lineage_example_seqs.txt file


2. 2_variable positions.py takes lineage..._seqs.txt file and creates new fasta file (you can analize sequences using another applcation) and analyzes variability of each position.

3. 3_value_distribution.py can be used for visualisation of values range for each position (code is given for posifion 57).
This file also takes lineage..._shms.txt and lineage..._seqs.txt files and returns table with 4 columns (57	92	Q	-3.5): 1- position number, 2- vertice number, 3- amino acid, 4- isoelectronicity value.
Example of visualization using Rstudio for several positions - values_dist_example.png

4. 4_probability.py file uses previously obtained files and creates distribution of values for each position, determines range of distribution and calculates value of significance.


Literature:
You can find more about clonal lineages here - https://www.biorxiv.org/content/10.1101/725424v2

# TD Potential Cleavage Analyzer

 <p align="center">
<img src="https://img.shields.io/badge/python-3.9.13+-blue.svg" alt="Python Version"> 
<img src="https://img.shields.io/pypi/l/MSDIFF" alt="License">
</p>


## Contents
- [Abstract](#abstract)
- [Technical Description](#technical-description)
- [Requirements](#requirements)
    - [Packages](#packages)
- [How to run the Script](#how-to-run-the-script)
- [Input Data](#input-data)
    - [Identified Middle-Down Peptides](#identified-middle-down-peptides)
    - [Fasta File](#fasta-file)
- [Graphical User Interface](#graphical-user-interface)
    - [Initialization](#initialization)
    - [Data Analysis](#data-analysis)
    - [Visualization](#visualization)
- [Data Sets for Testing](#data-sets-for-testing)
- [Output](#output)
    - [Potential cleavage analysis of subsequence proteoforms](#potential-cleavage-analysis-of-subsequence-proteoforms)
    - [Cleavage Specificity](#cleavage-specificity)
    - [Analyze Potential Cleavage Fasta File](#analyze-potential-cleavage-fasta-file)
    - [N-terminal Methionine Excision](#n-terminal-methionine-excision)
    - [Proteoform Information: C- and N-terminal peptides](#proteoform-information-c--and-n-terminal-peptides)
    - [Visualization of Identified Peptides for Specific Proteins](#visualization-of-identified-peptides-for-specific-proteins)
- [Troubleshooting](#troubleshooting)
- [Contributions](#contributions)
- [Changelog](#changelog)
- [References](#references)
- [How to cite](#how-to-cite)
- [License](#license)




## Abstract

Middle-down proteomics aims to identify peptides in the range of 3-10 kDa. The tool analyzes the identified middle-down peptides and graphically displays various properties . The following analyses can be performed:

- Specificity analysis: Two-dimensional histogram of cleavage sites of the identified peptides. Determination of full-, semi- and un-specific peptides.
- Determination of the sequence coverage of all proteins. 
- Analysis of N-terminal Methionine Excision. 
- Visualization of identified peptides in respect to the full-length protein. 

The entire script is based on the script "Potential Cleavage Analyzer" (PTK, 2021). 



## Technical Description

For each peptide, the tool searches the corresponding full length protein in the fasta database and the peptides are examined for their cleavage sites (**Figure 1**). If the peptide can be assigned to multiple proteins, the tool checks if the corresponding amino acids N- and C-terminal are the same for all assigned proteins. If this is not the case, the peptide is not considered further due to ambiguity. N-terminally non-truncated peptides (or with only start methionine cleaved) are used for start methionine cleavage analysis. 

<img src="Various\TechnicalDescription.png" style="zoom:57%" alt="Result_Methionin_Cleavage"/>

**Figure 1**: Determination of potential cleavage sites by analyzing the identified peptides. The tool searches for each peptide their corresponding full length protein in the fasta file and identifies the potential cleavage sites. 



## Requirements

- Python 3.9.13 or higher

### Packages 

- Bio==1.5.3
- matplotlib==3.5.1
- pandas==1.4.2
- PyQt5==5.15.7
- pyteomics==4.5
- seaborn==0.11.2

  

## How to run the Script

Installation and use of Anaconda Distribution and its build-in command line prompt is highly recommended. In case you don't use Anaconda, make sure all required packages are installed upfront.

````powershell
$ cd <PATH/TO/SOURCES>
$ python GUI.py
````

 

## Input Data

### Identified Middle-Down Peptides 

The tool allows different input formats for the identified proteoforms: 

- Proteome Discoverer database results. Exported "proteoform results" as txt-files. If the search was performed within Proteome Discoverer, use the "File->Export->To Text" function to export the proteoform results as txt-file.

Note: Currently only results obtained from ProSightPD searches are supported. 

### Fasta File

Fasta file, which was also used for database search. If database search was performed against a XML file, download the corresponding Fasta-file from UniProt. 

  

## Graphical User Interface 

<center> <img src="Various\GUI.PNG" style="zoom:100%" alt="Graphical User Interface"/></center>

**Figure 2**: Graphical User Interface.

### Initialization

1. Fasta File. Opens file dialog to select a Fasta File, see [Input Data](##Input-Data) for details.
2. PD Result File. Opens file dialog to select a proteoform file, see [Input Data](##Input-Data) for details.
3. Select file format, see [Input Data](##Input-Data) for details. Select PDProSight-Version. 
4. Select Protease used (currently only GluC is supported).
5. Initialization: Reading of the input files and initialization of different analysis. This may take a while depending on the size of the input files. The progress of the calculations is displayed in the command line.  

### Data Analysis

1. Proteoform Information: Generates pie chart of identified proteoforms, with distinction between N-terminal truncated, C-terminal truncated, N- and C-terminal truncated and full length (=not truncated) proteoforms.  
2. Potential Cleavage: Generates heatmap showing the number of amino acids identified in X and X'-Positions of N- and C-terminal truncated subsequence proteoforms. 
3. Methionine Cleavage: Generates plots displaying the N-terminal methionine cleavage excision properties.
4. Analze Fasta
5. Export Data: Opens file dialog to select path were all results will be saved as txt-files. 
6. Specificity:
7. Show Sequence Coverage: 

### Visualization

1. Visualize Sequence Coverage: Select the protein accession of interest and "Analyze Accession" generates plots to visualize the identified peptides in respect to the full length protein.  





## Data Sets for Testing

To test the script, you can download the datasets in the Datasets folder, which contains an human fasta-file and a Dataset Demo file containing peptide identifications exported from ProSightPD results. A detailed description of the expected output results after running the script is shown in [Output](##Output). 



 ## Output 

 Settings: 

- Input fasta file "Dataset\\20210709_Uniprot_Human_reviewed.fasta" 
- Input proteoform file "DEMO_Human_GluC.txt"
- ProSightPD 
- ProSightPD v4.2

As soon as 'Initalization' is pressed, the analysis starts. The progress of the calculations is displayed in the command line. If there are peptides in the input file that cannot be assigned to an accession number, they will be reported in the command line. 

 All charts can be exported in different file formats. 



### Potential cleavage analysis of subsequence proteoforms

The tool identifies the X and X’ cleavage site of identified peptides, whereby X represents the N-terminal and X’ the C-terminal cleavage position, respectively. 

<img src="Various\Result_Heatmap.png" style="zoom:70%" alt="Result Heatmap"/>

**Figure 3**: Potential cleavage analysis plot. The heatmap shows the potential cleavage sites between two amino acids determined by the peptides, with the X site shown vertically and the X' site shown horizontally. The histograms show the total number of amino acids determined at the X' site (right) or at the X site (top). 



<img src="Various\CMD_Output.PNG" style="zoom:70%" alt="CMD Output"/>



**Figure 4:** Potential cleavage analysis command line output. The command line shows the loaded input files (fasta- and peptide txt-file), the number of considered peptides and the number of cleavage events.  



### Cleavage Specificity 

The tool determines the specificity of the middle-down peptides, depending on the selected protease. For full specific peptides, both the N- and C-termini, for semi-specific peptides either the N- or the C-termini, and for un-specific none of the termini can be explained by the protease specificty. 

<img src="Various\Result_Specificity.png" style="zoom:20%" alt="Protease Specificity" width="50%"/>

**Figure 5**: Protease Specificity. 



### Analyze Potential Cleavage Fasta File

The tool calculates all theoretical possible cleavages of all proteins in the database (that is, it basically calculates the number of all dipeptide combinations in the database). 

<img src="Various\Result_AnalyzeFastaFile.png" style="zoom:75%" alt="Result_Methionin_Cleavage"/>

**Figure 6**: Theoretical possible cleavage events in the entire fasta file. 



### N-terminal Methionine Excision

The tool identifies all peptides whose N-terminus is not truncated, or where only the start methionine is cleaved. The influence of the following amino acid and its size on methionine cleavage is analyzed. 

<img src="Various\Result_Methionin_Cleavage_relativeAndAbsolut.png" style="zoom:57%" alt="Result_Methionin_Cleavage"/>

**Figure 7**: Plots displaying the N-terminal methionine cleavage excision properties. A) bar plot showing the count of amino acids at the N-term if the start methionine is cleaved (red bars, Met cleaved) and in the position after the methionine if the start methionine is not cleaved (black bars, Met not-cleaved). B) shows the percentage of methionine cleavage before a given amino acid, with the amino acid radius shown on the x-axis.  



### Proteoform Information: C- and N-terminal peptides 

The tool identifies the number of annotated (full-length), N-terminal truncated, C-terminal truncated, and N- and C-terminal truncated proteoforms. 

<img src="Various\Result_Truncation_PieChart.png" style="zoom:70%" alt="Result_ProteoformVisualization"/>

**Figure 8**: Percentage of identified C-terminal, N-terminal, C- and N-terminal or non-truncated (full length) proteoforms displayed as a pie chart. 



### Visualization of Identified Peptides for Specific Proteins

The tool visualizes the identified peptides of a given protein accession in terms of their localization within the protein sequence and their specificity (fully specific, semispecific N-terminal, semispecific C-terminal, non-specific).  

<img src="Various\Result_SeqCovVisualization_1.png" style="zoom:75%" alt="Result_SequenceCoverageVisualization"/>

**Figure 9**: Visualization of the identified peptides compared to the full-length protein. The x-axis shows the amino acid position of the full-length protein (as deposited in the fasta file). The identified peptide are plotted as bars along the y-axis. The color of each bar represents the specificity of the identified peptide: full specific (black), only N-terminal specific (orange), only C-terminal specific (red), unspecific (blue). 


<img src="Various\Result_ProteoformVisualization_CMD.png" style="zoom:60%" alt="Result_ProteoformVisualization"/>

**Figure  10**: Visualization of the identified peptides compared to the full-length protein in the command line window. The first row shows the full-length protein  (as deposited in the fasta file) and the following rows show the identified peptides. The columns show 1) the index of teh start amino acid of the identified peptide (compared to the full-length protein), 2) the index of teh end amino acid of the peptide, 3) the peptide sequence, and 4) the number of associated PSMs. 



### Calculation of the Sequence Coverage for all Proteins within the Database

The tool assigns the identified peptides to proteins in the database (caution: this is not a sophisticated protein inference! The peptides can be assigned to multiple proteins), determines the number of assigned peptides, the sequence coverage and visualizes the position of the peptides in the protein sequence.  

<img src="Various\Result_SequenceCoverage.png" style="zoom:80%" alt="Result_ProteoformVisualization"/>

**FIgure 11**: Table Sequence Coverage. 





## Troubleshooting




## Contributions 

PTK, Python script written, basic ideas 

AT, Many ideas for data visualization 




## Changelog

- v1.0.0 (February 2023) First release (based on "Potential Cleavage Analyzer")


## References



## How to cite

 

 

## License

The tool is available under the BSD license. See the LICENSE file for more info.

 

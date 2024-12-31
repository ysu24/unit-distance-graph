# Find Unit Distance Graph with Maximum Number of Edges

### Author: Yiheng Su  
### Mentors: Adrián Csiszárik, Dániel Varga, Pál Zsámboki  

This repository explores unit distance graphs (UDG) and methods for maximizing the number of edges, using Moser lattice representations and optimization techniques like beam search. It includes theoretical discussions, implementation details, and results from computational experiments. This repository documents the research progress up to May 20, 2023. For the final stages of the study, please refer to the updated paper on [arXiv](https://arxiv.org/abs/2406.15317) published on November 25, 2024.

## 📋 Table of Contents

1. [Introduction](#-introduction)  
2. [Structure](#-structure)  
3. [Getting Started](#-getting-started)  
4. [Features](#-features)  
5. [Results](#-results)  
6. [Acknowledgments](#-acknowledgments)

---

## 🧾 Introduction

This project investigates the **unit distance graph (UDG)**—a graph in which vertices correspond to points in the plane, and edges represent unit distances between them. Key objectives include:

- Understanding theoretical properties of UDGs.  
- Representing UDGs in the Moser lattice for efficient computation.  
- Maximizing edge counts using advanced techniques like beam search.

---

## 🗂 Structure

The repository is organized as follows:

- **`udg_beam_search.ipynb`**: Main notebook containing theory, implementation, and results. 
- **`README.md`**: Documentation for the repository.

### Notebook Sections
The notebook is divided into several key sections:
1. **Unit Distance Graph (UDG)**: Definition and basic properties.  
2. **Moser Lattice Representation**: Efficient representation of UDG vertices.  
3. **Parent and Children**: Construction rules for UDGs.  
4. **Beam Search Algorithm**: Implementation for optimizing edge counts.  
5. **Results**: Analysis and visualization of findings.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- Jupyter Notebook or JupyterLab  
- Required libraries: `numpy`, `matplotlib`, `networkx`

### Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/udg-beam-search.git
   cd udg-beam-search
   ```

2.	Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.	Launch the notebook:
    ```bash
    jupyter notebook udg_beam_search.ipynb
    ```

## ✨ Features

- **Moser Lattice Representation**: Efficient integer-based representation of UDG vertices.  
- **Parent-Child Graph Construction**: Dynamic generation of UDGs using predefined rules.  
- **Beam Search Optimization**: Advanced algorithm for maximizing edge counts.  
- **Deduplication**: Ensures unique graph structures during computation.

---

## 📊 Results

The results section in the notebook highlights:  
- Insights into the maximal edge count for given vertex counts.  
- Visualization of UDGs in the Moser lattice.  
- Performance benchmarks of the beam search algorithm.

---

## 🙏 Acknowledgments

This work is guided by mentors **Adrián Csiszárik**, **Dániel Varga**, and **Pál Zsámboki**. Special thanks to contributors in the field of discrete geometry for foundational research.
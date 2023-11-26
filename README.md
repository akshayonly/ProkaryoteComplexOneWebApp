# Prokaryotic Complex I Subunits Distribution Web App

This web application is designed to explore the distribution of _Prokaryotic_ Complex I subunits. The application allows users to interactively analyze the data based on various parameters.

## Usage Instructions

1. **Under Development Status:**
   - The site is currently under development.
   - Please be aware that some features may be incomplete or subject to change.

2. **Selecting Parameters:**
   - Use the slider to choose the number of subunits (ranging from 1 to 14, with a default of 11).
   - Select the genetic material (Chromosome or Plasmid) using the radio button.
   - Choose the organism type (Bacteria or Archaea) from the dropdown menu.

3. **Minimal Information Toggle:**
   - Toggle the "Minimal Information" button to display only essential columns.
   - Essential columns include Lineage, nuoA, nuoB, nuoC, ..., nuoN.

4. **Show Table Button:**
   - Click the "Show Table" button to generate a table based on the selected parameters.

5. **Table Display:**
   - The table displays information based on the chosen subunits, genetic material, and organism.
   - If the "Minimal Information" toggle is enabled, a subset of columns is displayed; otherwise, the full dataset is shown.

## Installation

```bash
pip install streamlit pandas
```

## Running the Application

```bash
streamlit run your_app_file.py
```

Replace `your_app_file.py` with the name of your Python script containing the provided Streamlit code.

### Dependencies
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

Feel free to explore and analyze the distribution of _Prokaryotic_ Complex I subunits using this interactive web application. For updates on the development status, check the warning message on the application page.

# Import necessary libraries
import streamlit as st
import pandas as pd

# Title and warning for the under-development status
st.title('_Prokaryotic_ Complex I Subunits Distribution')
st.warning('Site Under Development', icon="⚠️")
st.divider()

# Read data from a CSV file
data = pd.read_csv(r"D:\Work\Complex-I-Spread\Webapp\data.csv")

# Slider for selecting the number of subunits
subunits = st.slider("Subunits", 1, 14, 11)

# Radio button for selecting genetic material
replicon = st.radio("Genetic Material",
                    ['Chromosome', 'Plasmid'],
                    captions=['Chromosomal DNA', 'Extrachromosomal DNA'])

# Select box for choosing organism (Bacteria or Archaea)
organism = st.selectbox('Organism', ('Bacteria', 'Archaea'))

# Toggle button for minimal information display
minimal_version = st.toggle('Minimal Table', value=True)
minimal_version_columns = ['Lineage', 'nuoA', 'nuoB', 'nuoC', 'nuoD', 'nuoE', 'nuoF', 'nuoG', 'nuoH', 'nuoI', 'nuoJ', 'nuoK', 'nuoL', 'nuoM', 'nuoN']

# Filter the data based on user selections
subset = data[(data['Replicon'] == replicon.lower()) & (data['TotalSubunits'] == subunits)]
subset = subset[subset['Organism'] == organism]
no_organisms = subset['Lineage'].nunique()

st.caption(f"{no_organisms} {organism} found with {subunits} subunits")

# Button to show the table
if st.button("Show Table"):
    # Display the table based on user preference (minimal or full version)
    if minimal_version:
        st.dataframe(subset[minimal_version_columns], hide_index=True)
    else:
        st.dataframe(subset, hide_index=True)

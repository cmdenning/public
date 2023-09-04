# references:
# [1] Size distribution of exhaled aerosol particles containing SARS-CoV-2 RNA https://www.tandfonline.com/doi/full/10.1080/23744235.2022.2140822
# [2] https://www.allfilters.com/airfilter/mervefficiency

#size of particles in microns [1]
bins = [
    (0.34, 0.55),
    (0.55, 0.94),
    (0.94, 1.7),
    (1.7, 2.8),
    (2.8, 4.5),
    (4.5, 8.0),
    (8.0, 100)
]

#number of viral copies for each size bin [1]
copies = [
    3000,
    3900,
    6000,
    4500,
    600,
    800,
    1000
]

#minimum MERV 13 efficiencies for each bin [2]
efficiencies = [
    0.5,
    0.5,
    0.85,
    0.85,
    0.9,
    0.9,
    0.9
]

#normalized copies
copies_norm = [c/sum(copies) for c in copies]

#weighted average filtration efficiency for SARS-CoV-2-containing particles
efficiency = sum([cn*e for cn, e in zip(copies_norm, efficiencies)])
print("efficiency:", efficiency)

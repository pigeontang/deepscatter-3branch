import pandas as pd
import time
import numpy as np
import simplejson as json
import sys


def convert_json_to_csv(json_loc):
    df = pd.read_json(json_loc)
    df.rename(columns={0: 'paper_id', 1: 'x', 2: 'y', 3: 'size'}, inplace=True)

    # df_2 = pd.read_csv('./80_90.csv')

    # subject = {}
    # for row in df_2.values:
    #     if row[0] not in subject:
    #         subject[row[0]] = row[4]

    # mid_field2n = {'Chemistry': 'Chemistry',
    #                'Medicine': 'Medicine',
    #                'Physics and Astronomy': 'Physics',
    #                'Materials Science': 'Physics',
    #                'Mathematics': 'Mathematics',
    #                'Arts and Humanities': 'Social Sciences',
    #                'Earth and Planetary Sciences': 'Physics',
    #                'Decision Sciences': 'Social Sciences',
    #                'Engineering': 'Engineering',
    #                'Social Sciences': 'Social Sciences',
    #                'Computer Science': 'Computer Science',
    #                'Agricultural and Biological Sciences': 'Life Sciences',
    #                'Neuroscience': 'Life Sciences',
    #                'Biochemistry, Genetics and Molecular Biology': 'Life Sciences',
    #                'Business, Management and Accounting':  'Social Sciences',
    #                'Energy': 'Physics',
    #                'Chemical Engineering': 'Chemistry',
    #                'Psychology': 'Social Sciences',
    #                'Immunology and Microbiology': 'Life Sciences',
    #                'Environmental Science': 'Physics',
    #                'Economics, Econometrics and Finance': 'Social Sciences',
    #                'Health Professions': 'Health Sciences',
    #                'Multidisciplinary': 'Multidisciplinary',
    #                'Nursing': 'Health Sciences',
    #                'Dentistry': 'Health Sciences',
    #                'veterinary': 'Health Sciences',
    #                'Pharmacology, Toxicology and Pharmaceutics': 'Life Sciences'}

    # df['subject'] = df.paper_id.apply(lambda x: subject[x] if x in subject else None)
    df.to_csv('./newest.csv', index=False)
    

if __name__ == "__main__":
    convert_json_to_csv(json_loc=sys.argv[1])

# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 10:43:14 2023

@author: Utilisateur
"""
import pandas as pd
def nettoyage_et_merge():
    bio = pd.read_csv("Agriculture_biologique_final.csv", sep ="\t", low_memory = False)
    qnutri = pd.read_csv("Qualite nutritionnelle_final.csv", sep ="\t", low_memory = False)
    ienvi = pd.read_csv("Impact environnemental_final.csv", sep ="\t", low_memory = False)
    qnutri_sansna = qnutri[qnutri['brands_tags'].notna()]
    qnutri_sansna = qnutri_sansna[qnutri_sansna['product_name'].notna()]
    qnutri_sansna_duplicate = qnutri_sansna.drop_duplicates()
    bio_sansna = bio[bio['product_name'].notna()]
    bio_sansna_duplicate = bio_sansna.drop_duplicates()
    bio_sansna_duplicate_gb = bio_sansna_duplicate.groupby(by=["product_name", "brands_tags"]).first().reset_index()
    ienvi_sansna = ienvi[ienvi['brands_tags'].notna()]
    ienvi_sansna = ienvi_sansna[ienvi_sansna['product_name'].notna()]
    ienvi_sansna_duplicate = ienvi_sansna.drop_duplicates()
    df_total = qnutri_sansna_duplicate.merge(ienvi_sansna_duplicate,on=['code'], how="inner", suffixes=('', '_DROP')).filter(regex='^(?!.*_DROP)')
    df_total = df_total.drop_duplicates()
    df_total = df_total.merge(bio_sansna_duplicate_gb, on=["product_name","brands_tags"], how="inner", suffixes=('', '_DROP')).filter(regex='^(?!.*_DROP)').drop_duplicates()
    return df_total
df_total = nettoyage_et_merge()
print(df_total)


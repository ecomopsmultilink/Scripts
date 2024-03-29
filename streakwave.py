import os
import time
import csv
import pandas as pd
from datetime import datetime
import xlsxwriter

# %%
input_file = 'export.csv'
output_file = 'output.xlsx'

# %%
df = pd.read_csv(input_file, delimiter=";")

# %%
SKUdf = df.groupby('Code')

# %%
mSKU=['CONTROLLERLVL4', 'CONTROLLERLVL5', 'CONTROLLERLVL6', 'SR-10U', 'RB924I-2ND-BT5&amp;BG77', 'RBD23UGS-5HPACD2HND-NM', 'RBWAPG-5HACD2HND-BE', 'S-4554LC80D', 'SAW30-240-1200GA', 'XS+31LC10D', 'XS+DA0003', 'RBD52G-5HACD2HND-TC-US', 'ACSMAUFL', 'HGO-ANTENNA-OUT', 'MTAO-LTE-5D-SQ', 'PL6400', 'RBLDFG-5ACD', 'RBLDFG-5ACD-US', 'CUBEG-5AC60AD', 'GESP+POE-IN', 'CSS106-1G-4P-1S', 'RBGPOE-CON-HP', 'RB912UAG-2HPND', 'RBLHG-5HPND', 'ACGPSA', 'S-85DLC05D', 'RBDYNADISHG-5HACD', 'RBDYNADISHG-5HACD-US', 'RBDYNADISHG-6HND', 'RBFTC11', 'RBLHG-2ND', 'RBLHG-5HPND-US', 'RBLHG-5HPND-XL', 'RBLHG-5HPND-XL4PACK-US', 'RBLHG5KIT', 'RBLHG5KIT-US', 'RBLHG-5ND', 'RBLHG-5ND-US', 'RBLHG-60AD', 'RBLHGG-5ACD', 'RBLHGG-5ACD-US', 'RBLHGG-60AD', 'RBLHGR', 'RBLHGR&amp;R11E-LTE', 'RBLHGR&amp;R11E-LTE6', 'ACMMCXRPSMA', 'RBLTAP-2HND&amp;R11E-LTE&amp;LR8', 'RBLTAP-2HND&amp;R11E-LTE6', 'RBOMNITIKG-5HACD', 'RBOMNITIKG-5HACD-US', 'RBOMNITIKPG-5HACD', 'RBOMNITIKPG-5HACD-US', 'RBOMNITIKU-5HND', 'RBSXTG-5HPACD-SA', 'RBSXTSQ5HPND', 'RBSXTSQ5ND', 'RBSXTSQ5ND-US', 'RBSXTSQG-5ACD', 'CRS112-8P-4S-IN', 'RBWAPG-5HACD2HND-US', 'RBWAPR-2ND&amp;R11E-4G', 'RBWAPR-2ND&amp;R11E-LR2', 'RBWAPR-2ND&amp;R11E-LTE', 'SLEEVE30', 'SOLIDMOUNT', 'TOF-2400-8V-4', 'S+85DLC03D', 'CRS328-4C-20S-4S+RM', '5VPOW', 'CCR1036-8G-2S+EM', 'CUBEG-5AC60AY', 'CUBEG-5AC60AY-SA', 'CUBEG-5AC60AY-US', 'RBSXTSQG-5ACD-US', 'CRS318-16P-2S+OUT', 'RB951UI-2ND', 'CRS310-1G-5S-4S+IN', 'CRS354-48G-4S+2Q+RM', 'CUBEG-5AC60AY-SA-US', 'ACRPSMA', 'ACUFL', 'CCR2004-1G-12S+2XS', 'CCR2004-1G-2XS-PCIE', 'CRS310-1G-5S-4S+OUT', 'CRS318-1FI-15FR-2S-OUT', 'CSS610-8G-2S+IN', 'CCR2004-16G-2S+', 'CRS312-4C+8XG-RM', 'CRS109-8G-1S-2HND-IN', 'CRS112-8G-4S-IN', 'CRS317-1G-16S+RM', 'CRS326-24G-2S+RM', 'CSS326-24G-2S+RM', 'RB941-2ND', 'RBWAPG-60AD', '48POW', 'ACOMNIRPSMA', 'ACSWI', 'XS+DA0001', 'GPER', 'S+AO0005', 'RB760IGS', '12POW150', 'RBSXTR&amp;R11E-LTE', 'RB3011UIAS-RM', 'RBMAPL-2ND', 'R11E-5HACD', 'RB750R2', 'RB911G-5HPACD-NB', 'QME', '24V2APOW', 'S-31DLC20D', 'RB750GR3', 'R11E-5HND', '18POW', '48V2A96W', 'R11E-LTE6', 'RB911G-5HPACD-US', 'R11E-LR2', 'RBWAPG-60ADKIT', 'RBWAPG-5HACD2HND', 'RBMQS', 'RBLTAP-2HND&amp;R11E-LTE', 'RBLTAP-2HND', 'CRS106-1C-5S', 'RBLHGG-60ADKIT', 'RBGROOVEA-52HPN-US', 'RBD53IG-5HACD2HND', 'RBD25G-5HPACQD2HPND', 'RBD22UGS-5HPACD2HND-15S', 'RB941-2ND-TC', 'RB931-2ND', 'RB750UPR2', 'RB2011-H', 'QM-X', 'CUBEG-5AC60ADPAIR', 'LHGGM&amp;EG18-EA', 'PW48V-12V85W', 'CRS354-48P-4S+2Q+RM', 'R11E-LORA9', 'R11E-LORA8', 'MTRADC4', 'MTRADC', 'MTP250-53V47-OD', 'MTP250-26V94-OD', 'MT-HOTSWAPFAN', 'MTAS-5G-19D120', 'MTAS-5G-15D120', 'MTAD-5G-30D3-PA', 'MTAD-5G-30D3-4STD', 'MTAD-5G-30D3-4PA', 'MTAD-5G-30D3', 'K-79', 'HGO-LTE-W', 'GPEN21', 'GPEN11', 'G1040A-60WN', 'GPER-IP67-CASE', 'LDF-2ND', 'LDF-5ND', 'LDF-5ND-US', 'OEMMMCX', 'PW48V-12V150W', 'QM', 'QMP', 'QMP-LHG', 'R11E-2HND', 'R11E-2HPND', 'R11E-4G', 'R11E-LTE', 'R52HND', 'RB2011IL-IN', 'RB2011ILS-IN', 'RB800', 'RB911G-5HPND', 'RB912R-2ND-LTM', 'RB912R-2ND-LTM&amp;R11E-LTE', 'RB921UAGS-5SHPACD-NM-US', 'RB921UAGS-5SHPACT-NM-US', 'RB922UAGS-5HPACD-NM', 'RBD52G-5HACD2HND-TC', 'RBDISC-5ND', 'RBDISC-5ND-US', 'RBDISCG-5ACD', 'RBGROOVE-52HPN', 'RBGROOVEA-52HPN', 'RBGROOVEGA-52HPACN', 'RBGROOVEGA-52HPACN-US', 'RBSXTG-5HPND-SAR2', 'RBSXTG-6HPND', 'RBSXTSQ2ND', 'RBWAPG-60AD-A', 'RBWAPR-2ND', 'RBWSAP-5HAC2ND', 'RBWSAP-5HAC2ND-US', 'S+RJ10', 'S-3553LC20D', 'S-C47DLC40D', 'S-RJ01', 'TG-BT5-IN', 'TG-BT5-OUT', 'WMK4011', 'WOOBM-USB', 'XS+2733LC15D', 'CCR1016-12G', '24V4APOW', 'CSS610-1GI-7R-2S+OUT', 'RB911-5HACD', 'RB911G-5HPND-QRT', 'CA600', 'RB911G-5HPND-QRT-US', 'RB921GS-5HPACD-15S', 'RB921GS-5HPACD-19S', 'RB921GS-5HPACD-19S-US', 'RB922UAGS-5HPACD', 'RB922UAGS-5HPACD-US', 'RBCAPGI-5ACD2ND-XL', 'RBCAPGI-5ACD2ND-XL-US', 'RBD53IG-5HACD2HND-US', 'RBDISCG-5ACD-US', 'CRS326-24S+2Q+RM', 'RB951UI-2HND', 'CWDM-CHASSIS-2', 'K-65', 'NRAYAIM-DH1', 'RB911-5HND', 'RB911-5HND-US', 'RB922UAGS-5HPACD-NM-US', 'RBD23UGS-5HPACD2HND-NM-US', 'SAW30-240-1200GR2A', 'S-C49DLC40D', 'S-C53DLC40D', 'S-C55DLC40D', 'S-C57DLC40D', 'S-C59DLC40D', 'S-C61DLC40D', 'RB4011IGS+5HACQ2HND-IN', 'RB4011IGS+5HACQ2HND-IN-US', 'RB4011IGS+RM', 'RB450GX4', 'RB911-5HACD-US', 'RB911G-2HPND-12S', 'RB912UAG-2HPND-OUT', 'RB912UAG-5HPND', 'RB912UAG-5HPND-OUT', 'RB912UAG-5HPND-OUT-US', 'RB912UAG-5HPND-US', 'RB912UAG-6HPND-OUT', 'RB952UI-5AC2ND', 'RB952UI-5AC2ND-TC', 'RB952UI-5AC2ND-TC-US', 'RB952UI-5AC2ND-US', 'RB960PGS', 'RB960PGS-PB', 'RB962UIGS-5HACT2HNT', 'RB962UIGS-5HACT2HNT-US', 'RBCAP2N', 'RBCAPGI-5ACD2ND', 'RBCAPGI-5ACD2ND-US', 'RBM11G', 'RBM33G', 'RBMAP2ND', 'RBMETALG-52SHPACN', 'RBMETALG-52SHPACN-US', 'RBOMNITIKUPA-5HND', 'RBOMNITIKUPA-5HND-US', 'RBPOE', 'RBSXTG-2HND', 'S-C51DLC40D', 'CA150', 'CA411-711', 'CA433U', 'CA493', 'CAOTS', 'CAOTU', 'CCR1016-12S-1S+', 'CCR1036-12G-4S-EM', 'CRS305-1G-4S+IN', 'CRS309-1G-8S+IN', 'CRS326-24G-2S+IN', 'CSS106-5G-1S', 'CWDM-MUX8A', 'NRAYG-60ADPAIR', 'QMP-LDF', 'R11E-5HACT', 'RB1100DX4', 'RBCAP2ND', 'RBD25G-5HPACQD2HPND-US', 'RBGROOVE52HPN-US', 'CCR2216-1G-12XS-2XQ', 'CRS504-4XQ-IN', 'CRS328-24P-4S+RM', 'CCR2116-12G-4S+', 'RB1100AHX4', 'RBGPOE', 'RB911G-5HPACD-QRT', '24HPOW', 'RB5009UG+S+IN', 'CCR2004-16G-2S+PC', 'RBWAPR-2ND&amp;R11E-LORA9', 'RBWAPR-2ND&amp;R11E-LORA8', 'RBWAPGR-5HACD2HND', 'PL7510GI', 'PL7411-2ND', 'PL7400', 'PL6411-2ND', 'LHGMOUNT', 'GESP', 'DRP-LTM', 'RB750P-PBR2', 'S-55DLC80D', 'RBD25GR-5HPACQD2HPND&amp;R11E-LTE6', 'CAP-LITE', 'RB5009UPR+S+IN', 'C52IG-5HAXD2HAXD-TC', 'C53UIG+5HPAXD2HPAXD', 'C52IG-5HAXD2HAXD-TC-US', 'C53UIG+5HPAXD2HPAXD-US', 'D53G-5HACD2HND-TC&amp;EG06-A', 'CRS305-1G-4S+OUT', 'CRS518-16XS-2XQ-RM', 'CSS610-8P-2S+IN', 'RBSXTG-5HPACD-SA-US', 'SXTR&amp;EP06-A', 'XQ+31LC02D', 'XQ+85MP01D', 'XQ+BC0003-XS+', 'XQ+DA0001', 'XQ+DA0003', '868-OMNI-ANTENNA', 'RB924IR-2ND-BT5&amp;BG77&amp;R11E-LR8', 'RB924IR-2ND-BT5&amp;BG77&amp;R11E-LR9', 'RBD53GR-5HACD2HND&amp;R11E-LTE6', 'S53UG+M-5HAXD2HAXD-TC&amp;RG502Q-EA', 'RBD53G-5HACD2HND-TC&amp;EG12-EA', 'S53UG+5HAXD2HAXD-TC&amp;EG18-EA', 'RBWAPGR-5HACD2HND&amp;R11E-LTE', 'RBWAPGR-5HACD2HND&amp;R11E-LTE6', 'CRS510-8XS-2XQ-IN', 'CRS504-4XQ-OUT', 'MT13-052400-U15BG', 'L41G-2AXD', 'MT13-052400-E15BG', 'RMK-2/10', 'XQ+31LC10D', 'CAPGI-5HAXD2HAXD-US', 'L41G-2AXD&amp;FG621-EA', 'RB5009UPR+S+OUT', 'L009UIGS-2HAXD-IN', 'L009UIGS-RM', 'CUBEG-5AC60AYPAIR-US', 'CRS310-8G+2S+IN', 'SXTR&amp;FG621-EA', 'LTAP-2HND&amp;FG621-EA', 'CME22-2N-BG77', 'R11EL-FG621-EA']
print(len(mSKU))
print(mSKU)

# %%
column_order=['SKU', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
edf = pd.DataFrame(columns=column_order)
for DF in SKUdf:
    for row in DF[1].iterrows():
        sk = row[1][0]
        if row[1][4] == "In stock":
            month_name = datetime.now().strftime('%B')
            AB = row[1][3]
        else:
            month_name = datetime.strptime(row[1][4], "%Y-%m-%d").strftime("%B")
            AB = row[1][3]
        DTA = {'SKU': sk, month_name: AB}
        edf=edf.append(DTA, ignore_index=True).fillna(0)

summed_df = edf.groupby('SKU').sum().reset_index()

# %%
# summed_df['SKU'] = summed_df['SKU'].tolist() + mSKU
new_df = pd.DataFrame({'SKU': mSKU})
result_df = new_df.combine_first(summed_df).fillna(0)
# all_zero_columns = (result_df == 0.0).all()
# columns_to_drop = all_zero_columns[all_zero_columns].index
# final_df=result_df.drop(columns=columns_to_drop)
print(result_df)

# %%
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    result_df[column_order].to_excel(writer, sheet_name='Sheet1', index=False)

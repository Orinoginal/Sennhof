# Ausfuehren im Ordner Paket_1_Finanzen (entpackt): python ../analyse/bruecke.py
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
er=pd.read_csv('Export_ERP/ER_Monat_2025-2026_final_v2.csv')
b=pd.read_csv('Export_ERP/umsatz_kd_art_20260902.csv'); st=pd.read_csv('stammdaten_art.csv')
rm=pd.read_csv('Einkauf/Preise RM 25-26.csv')
b=b.merge(st[['SKU','Standard_Materialkosten_2026_CHF_pro_kg','Kakaoanteil_an_Materialkosten_Prozent']],on='SKU')
D=['TD70','TD85','TDO']; b['dunkel']=b.SKU.isin(D)
b['sm']=b.Menge_kg*b.Standard_Materialkosten_2026_CHF_pro_kg
b['sm_b']=b.Budget_Menge_kg*b.Standard_Materialkosten_2026_CHF_pro_kg
b['sm_k']=b.sm*b.Kakaoanteil_an_Materialkosten_Prozent/100
er['dev']=er.Ist_CHF-er.Budget_CHF
M=['2026-05','2026-06','2026-07','2026-08']
dv=er[er.Periode.isin(M)].pivot_table(index='Konto',columns='Periode',values='dev')/1000
dv['Jun-Aug']=dv[M[1:]].sum(1); print(dv.round(1)); print(dv.sum().round(1))
k=rm[rm.Rohstoff.isin(['Kakaomasse','Kakaobutter'])].groupby('Periode').apply(lambda x:(x.Einkaufspreis_Ist/x.Einkaufspreis_Budget_2026).mean())
mat=er[er.Konto.str.startswith('Material')].set_index('Periode')[['Ist_CHF','Budget_CHF']].abs()
s=b.groupby('Periode')[['sm','sm_b','sm_k']].sum()
t=pd.concat([s,mat,k.rename('kidx')],axis=1).loc['2026-01':'2026-08']
t['r_bud']=t.Budget_CHF/t.sm_b
t['volmix']=t.r_bud*(t.sm-t.sm_b)
t['preis_kakao']=t.r_bud*t.sm_k*(t.kidx-1)
t['verbrauch']=t.Ist_CHF-t.Budget_CHF-t.volmix-t.preis_kakao
print(t[['kidx','r_bud']].round(4))
print((t[['Ist_CHF','Budget_CHF','volmix','preis_kakao','verbrauch']]/1000).round(1))
print('Summe Jun-Aug', (t.loc['2026-06':'2026-08',['volmix','preis_kakao','verbrauch']].sum()/1000).round(1).to_dict())
x=b[b.Periode.isin(M)].copy(); x['dev']=x.Bruttoumsatz_CHF-x.Budget_Bruttoumsatz_CHF
x['devkg']=x.Menge_kg-x.Budget_Menge_kg
print((x.groupby(['Periode','dunkel']).dev.sum()/1000).unstack().round(1))
print((x[x.dunkel].groupby(['Periode','Kunde']).devkg.sum()/1000).unstack().round(2))
y=b[(b.Periode.between('2026-01','2026-04'))&b.dunkel]
print('dunkel netto/kg', ((y.Bruttoumsatz_CHF+y.Rabatte_Boni_CHF).sum()/y.Menge_kg.sum()).round(2),'mat/kg', (y.sm.sum()/y.Menge_kg.sum()*1.0213).round(2))
fm=b[(b.Kunde=='FrischMarkt')&b.dunkel]
q=fm[fm.Periode.between('2025-09','2025-12')]
print('FM dunkel 2025 Sep-Dez: t',q.Menge_kg.sum()/1e3,'brutto',q.Bruttoumsatz_CHF.sum()/1e3,'netto',q.Nettoumsatz_CHF.sum()/1e3,'mat',q.sm.sum()*1.0213/1e3)
d25=b[(b.Periode.between('2025-09','2025-12'))&b.dunkel]; print('Dunkel 2025 Sep-Dez brutto',d25.Bruttoumsatz_CHF.sum()/1e3,'t',d25.Menge_kg.sum()/1e3)
print('Gesamt brutto 2025 Sep-Dez', b[b.Periode.between('2025-09','2025-12')].Bruttoumsatz_CHF.sum()/1e3, 't', b[b.Periode.between('2025-09','2025-12')].Menge_kg.sum()/1e3)
print('Budget brutto Sep-Dez', er[(er.Periode>='2026-09')&(er.Konto=='Bruttoumsatz Produkte')].Budget_CHF.sum()/1e3)
print('Budget mat Sep-Dez',-er[(er.Periode>='2026-09')&(er.Konto.str.startswith('Material'))].Budget_CHF.sum()/1e3)
print('Budget EBIT Sep-Dez', er[er.Periode>='2026-09'].groupby('Periode').Budget_CHF.sum().div(1e3).round(1).to_dict())

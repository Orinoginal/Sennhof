# Ausfuehren im Ordner Paket_1_Finanzen (entpackt), Ausgabe nach grafiken/
import pandas as pd, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
BLUE='#2a78d6'; ORANGE='#eb6834'; GRAY='#a3a29b'; INK='#0b0b0b'; INK2='#52514e'; SURF='#fcfcfb'; GRID='#e6e5e0'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.edgecolor':GRID,'axes.labelcolor':INK2,'xtick.color':INK2,'ytick.color':INK2,'axes.facecolor':SURF,'figure.facecolor':SURF})
def style(ax):
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.yaxis.grid(True,color=GRID,lw=0.8); ax.set_axisbelow(True); ax.tick_params(length=0)
er=pd.read_csv('Export_ERP/ER_Monat_2025-2026_final_v2.csv'); b=pd.read_csv('Export_ERP/umsatz_kd_art_20260902.csv')
mon=['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug']
# 1 Waterfall
items=[('Überstunden\nProduktion',-158.2),('Material-\nmehrverbrauch',-132.8),('Retouren\nQualität',-107.0),('Umsatz/Mix\n(v. a. Dunkel)',-67.2),('IT ERP\n(einmalig)',-48.0),('Übrige',-19.5),('Kakaopreis',11.3)]
fig,ax=plt.subplots(figsize=(11,5.2)); cum=0; x=0
for lab,v in items:
    ax.bar(x,v,bottom=cum,color=ORANGE if v<0 else BLUE,width=0.62)
    ax.text(x,cum+v-(14 if v<0 else -6),f'{v:+.0f}'.replace('-','−'),ha='center',va='top' if v<0 else 'bottom',color=INK,fontsize=11)
    cum+=v; x+=1
ax.bar(x,cum,color=INK2,width=0.62); ax.text(x,cum-14,f'{cum:.0f}'.replace('-','−'),ha='center',va='top',color=INK,fontweight='bold')
ax.set_xticks(range(len(items)+1)); ax.set_xticklabels([i[0] for i in items]+['EBIT-Abw.\nJun bis Aug'],fontsize=10)
ax.axhline(0,color=INK2,lw=1); style(ax); ax.set_ylabel('TCHF gegenüber Budget'); ax.set_ylim(-600,40)
ax.set_title('EBIT Juni bis August: 521 TCHF unter Budget, drei Viertel Qualitätskosten',loc='left',color=INK,fontsize=13,fontweight='bold')
fig.text(0.01,0.01,'Quelle: ER_Monat_2025-2026_final_v2.csv, umsatz_kd_art_20260902.csv, Preise RM 25-26.csv, stammdaten_art.csv. August vorläufig.',fontsize=8,color=INK2)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('grafiken/1_ebit_bruecke.png',dpi=160)
# 2 Retourenquote Dunkel vs übrige 2025/2026
d=b.SKU.isin(['TD70','TD85','TDO'])
def q(mask): g=b[mask].groupby('Periode'); return -g.Retouren_Gutschriften_CHF.sum()/g.Bruttoumsatz_CHF.sum()*100
qd=q(d); qr=q(~d)
fig,ax=plt.subplots(figsize=(11,4.8)); per=qd.index.tolist(); xs=range(len(per))
ax.plot(xs,qd.values,color=ORANGE,lw=2,marker='o',ms=5,label='Dunkel (TD70, TD85, TDO; Linie 2)')
ax.plot(xs,qr.reindex(per).values,color=GRAY,lw=2,marker='o',ms=5,label='übrige Produkte')
i=per.index('2026-04'); ax.axvline(i+0.2,color=INK2,ls='--',lw=1); ax.text(i+0.3,5.0,'06.04.2026\nEinbau TX-200\nauf Linie 2',fontsize=9,color=INK2,va='top')
ax.set_xlim(-0.5,len(per)+0.6); ax.set_xticks(list(xs)); ax.set_xticklabels([p[2:4]+'/'+p[5:] for p in per],fontsize=9)
ax.set_ylabel('Retouren in % vom Bruttoumsatz'); style(ax); ax.legend(frameon=False,loc='upper left')
ax.text(len(per)-1+0.35,qd.iloc[-1],f'{qd.iloc[-1]:.1f} %',ha='left',va='center',color=INK,fontsize=10); ax.text(per.index('2026-07'),qd['2026-07']+0.25,f"{qd['2026-07']:.1f} %",ha='center',color=INK,fontsize=10)
ax.set_title('Retouren steigen ab Mai 2026 nur bei Dunkelschokolade (Linie 2)',loc='left',color=INK,fontsize=13,fontweight='bold')
fig.text(0.01,0.01,'Quelle: umsatz_kd_art_20260902.csv; Linienzuordnung stammdaten_art.csv; Einbaudatum Unterhaltsprotokoll (CFO).',fontsize=8,color=INK2)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('grafiken/2_retouren_dunkel.png',dpi=160)
# 3 Material-Mehrverbrauch und Überstunden 2026 monthly (two panels, one axis each)
verb=[6.8,0.6,5.8,12.6,25.2,39.2,52.3,41.3]
ot=er[er.Konto.str.startswith('Überstunden')&(er.Periode.str[:4]=='2026')&er.Ist_CHF.notna()]
ot=ot[ot.Periode<='2026-08']; otd=(-(ot.Ist_CHF-ot.Budget_CHF)/1000).tolist()
fig,axs=plt.subplots(1,2,figsize=(11,4.4))
for ax,vals,t in [(axs[0],verb,'Material-Mehrverbrauch (TCHF)'),(axs[1],otd,'Überstunden über Budget (TCHF)')]:
    cols=[GRAY]*3+[GRAY]+[ORANGE]*4
    ax.bar(range(8),vals,color=cols,width=0.62); style(ax); ax.set_xticks(range(8)); ax.set_xticklabels(mon)
    ax.set_title(t,loc='left',color=INK,fontsize=11,fontweight='bold')
    for i,v in enumerate(vals):
        if i>=4: ax.text(i,v+1,f'{v:.0f}',ha='center',color=INK,fontsize=9)
fig.suptitle('Mehr Material und Überstunden ohne Mehrmenge, Sprung ab Mai',x=0.01,ha='left',color=INK,fontsize=13,fontweight='bold')
fig.text(0.01,0.01,'Material: Ist minus Budget, bereinigt um Menge/Mix und Kakaopreis (Standardkosten stammdaten_art.csv). Überstunden: Konto 5050. Quelle ER-Export.',fontsize=8,color=INK2)
fig.tight_layout(rect=(0,0.04,1,0.94)); fig.savefig('grafiken/3_material_ueberstunden.png',dpi=160)
# 4 Ausblick Szenarien Sep-Dez
sc=[('A Problem behoben\nab Mitte Oktober',-(166+98+60)),('B Weiter wie\nbisher',-908),('C Weiter wie bisher\n+ FrischMarkt listet\nDunkel aus (ab Okt)',-(908+806))]
fig,ax=plt.subplots(figsize=(11,4.6))
for i,(l,v) in enumerate(sc):
    ax.barh(i,v,color=[BLUE,ORANGE,ORANGE][i],height=0.55); ax.text(v-15,i,f'{v:.0f}'.replace('-','−'),va='center',ha='right',color=INK)
ax.set_yticks(range(3)); ax.set_yticklabels([s[0] for s in sc]); ax.invert_yaxis(); ax.set_xlim(-2000,0)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.xaxis.grid(True,color=GRID); ax.set_axisbelow(True); ax.tick_params(length=0); ax.set_xlabel('EBIT-Wirkung Sep bis Dez gegenüber Budget (TCHF)')
ax.set_title('Ausblick: Jeder Monat ohne Lösung kostet im Q4 rund 170 bis 270 TCHF',loc='left',color=INK,fontsize=13,fontweight='bold')
fig.text(0.01,0.01,'Annahmen: Qualitätskosten Jun bis Aug (398 TCHF) skaliert mit Budget-Materialaufwand; KT-900 CHF 60k; FrischMarkt-Deckungsbeitrag Dunkel Okt bis Dez 2025 als Basis.\nSzenarien, keine Prognose.',fontsize=8,color=INK2)
fig.tight_layout(rect=(0,0.08,1,1)); fig.savefig('grafiken/4_ausblick.png',dpi=160)

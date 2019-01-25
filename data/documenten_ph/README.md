### Documenten PH

De documenten PH bevatten informatie over de geneesmiddelen afgeleverd aan
gehospitaliseerde en ambulante patiënten verzorgd in een ziekenhuis, zowel in
een algemeen als in een psychiatrisch ziekenhuis. 
([KCE rapport](https://drive.google.com/file/d/1fMOLfP15hRktySTS8EvsaaAGnoGAUdX0/view), p. 245)

```
$ file DB_V2.TXT 
DB_V2.TXT: ISO-8859 text, with CRLF line terminators
```

```
$ wc -l DB_V2.TXT 
26009310 DB_V2.TXT
```

```
$ head DB_V2.TXT 
account_yy_ss	Province	Type	hosp_serv_id	reimbt_cat_id	drug_code	realization_date	quantity	amount_reimb	amount_not_reimb	Year
20026	Anvers	G?n?ral	990	698014	0000000	20014	1	218.1	0	2002
20026	Anvers	G?n?ral	990	698051	0000000	20014	3	5816.01	0	2002
20027	Anvers	G?n?ral	990	698051	0000000	20014	1	51.83	0	2002
20026	Anvers	G?n?ral	990	698051	0000000	20021	2	535.21	0	2002
20027	Anvers	G?n?ral	990	698051	0000000	20021	1	267.61	0	2002
20026	Anvers	G?n?ral	720	698051	0000000	20022	1	5184.17	0	2002
20027	Anvers	G?n?ral	720	698051	0000000	20022	1	5184.17	0	2002
20027	Anvers	G?n?ral	990	698051	0000000	20022	7	6789.83	0	2002
20027	Anvers	G?n?ral	990	698051	0000000	20023	4	1070.44	0	2002
```

#### Column names (from [this ppt](https://drive.google.com/file/d/1DuPcL1qC2rrbtZWH6znGiasXjsiTXwVi/view))

Year & account_yy_ss : Année et Semestre comptable

Province : Province (ou Région Bruxelles Capitale) dans laquelle se situe l’institution

Type : Type de l’institution hospitalière (hôpital général ou psychiatrique)

hosp_serv_id : Identifiant du service hospitalier (+ lien vers Table de référence)

reimbt_cat_id : Catégorie de remboursement du médicament (+ lien vers Table de référence)

drug_code : Identifiant du produit administré (+ lien vers Table de référence).

realization_date : Date d’utilisation du produit

Quantity : Nombre de fois où le produit a été administré

amount_reimb : Montant pris en charge par l’AMI

amount_not_reimb : Montant non pris en charge par l’AMI

#### More info

De l’ordre de 1,5 million d’enregistrements (=lignes)/an

16 années (2002 à 2017) : total de 24.839.535 enregistrements pour la période

Représentant une dépense pour les OA de 497.902.884,56 € en 2017
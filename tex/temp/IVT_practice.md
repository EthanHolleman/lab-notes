# IVT practice

---
title:  'This is the title'
---

## *In vitro* transcription pf pFC8 plasmid 

### Reagents

| Name | Volume (ul) | 
| ---- | ----------- |
| 5x Buffer | 4 |
| 100 mM DTT | 4 |
2.5 mM NTP | 1 |
DNA | 2.12 |
H20 | 8.88 |

DNA concentration much lower than was marked on
the tube.

### Samples

- Control: Master mix only, no transcription
- Transcribed: Master mix + T7 Polymerase + RNAaseA
- Transcribed + RNAase H: Master mix + T7 + RNAaseA Polymerase + RNAaseH

### Protocol notes

1. Measure DNA concentration using Nanodrop
2. Calculate volume of DNA sample required for ~ 200 ng per lane
3. Make master mix 
4. Aliquot 5 ul for control and remaining sample into PCR reaction
   tubes.
5. Create thermocycler reaction profile; 37 C for 20 mins then 65 C for 10 mins.
6. Add 0.5 ul T7 Polymerase to the treatment tube (15 ul master mix). Run thermocycler profile. 
7. Prepare 0.9 % agarose gel using 40 ml TBE buffer while thermocycler is running.
8. Add 0.5 ul RNAaseA to treatment tube incubate in thermocycler for
   20 mins at 37 C. 
9. Split treatment tube in half (7.5 ul remove to third PCR tube) and
    add 0.5 ml RNAaseH to the third sample. 
10. Incubate at 37 C for 20 mins.
11. Add protease K to all samples to eat junk and incubate at 37 C for 10 mins.
12. Load samples into gel using purple loading dye.
13. Run get for 1 hr at 90 volts.
14. Remove gel from tray and place into temporary container (tuperware will work) and add 1 ul of ethedium bromide and aggitate on the spinner machine by the gel imager for at least 10 minutes.
15. Image the gel and pray.

### Results

Not great lol. Somehow it looks like the DNA did not make it
onto the gel.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/ivt_4-6-2020.png)




## IVT Plasmid pFC8 T<sub>1</sub> T<sub>2</sub>

### Summary

Redoing the IVT assay with different batch of the plasmid.

### Reagents


| Name | Volume (ul) | 
| ---- | ----------- |
| 5x Buffer | 4 |
| 100 mM DTT | 4 |
2.5 mM NTP | 1 |
DNA | 4 |
H20 | 11 |

### Protocol Flow

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/IVT_4-15-21.png)

Note: When using more plasmids do not split
the RNAse + and - cases until after the polymerase
is added. Can keep these in one tube until then.

### Results

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/IVT_4-15-21_gel.png)

There is actually DNA this time but no band shifting :(
## IVT practice with pFC8 and pFC11

#### IVT pFC8

DNA concentration: 740 ng / ul

| Name       | Volume (ul) | 
| ---------- | ----------- |
| 5x Buffer  |       4     |
| 100 mM DTT |       4     |
|2.5 mM NTP  |       1     |
|   DNA      |     0.81    |
|   H20      |     10.19   |

Used **T7 Pol** but was informed by Fred that pFC8 does not actually
have a T7 promoter (oops) so this was never going to work out and is
hopefully why the other gels failed as well.

#### Gel image

No shift since not using the correct POL.

0.8 % TBE agarose ran 90v for 1 hr with 1ul 1kb Thermofisher O'Gene ruler. 

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/temp_2021-05-05_12h26m07s_ivt_pfc8.png)

### Redo pFC8T<sub>1</sub>T<sub>2</sub> with T3 Pol + pFC11 with T7 Pol

| Plasmid | DNA Concentration (ng / nl) |
| ------- | --------------------------  |
|  pFC8   |            240              |
|  pFC11  |            252              |

#### Master mix reagents

| Reagent |  pFC8T<sub>1</sub>T<sub>2</sub>  |  pFC11   |
| ---------  | ----------------------------- | -------- |
| 5x Buffer  |       4                       |    4     |
| 100 mM DTT |       4                       |    4     |
|2.5 mM NTP  |       1                       |    1     |
|   DNA      |     2.5                       |    2.38  |
|   H20      |     8.5                       |    8.61  |

#### Tube labeling

Order in gel (right to left) is the same.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/pFC8_pFC11_tubes.jpg)

| Symbol | Meaning             |
| -----  | ------------------  |
|   +    |   RNaseH containing |
|   -    | RNaseH control      |
|   c    |  Un-transcribed     |
|  `\d`  |   Plasmid number    |

#### Gel image

0.8 % TBE agarose ran 90v for 1.25 hr. 

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/2021-05-05_17h38m14s_IVT_PFC8_PFC11_label.png)

Looks like 11 was transcribed but no shift from
the control. This actually makes sense because
read through [Fred's plasmid doc](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/documents/Freds_plasmids.pdf) and found that does not actually form R-loops. On the other hand pFC8
should form R-loops.

Maybe the T3 Pol is old and not good? Test with
additional T3 plasmids and replicating pFC8.
## Debugging IVT

Yesterday used pFC11 and pFC8 for IVT experiments,
but should have realized pFC11 is not R-loop forming. However, pFC8 did not show *any* transcription. I want to both retest a R-loop forming plasmid with a T7 promoter and 2 T3 R-loop formers to see if the T3 needs to be reordered. 

The full FC plasmid table with respect to their
promoters and R-loop forming abilities is below.

| Plasmid 	| RNA Pol 	| R-loop Forming 	|
|---------	|---------	|----------------	|
| pFC1    	| NA      	| 0              	|
| pFC2    	| NA      	| 0              	|
| pFC3    	| T3      	| 1              	|
| pFC4    	| T7      	| 1              	|
| pFC5    	| NA      	| 0              	|
| pFC6    	| T3      	| 0              	|
| pFC7    	| T3      	| 0              	|
| pFC8    	| T3      	| 1              	|
| pFC9    	| T7      	| 1              	|
| pFC10   	| T3      	| 1              	|
| pFC11   	| T7      	| 0              	|
| pFC12   	| NA      	| 0              	|
| pFC13   	| NA      	| 0              	|
| pFC14   	| T3      	| 1              	|
| pFC15   	| T3      	| 1              	|
| pFC15   	| T3      	| 1              	|
| pFC16   	| NA      	| 0              	|
| pFC17   	| T3      	| 1              	|
| pFC18   	| T7      	| 0              	|
| pFC19   	| NA      	| 0              	|
| pFC20   	| T7      	| 0              	|
| pFC21   	| T7      	| 0              	|
| pFC22   	| T7      	| 0              	|
| pFC23   	| T7      	| 0              	|
| pFC24   	| T7      	| 0              	|
| pFC25   	| T7      	| 0              	|
| pFC26   	| T7      	| 0              	|
| pFC27   	| T7      	| 0              	|
| pFC28   	| T7      	| 0              	|
| pFC29   	| T3      	| 0              	|
| pFC30   	| NA      	| 0              	|
| pFC31   	| NA      	| 0              	|
| pFC32   	| T3      	| 0              	|
| pFC33   	| T7      	| 0              	|
| pFC34   	| NA      	| 0              	|
| pFC35   	| RSVLTR  	| 0              	|
| pFC36   	| RSVLTR  	| 0              	|
| pFC37   	| RSVLTR  	| 0              	|
| pFC38   	| T7      	| 0              	|
| pFC39   	| T3      	| 0              	|
| pFC40   	| RSV     	| 0              	|
| pFC41   	| T7      	| 0              	|
| pFC42   	| NA      	| 0              	|
| pFC43   	| NA      	| 0              	|
| pFC44   	| T7      	| 0              	|
| pFC45   	| T3      	| 0              	|
| pFC46   	| T3      	| 0              	|
| pFC47   	| RSV     	| 0              	|
| pFC48   	| RSV     	| 0              	|
| pFC49   	| RSV     	| 0              	|
| pFC50   	| T3      	| 0              	|
| pFC51   	| T3      	| 0              	|
| pFC52   	| T3      	| 0              	|
| pFC53   	| T3      	| 0              	|
| pFC54   	| CMV     	| 0              	|
| pFC55   	| CMV     	| 0              	|
| pFC56   	| RSV     	| 0              	|
| pFC57   	| RSV     	| 0              	|
| pFC58   	| NA      	| 0              	|
| pFC59   	| NA      	| 0              	|
| pFC60   	| NA      	| 0              	|
| pFC61   	| NA      	| 0              	|
| pFC62   	| NA      	| 0              	|
| pFC63   	| RSV     	| 0              	|
| pFC64   	| NA      	| 0              	|
| pFC65   	| NA      	| 0              	|
| pFC66   	| NA      	| 0              	|

Currently have pFC8, 11, 14, 15, 17, 32 and 44 in
the IVT box. 

Also re-read the protocol and was using too much DTT (should be 10 mM) and way too much RNaseA. Fred
says dilute 0.1mg/ml to 100x. That was probably eating up any R-loops that might have formed.

### Protocol

pFC8 DNA concentration: 240 ng / ul.
pFC14 DNA concentration: 1452 ng / ul.

|  Reagent  |     pFC8   |   pFC14    |
| --------- | ---------- | ---------  |
| 5x Buffer |     4      |    4       |
| 100 mM DTT|     2      |     2      |
| 25 mM NTP |    0.4     |     0.4    |
|    H20    |    11.1    |     13.187 |
|    DNA    |    2.5     |   0.413    |

Diluted stock RNaseA 100x and added 0.5 ul per sample. Both
samples use the T3 Pol.

Run gel for 2hr at 60v, afterwards stained with EtBr for ~15 mins
but added 8 ul instead of the usual 2 ul.

### Gel image

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/2021-05-06_18h17m00s_IVT_pFC8_pFC14.png)

#### Labeling scheme

| Symbol | Meaning             |
| -----  | ------------------  |
|   +    |   RNaseH containing |
|   -    |   RNaseH control    |
|   c    |  Un-transcribed     |
|  `\d`  |   Plasmid number    |


#### Reagent details

After talking with Fred agreed there was some shift but a lot
of noise, the source of which could be bad reagents. Checked
all reagents and multiple were expired. Also noted lot numbers,
but should order all new ones tomorrow.

| Reagent    |  Lot Number | Expiration Date |
| -------    | ----------  | --------------  |
| RNaseH     |  10016798   |     8/20        |
| DTT        |  0000264878 |    Not listed   |
| RNA Pol T3 |  10060118   |    12/21        |
| rNTP Mix   |  0291704    |    4/19         |
| 5x buffer  |  004180     |    2/21         |





## Received new IVT reagents

No experiments today, but did get new reagents and buffers.
All reagents in freezer box on my self in the kitchen -20C
freezer.

Also started a [reagents google sheet](https://docs.google.com/spreadsheets/d/1rVptZOR0hYqnl65eNiCE7tTJfLVMTTQNK7_YMsuVzHc/edit?usp=sharing) to record information when they arrive or begin use.

### IVT reagent table

| Reagent                               | Concentration | Recieved  | Lot Number | Expiration Date | Location                 | Product Details    |
| ------------------------------------- | ------------- | --------- | ---------- | --------------- | ------------------------ | ------------------ |
| T7 RNA Polymerase                     | 50000 U/ml    | 5/14/2021 | 10091329   | 11/23           | Ethan IVT Box -20 Fridge | www.neb.com/MO25S  |
| 10X T7 RNA Polymerase Reaction Buffer | NA            | 5/14/2021 | 10073286   | 7/23            | Ethan IVT Box -20 Fridge | www.neb.com/MO25S  |
| T3 RNA Polymerase                     | 50000 U/ml    | 5/14/2021 | 10085498   | 10/22           | Ethan IVT Box -20 Fridge | www.neb.com/MO378S |
| 10X T3 RNA Polymerase Reaction Buffer | NA            | 5/14/2021 | 10073286   | 7/23            | Ethan IVT Box -20 Fridge | www.neb.com/MO378S |
| RNase H                               | 5000 U/ml     | 5/14/2021 | 10081857   | 10/22           | Ethan IVT Box -20 Fridge | www.neb.com/MO297S |
| 10X RNase H Reaction Buffer           | NA            | 5/14/2021 | 10085445   | 10/23           | Ethan IVT Box -20 Fridge | www.neb.com/MO551S |
| E. coli RNA Polymerase Holoenzyme     | 1000 U/ml     | 5/14/2021 | 10088317   | 7/22            | Ethan IVT Box -20 Fridge | www.neb.com/MO551S |
| 5x E. coli Reaction Buffer            | NA            | 5/14/2021 | 10048086   | 7/22            | Ethan IVT Box -20 Fridge | www.neb.com/MO551S |
| rNTP Mix                              | 25 mM         | 5/14/2021 | 10085968   | 10/22           | Ethan IVT Box -20 Fridge | www.neb.com/MO466S |

## IVT pFC8 + pFC14 with new reagents

Doing another IVT practice with new reagents except for DTT which
is from existing IVT reagent box. Used DTT lot number `0000038464`.

### Protocol

#### DNA concentrations

| Plasmid | DNA concentration (ng/ul) |
| ------- | ------------------------- |
| pFC8    | 240                       |
| pFC14   | 1452                      |

| Reagent    | pFC8 | pFC14  |
| ---------- | ---- | ------ |
| 10x Buffer | 2    | 2      |
| 100 mM DTT | 1    | 1      |
| 25 mM NTP  | 0.4  | 0.4    |
| H20        | 14.1 | 16.187 |
| DNA        | 2.5  | 0.413  |

Same as [5-6-21](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/5-6-21.md) IVT but updated concentrations
of reagents (10x buffer and DTT) based on recommendations that
were included with the new set of reagents.

Also wanted to test the recommendation that T3 Pol should be
incubated for 1hr (is this worth it) and so did two replicates, only change was 20 mins transcription time vs 1hr.

Ran two separate gels (6 wells each) for 1.5 hr (dye getting close to end of gel) at 90V. De-stained both gels in TBE for 10 mins.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/running_gels_5-19-21.jpg)

### Results

20 mins on right, 1hr on left.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/pfc8_pfc14_ivt_5-19-21.png)

Overall, the new reagents definietly seem to help but there is lots of room for improvement. Going for the full hour for transcription seems to be definitely worth it as there is actually
a strong shift for pFC8 there. However, did not observe really any shift in the 1hr replicate for pFC14. In fact all treatments look basically identical to each other.

It is also a bit odd that all pFC14 samples after 1hr are showing signal at 2 bands, even for the un-transcribed sample. Some portion of the DNA is not carrying superhelicity before it is even transcribed.

It also might be worthwhile to add additional 0.5 ul of RNaseA as lot of signal in the transcribed samples.

I think I probably introduced some error trying to work between classes and presentations today. Going to repeat with pFC8, pFC14, and pFC11 (test the T7 polymerase) tomorrow and compare results. Overall, need to improve consistency between samples and replicates.

## IVT pFC8, pFC14, pFC17 with new reagents: attempt 2

### Protocol


#### DNA concentrations

Remeasured all DNA concentrations before starting today.

| Plasmid | DNA concentration (ng/ul) |
| ------- | ------------------------- |
|  pFC8   |           277             |
| pFC14   |           1356            |
| pFC17   |           1236            |

#### Reagents

|  Reagent  |     pFC8   |   pFC14    |  pFC17      |
| --------- | ---------- | ---------  | ----------  | 
| 10x Buffer |     2     |     2      |      2      |
| 100 mM DTT|     1      |     1      |      1      |
| 25 mM rNTP |    0.4     |     0.4    |      0.4    |
|    H20    |    14.4    |     16.15  |      16.11  |
|    DNA    |    2.16     |   0.44    |      0.48   |

Since using more plasmids this time made a master mix composed
of the constant reagents, made 1.5x more than needed. Composition
is shown in the table below.

| Reagent     |      Volume (ul)   |
| ---------   |  ---------------   |
| 10x buffer  |         9          |
|     DTT     |         4.5        |
|    rNTP     |         1.8        |

Added 3.4 ul MM to each sample plus H20 and DNA specific to
each plasmid.

All plasmids use the T3 polymerase.

### Results

Ran 0.8% agarose gel for 1 hour 45 mins.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/IVT_pfc8_pcf14_pfc17_5-20-21.png)


## Transcription time vs DNA concentration optimization

After lab meeting last Friday Fred suggested experimenting
with different DNA concentrations and transcription times
in order to optimize IVT.

Designed protocol which is layed out in 
[spreadsheet form at this link](https://docs.google.com/spreadsheets/d/15oUK6Z6GfXZMH4Q9PZiSx24dGQXJuvFM7fCIeLSdvrQ/edit?usp=sharing).

I choose to use pFC14 as it wasn't as clean as pFC8 but showed
R-loop formation and so there would be lots of room to
optimize using it.

### Protocol

See [spreadsheet form at this link](https://docs.google.com/spreadsheets/d/15oUK6Z6GfXZMH4Q9PZiSx24dGQXJuvFM7fCIeLSdvrQ/edit?usp=sharing) for details of reagents and concentrations.

1. Make buffer master mix (Txn buffer, rNTP, DTT)
2. Make DNA master mix for each DNA concentration
3. Split DNA master mixes into transcription and control samples for each transcription length.

![All samples](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/IVT_Time_vs._DNA_mass_samples.jpg)

This is where I differed from what I intended to do. Originally I planned to add the T3 just before adding the sample to the thermocycler for incubation. In this system 45 min samples would go in first, then after 15 mins T3 would be added to 30 min sample, etc. until all samples have incubated for repsective lengths. Then all samples run at 65C for 10 mins to kill transcription. This has the benefit of all samples finishing at the same time.

However, I accidentally added T3 to *all* transcribed samples at the same time. So at that point it was game on, transcription was underway and so I basically had to do the above in reverse. All samples went into block B of the thermocycler at 37C. After 15 mins I removed the 15 min sample and incubated in block A at 65, after another 5 I removed the 20 min sample etc. until I finished all samples. Samples were kept on ice while waiting for other samples to finish which may have introduced some error since the sample sat after killing transcription for different amounts of time.

4. Add 1 ul 1:100 RNaseA
5. Incubate all samples 37C for 30 mins.
6. Add 0.25 ul Protease K to all samples.
7. Incubate at 37C for 10 mins.
8. Load samples onto 1% agarose gel (I used higher percentage this time as was using the big gel and was slightly worried about integrity of the gel)
9. Run samples at 90V for 1.75 hours.
10. Post-stain gel with 10ul EtBr for 15 mins.
11. Destain get for 10 mins.
12. Image gel.

#### Gel lane layout

Lane layout with respect to transcription time and DNA
concentration available at 
[this link](https://docs.google.com/spreadsheets/d/15oUK6Z6GfXZMH4Q9PZiSx24dGQXJuvFM7fCIeLSdvrQ/edit#gid=929396717) or image below.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/well_layout_5-25-21.png)

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/big_gel_box.jpg)

### Results

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/IVT_txn_time_vs_DNA_con_pFC14_5-25-21.png)

Results are not as clean as I was hoping for. Looks like
I did not add RNaseA in a couple cases (not sure how that
happened and can be seen as the bright lanes).

If I had to pick a best condition I would saw 100 ng
of DNA at 15 - 20 mins transcription time. 
## Transcription time vs DNA concentration optimization with pFC17



This is a replication of 
[Transcription time vs DNA concentration optimization with pFC17](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/5-25-21.md) with pFC17 instead of 14.

### Protocol

| plasmid |  DNA ng / ul |
| ----    | ---------    |
|  pFC17  |   1236       |

Main difference in protocol was I corrected the order in which
samples were places into the thermocycler. 45 min samples + T3
went in first and then at each time mark (30, 20 and 15 minutes)
the protocol was paused and T3 was added to the respective sample
and then added to the thermocycler. This removed wait time for
short run samples post transcription.

### Results

#### Sample switch mistake

When loading the samples into the gel I switched the locations
of the 100 ng and 150 ng 45 minute samples. This will not affect
results but will require some cropping in order to get everything
in the correct order.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/2021-05-27_15h13m50s_txn_time_DNa_con_pFC17.png)
## Test for DNase activity in RNaseA

In the last two time resolved gels saw decrease in DNA
signal as transcription time increased. There were
no samples treated with RNAseH, but all samples were
treated with RNAseA which is lab made. Normally, it is well
boiled to destroy other less hardy proteins but it is
possible that some DNase was retained. 

To test this today doing a time resolved digestion of pFC14 and
17 with high or low concentrations of the RNaseA I used in the
previous two IVTs (see [5-27-21](5-27-21.md) and [5-25-21](5-25-21.md)).

### Protocol

[Google sheet for master mix calculator](https://docs.google.com/spreadsheets/d/19SzEC0GCZEz3y9boZorlRqx0nOqL56obEHCXnjmxrOM/edit?usp=sharing).

Created master mixes of pFC14 and 17 as described in the above
sheet. Each master mix was divided into samples of 4 increasing
digestion times; 15, 30, 45 and 60 mins.

Within each digestion time for each plasmid either 0, 1 or 4 ul
of 1:100 dilution 1mg / ml RNaseH was added just before incubation.

Thermocycler was set to 37C for 60 mins and samples were added
at their respective time point immediately after adding the 
RNaseA. The only exception was the 15 min and 60 minute samples; 60 min samples added at 15 minute mark and 15 minute samples added at 60 min mark. No effect on experimental results after swapping those samples since reagent concentrations are identical.

Samples were kept on ice while they waiting for their turn in
the thermocycler.

While loading samples into 20 well rack noticed that there
seemed to be significant leaking from first well loaded. After 1
min saturation of dye was nearly gone in the loaded well and well
next to it had taken on some purple color. Skipped the next well
kept loading and noticed what I think was overflow while loading.
Seems like the 20 rack wells are too small for sample volumes.
Unfortunately, because of this lost the 15 min samples. Put the rest on ice and made two gels with 6 rack well size using. Kept samples cold in deli fridge while waiting for gels to harden.

### Results

Samples loaded into 0.8% agarose gel with 1x TAE running buffer and 6x purple loading dye. Post-stained with 12 ul EtBr for 20
mins on rotator protected from light.

| Symbol |  Meaning |
| ----   |  ------  |
|   L    |    1 ul RnaseA  |
|   H    |   4 ul RNaseA   |
|   C    |   Control no RnaseA  |

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/2021-06-01_13h27m23s_pfc14_17_RNaseA_time_resolved_labeled.png)

Although signal is definetely weak in the pFC14 samples
(not sure why times are making a difference here though) all
samples seem to be showing about the same signal which would
*not* indicate the presence of a DNase in the RNaseA sample.
60 min samples both seem to be stronger though, maybe when
I was setting up the samples I pulled from the master mix that
had too much DNA. I think it would probably be best just to replicate this one again. If it is not a case of RNAseA being contaminated then I am not
sure what would explain the differences in DNA signal between transcription times besides just pipetting error on my part; possibly due to not adding exact same amounts of sample to each well when mixing on the parafilm. 

## Test for possible nuclease activity in RNAse A enzyme stock

Follow up to [6-1-21](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/6-1-21.md) test using plasmids pFC11 and pFC44. Also
noted that running pretty low on stock of pFC14 and 17. Need to make
more soon.

### Protocol

Plasmid concentrations table.

| Plasmid |  DNA Concentration (ng / ul) |
| ------- |   -------------------------- |
| pFC11   |             1080             |
| pFC44   |             1165             |

DNA master mix recipe.

|  Plasmid |     H20 (ul)   |    DNA (ul)    |    Total Volume (ul)  |
| -----    |  ---------     | -------------- |  -------------------- |
| pFC11    |    88.34       |      1.66      |           90          |
| pFC44    |    88.46       |      1.54      |           90          |

Stock RNase A (1mg/ml) was diluted 1:100.

Master mixes described above were prepared and then separated into 8
aliquots per sample. 8 samples were divided into 4 increasingly
long durations of incubation at 37C for 15, 30, 60 and 120 minutes.
Samples were added to the thermocycler in reverse order by duration
of incubation (120 mins first) and 4 ul of RNAse A was addded to treated
samples while 4 ul npH20 was added to controls immediatly before placing
samples into the thermocycler. 

After all samples completed incubation I had to give a presentation in
one of my classes and so there was a delay of about 1hr between the last
sample finishing incubation and actually running samples on agarose
gel.

Samples ran on 0.7% agarose gel for 45 mins at 90 V in TAE with 12 ul
of EtBr in both agarose mix and running buffer.

### Results

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/RNaseA_test_pFC11_pFC44_15-120_mins_labeled.png)

Some time dependent effect is occurring but it is observable after
15 mins and then samples look very similar. The weird part is that
control samples are also being effected. This is indicating some
other DNA degradation process is occurring that is independent of
RNaseA activity and it is mainly observed after only 15 mins. 

WTF. Fred offered DNA eating tubes as possible explanation. Everyone
agreed this was probably unlikely but worth testing. Other possibilities
could be effects of H20 (high acidity of npH20) so also will test effects
of using DNase free H20.
## RNAse mediated DNA degradation; or something more sinister?

As a follow up to the confusing results of [6-3-21](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/6-3-21.md) I am testing to see if other factors outside
of RNAse A might be degrading DNA during IVT / related
experiments that utilize RNase A lab stock. Two main variables are the tubes and water used. Both where proposed as potential sources of DNA consumption / degradation respectively.

Types of tubes tested shown below, previously I have
been using snap tops for all experiments that needed
PCR tubes.

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/snap_top_vs_strip_top_tubes.png)

### Protocol



### Results

![](/home/ethan/Documents/github/lab-notes/experiments/IVT_practice/images/RNaseA_test_pFC11_change_tubes_h20_15-30min_treatment_labeled.png)



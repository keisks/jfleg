# JFLEG (JHU FLuency-Extended GUG) corpus

Last updated: December 7th, 2018

(Make sure to download and use the latest version.)

[link to the paper](http://aclweb.org/anthology/E17-2037)

- - -

## Data

    .
    ├── EACL_exp      # experiments in the EACL paper
    │   ├── m2converter # script to create m2 format from plain texts
    │   ├── mturk     # mechanical turk experiments
    │   │   ├── sample.csv
    │   │   ├── pairwise.csv
    │   │   └── template.html
    │   └── manual_eval # manual analysis of 100 sentences
    │       ├── README.md
    │       └── coded_sentences.csv
    ├── README.md     # This file
    ├── EACLshort037.pdf
    ├── dev           # dev set (754 sentences originally from the GUG **test** set)
    │   ├── dev.ref0
    │   ├── dev.ref1
    │   ├── dev.ref2
    │   ├── dev.ref3
    │   ├── dev.spellchecked.src (spellchecked by enchant)
    │   └── dev.src   # source (This should be the input for your system.)
    ├── eval
    │   └── gleu.py   # evaluation script (sentence-level GLEU score)
    └── test          # test set (747 sentenses ogirinally from the GUG **dev** set)
        ├── test.ref0
        ├── test.ref1
        ├── test.ref2
        ├── test.ref3
        ├── test.spellchecked.src (spellchecked by enchant)
        └── test.src   # source (This should be the input for your system.)


## Evaluation

    e.g. python ./eval/gleu.py -r ./dev/dev.ref[0-3] -s ./dev/dev.src --hyp YOUR_SYSTEM_OUTPUT

    This returns the mean, standard deviation, and confidence interval.

## Leader Board (published results)

N.B. Sytems with asterisk (*) are tuned on different data. 

System                     | GLEU (dev) | GLEU (test)
---------------------------------------- | :--------: | :---------:
[Coyne et al. (2023)](https://arxiv.org/abs/2303.14342) | 60.10* | 65.02
[Ge et al. (2018)](https://arxiv.org/pdf/1807.01270.pdf)         |  N/A | 62.42
[Liu et al. (2021)](https://github.com/thunlp/VERNet)         |  N/A | 61.61
[Grundkiewicz and Junczys-Dowmunt (2018)](https://arxiv.org/pdf/1804.05945.pdf)         |  N/A | 61.50
[Junczys-Dowmunt et al. (2018)](https://arxiv.org/pdf/1804.05940.pdf)         |  N/A | 59.90
[Chollampatt and Ng (2018)](https://arxiv.org/pdf/1801.08831.pdf)         |  52.48 | 57.47
[Chollampatt and Ng (2017)](http://www.aclweb.org/anthology/W17-5037)         |  51.01 | 56.78
[Xie et al. (2018)*](http://www.aclweb.org/anthology/N18-1057)         |  N/A | 56.20
[Sakaguchi et al. (2017)](https://arxiv.org/pdf/1707.00299.pdf)         |  49.82 | 53.98
[Ji et al. (2017)*](http://aclweb.org/anthology/P/P17/P17-1070.pdf)      |  48.93 | 53.41
[Yuan and Briscoe (2016)* ](http://www.aclweb.org/anthology/N16-1042)   |  47.20 | 52.05 
[Junczys-Dowmunt and Grundkiewicz (2016) ](https://www.aclweb.org/anthology/D/D16/D16-1161.pdf) |  49.74 | 51.46
[Chollampatt et al. (2016)* ](https://aclweb.org/anthology/D/D16/D16-1195.pdf) |  46.27     | 50.13
[Felice et al. (2014)* ](http://www.aclweb.org/anthology/W14-1702)      |  42.81 | 46.04
=================================== | ========== | ==========
SOURCE    |  38.21 | 40.54
REFERENCE |  55.26 | 62.37

- If you want to add your score, please send an e-mail to keisukes[at]allenai.org a link to your paper and system outputs.
- The reference scores are computed by averaging each reference.


## Reference
The following paper should be cited in any publications that use this dataset:

Courtney Napoles, Keisuke Sakaguchi and Joel Tetreault. (EACL 2017): JFLEG: A Fluency Corpus and Benchmark for Grammatical Error Correction. In Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics. Valencia, Spain. April 03-07, 2017.

Michael Heilman, Aoife Cahill, Nitin Madnani, Melissa Lopez, Matthew Mulholland, and Joel Tetreault. (ACL 2014): Predicting Grammaticality on an Ordinal Scale. In Proceedings of the Association for Computational Linguistics. Baltimore, MD, USA. June 23-25, 2014.

bibtex information:

    @InProceedings{napoles-sakaguchi-tetreault:2017:EACLshort,
      author    = {Napoles, Courtney  and  Sakaguchi, Keisuke  and  Tetreault, Joel},
      title     = {JFLEG: A Fluency Corpus and Benchmark for Grammatical Error Correction},
      booktitle = {Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers},
      month     = {April},
      year      = {2017},
      address   = {Valencia, Spain},
      publisher = {Association for Computational Linguistics},
      pages     = {229--234},
      url       = {http://www.aclweb.org/anthology/E17-2037}
    }

    @InProceedings{heilman-EtAl:2014:P14-2,
      author    = {Heilman, Michael  and  Cahill, Aoife  and  Madnani, Nitin  and  Lopez, Melissa  and  Mulholland, Matthew  and  Tetreault, Joel},
      title     = {Predicting Grammaticality on an Ordinal Scale},
      booktitle = {Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
      month     = {June},
      year      = {2014},
      address   = {Baltimore, Maryland},
      publisher = {Association for Computational Linguistics},
      pages     = {174--180},
      url       = {http://www.aclweb.org/anthology/P14-2029}
    }





## Questions

 - Please e-mail Courtney Napoles (napoles[at]cs.jhu.edu) and Keisuke Sakaguchi (keisuke[at]cs.jhu.edu).


## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

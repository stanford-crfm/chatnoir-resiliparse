from resiliparse.parse import lang

# Source: Wikipedia front page articles of the day
SAMPLES = dict(
    en="""Raymond Pace Alexander (1897–1974) was a civil rights leader, lawyer, and politician who was the first
    African-American judge appointed to the Pennsylvania courts of common pleas. In 1920, he became the first black
    graduate of the Wharton School of Business. He married in 1923 and in 1927 his wife, Sadie, became the first black
    woman to earn a law degree from the University of Pennsylvania. After graduating from Harvard Law School in 1923,
    Alexander became one of the leading civil rights attorneys in Philadelphia.""",
    ml="""കോവിഡ്-19 നിർണ്ണയം, രോഗബാധ തടയൽ, ചികിത്സ എന്നിവ സംബന്ധിച്ച നിരവധി വ്യാജവും തെളിയിക്കപ്പെടാത്തതുമായ മെഡിക്കൽ
    ഉൽപ്പന്നങ്ങളും രീതികളും നിലവിലുണ്ട്. കോവിഡ്-19 ഭേദപ്പെടുത്താം എന്ന അവകാശവാദത്തോടെ വിൽക്കുന്ന വ്യാജ മരുന്നുകളിൽ
    അവകാശപ്പെടുന്ന ഘടകങ്ങൾ ഉണ്ടാവണമെന്നില്ല. മാത്രമല്ല, അവയിൽ ദോഷകരമായ ചേരുവകൾ ഉണ്ടായേക്കുകയും ചെയ്യാം. വാക്‌സിനുകൾ
    വികസിപ്പിക്കുന്നതിന് ലോകമെമ്പാടും ശ്രമങ്ങൾ നടക്കുന്നുണ്ട്. ലോകാരോഗ്യസംഘടനയുടെ നേതൃത്വത്തിലുള്ള സോളിഡാരിറ്റി ട്രയൽ ഉൾപ്പെടെ
    പല രാജ്യങ്ങളിലും ഗവേഷണം നടക്കുന്നുണ്ടെങ്കിലും 2020 മാർച്ച് വരെ ലോകാരോഗ്യ സംഘടന കോവിഡ്-19 ചികിത്സിക്കുന്നതിനോ
    ചികിത്സിക്കുന്നതിനോ മരുന്നുകളൊന്നും ശുപാർശ ചെയ്യുന്നില്ല.""",
    ta="""எமிலி டிக்கின்சன் (1830 – 1886) ஒரு அமெரிக்கப் பெண் கவிஞர் ஆவார். ஆங்கிலக் கவிதையுலகின் குறிப்பிடத்தக்க
    படைப்பாளிகளுள் ஒருவராகக் கருதப்படுபவர். ஐக்கிய அமெரிக்காவின் மாசசூசெட்ஸ் மாநிலத்தைச் சேர்ந்த இவர் தனிமையைப் பெரிதும்
    விரும்பியவர். வெள்ளை நிற ஆடைகளை மட்டும் அணிதல், விருந்தினருடன் பேசுவதில் தயக்கம் காட்டுதல், அறையை விட்டு வெளியே
    வராதிருத்தல் போன்ற பழக்க வழக்கங்களால் விந்தையான பெண்ணாக அறியப்பட்டார்.""",
    pt="""Music é o oitavo álbum de estúdio da cantora americana Madonna. O seu lançamento ocorreu em 18 de setembro
    de 2000, através das gravadoras Maverick e Warner Bros.. Em setembro de 1999, Madonna iniciaria uma turnê para
    promover seu Ray of Light, mas teve que adiar devido ao atraso das filmagens de The Next Best Thing (1999). Pouco
    depois de lançar "Beautiful Stranger" para a trilha sonora do filme Austin Powers: The Spy Who Shagged Me, ela
    iniciou um relacionamento com o diretor britânico Guy Ritchie.""",
    fr="""La Sarcelle d'hiver (Anas crecca) est la plus petite espèce de canards de surface. Elle se rencontre en
    Europe, Amérique du Nord et aussi en Asie. Dans ces régions, elle vit dans les zones tempérées à septentrionales.
    C'est un migrateur partiel, elle est chassée en grand nombre en Europe et en Amérique du Nord. La population
    nord-américaine est considérée par certains ornithologues comme une espèce à part, la Sarcelle à ailes vertes, et
    par d'autres comme une sous-espèce.""",
    nl="""Zoogdieren (Mammalia) vormen een klasse van warmbloedige, meestal levendbarende gewervelde dieren die hun
    jongen zogen: de moederdieren produceren melk en voeden hiermee hun jongen. Zoogdieren kenmerken zich door hun
    beschermende beharing, hun goed ontwikkelde hersenen en de specifieke bouw van hun schedel.""",
    es="""RoboCop es una película de acción y ciencia ficción estadounidense dirigida por Paul Verhoeven y escrita por
    Edward Neumeier y Michael Miner. Está protagonizada por Peter Weller, Nancy Allen, Dan O'Herlihy, Ronny Cox,
    Kurtwood Smith y Miguel Ferrer. La trama se centra en el oficial de policía Alex Murphy (Weller), quien es
    asesinado por una banda de criminales y posteriormente revivido por la corporación Omni Consumer Products como un
    cíborg policía llamado RoboCop.""",
    el="""Η μάχη του Μελιγαλά έλαβε χώρα στο Μελιγαλά της Μεσσηνίας από τις 13 ως και τις 15 Σεπτεμβρίου του 1944
    ανάμεσα στον ΕΛΑΣ, αντιστασιακό στρατό του ΕΑΜ και τα δωσιλογικά Τάγματα Ασφαλείας. Ανταρτοομάδες του ΕΑΜ/ΕΛΑΣ
    δρούσαν στην κατεχόμενη Πελοπόννησο από το 1942 και το 1943 ξεκίνησαν να εδραιώνουν την κυριαρχία τους στην περιοχή.
    Για την αντιμετώπισή τους οι γερμανικές αρχές οργάνωσαν τα ΤΑ, ένα από τα οποία είχε έδρα το Μελιγαλά και τα οποία
    συμμετείχαν σε αντιανταρτικές επιχειρήσεις και μαζικά αντίποινα εναντίον του συμπαθούντος πληθυσμού. """,
    ru="""Мятеж сыновей Генриха II — восстание англо-нормандской знати против английского короля Генриха II
    Плантагенета в 1173—1174 годах, которое возглавили трое его сыновей и жена, Алиенора Аквитанская. Основной причиной
    недовольства сыновей Генриха II было то, что хотя король наделил сыновей титулами (старший — Генрих Молодой Король
    — был коронован как соправитель отца, а двое следующих, Ричард и Джеффри, получили титулы герцогов Аквитании и
    Бретани соответственно), эти титулы были лишь символическими, он намеревался продолжать лично управлять своими
    владениями и делиться властью с сыновьями не желал.""",
    dk="""The Corrs er et irsk folkrockband, der kombinerer poprock med traditionel keltisk musik. Bandet består af
    fire søskende Andrea (forsanger, tinwhistle), Sharon (violin, baggrundsvokal), Caroline (trommer, klaver, bodhrán,
    baggrundsvokal) og Jim Corr (guitar, klaver, baggrundsvokal). De stammer fra Dundalk, County Louth i Irland.
    The Corrs har udgivet seks studiealbums og adskillige singler, som har nået platincertificering i flere lande.""",
    it="""Alcibiade, figlio di Clinia del demo di Scambonide (in greco antico: Ἀλκιβιάδης, Alkibiádēs; Atene, 450 a
    C. – Frigia, 404 a.C.), è stato un militare e politico ateniese. Oratore e statista di altissimo livello, fu
    l'ultimo membro di spicco degli Alcmeonidi, il clan aristocratico a cui apparteneva la famiglia di sua madre, poi
    decaduto con la fine della guerra del Peloponneso. Svolse un ruolo importante nella seconda parte di questo
    conflitto, come consigliere strategico, comandante militare e politico.""",
    tr="""Panayia Kilisesi, Panaya Kilisesi, Panagia Kilisesi (Yunanca: Εκκλησία Της Παναγίας) ya da Koimesis Theotokou
    Kilisesi (Yunanca: Εκκλησία της Κοιμήσεως της Θεοτόκου); Türkiye'nin Balıkesir ilindeki Ayvalık'a bağlı Cunda'da,
    harabe hâlindeki bulunan eski bir Rum Ortodoks kilisedir.""",
    sv="""Sveriges utrikes- och säkerhetspolitik under kalla kriget utformades efter andra världskrigets slut med
    hänsyn till landets geografiska position mellan de två militärallianserna Nato och Warszawapakten; perioden täcker
    åren från 1945 till 1989. Vid en eventuell stormaktskonflikt ville landet, genom att vara alliansfri i fredstid vid
    en eventuell stormaktskonflikt ha möjlighet att vara neutralt. Genom olika politiska åtgärder ville man också göra
    en sådan neutralitetspolitik trovärdig.""",
    ar="""عِلْم الكِيِمْيَاء هو العلم الذي يدرس المادة والتغيُّرات التي تطرأ عليها، تحديدًا بدراسة خواصها، 
    بنيتها، تركيبها، سلوكها، تفاعلاتها وما تحدثه من خلالها. ويدرس علم الكيمياء الذرات والروابط التي تحدث بينها مكونةً
    الجزيئات، وكيف تترابط هذه الجزيئات فيما بعدها لتُكوّن المادة. ويدرس أيضًا التفاعلات التي تحدث بينها. وللكيمياء
    أهمية كبيرة في حياة البشر وتدخل في مجالات كثيرة وتلعب دورًا مهمًا في الصناعات بمختلف أنواعها، كالصِّناعاتالغذائية،
    صناعة المواد التنظيفية، الدهانات، الأصبغة، صناعة الأدوية والعقاقير، النسيج والملابس والأسلحة وغيرها.""",
    de="""Die heilige Ludmilla von Böhmen (auch Lidmilla, tschechisch Svatá Ludmila, selten Lidmila, * zwischen 855 und
    860; † 15. September 921 in Tetín) war eine böhmische Fürstin. Sie war die erste christliche Herrscherin und ist
    die erste Heilige des Landes. Während ihrer Lebenszeit wurde der Grundstein für die Christianisierung gelegt und
    die Machtbasis der Přemyslidendynastie geschaffen. Das Leben der Großmutter und Erzieherin des heiligen Wenzel wurde
    in vielen Legenden beschrieben, die grundlegende Quellen zur Geschichte Böhmens im 9. und 10. Jahrhundert sind.""",
    kn="""ಕನ್ನಡ ಅಕ್ಷರಮಾಲೆಯು ಬ್ರಾಹ್ಮಿ ಲಿಪಿಯಿಂದ ಬೆಳೆದು ಬಂದಿದೆ. ಇದನ್ನು ಸ್ವರಗಳು, ಅನುಸ್ವಾರ, ವಿಸರ್ಗ, ವ್ಯಂಜನಗಳು, ಅವರ್ಗೀಯ ವ್ಯಂಜನಗಳೆಂದು
    ವಿಭಾಗಿಸಲಾಗಿದೆ. ಕನ್ನಡ ಅಕ್ಷರಮಾಲೆಯನ್ನು ಕನ್ನಡ ವರ್ಣಮಾಲೆಯೆಂದು ಕರೆಯಲಾಗುತ್ತದೆ. ನಾವು ಮಾತನಾಡುವ ಮಾತುಗಳೆಲ್ಲ ವಾಕ್ಯ ವಾಕ್ಯಗಳಾಗಿರುತ್ತವೆ. ವಾಕ್ಯಗಳು
    ಪದಗಳಿಂದ ಕೂಡಿರುತ್ತವೆ. ಪದಗಳು ಅಕ್ಷರಗಳಿಂದ ಕೂಡಿರುತ್ತವೆ. ಉದಾಹರಣೆಗೆ, ನಾನು ಶಾಲೆಗೆ ಹೋಗಿ ಬರುವೆನು. ಈ ವಾಕ್ಯದಲ್ಲಿ ನಾನು, ಶಾಲೆಗೆ, ಹೋಗಿ,
    ಬರುವೆನು, ಹೀಗೆ ನಾಲ್ಕು ಪದಗಳಿವೆ. ಒಂದೊಂದು ಪದದಲ್ಲೂ ಹಲವು ಅಕ್ಷರಗಳಿವೆ."""
)


def test_lang_detect_fast():
    assert lang.detect_fast('This is an average English text...')[0] == 'en'
    assert lang.detect_fast('...aber fügen wir doch etwas auf Deutsch hinzu.')[0] == 'de'

    for l in SAMPLES:
        assert lang.detect_fast(SAMPLES[l])[0] == l


def test_lang_detect_fast_train_examples():
    trained_vecs = []
    vec_lens = [150, 200]
    for vl in vec_lens:
        for l in SAMPLES:
            vec = lang._train_language_examples([SAMPLES[l]], vl)
            assert len(vec) == vl
            assert vec != [0] * vl
            for pv in trained_vecs:
                assert vec != pv
            trained_vecs.append(vec)

            vec_str = lang._train_language_examples_c_decl(l, [SAMPLES[l]], vl)
            assert f'{{"{l}", {{{", ".join(str(i) for i in vec)}}}}};' in vec_str

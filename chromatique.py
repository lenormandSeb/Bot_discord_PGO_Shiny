class Chromatique():
    def __init__(self):
        self.gen1 = [
            {'name': 'Bulbizarre','numero': '001'},
            {'name': 'Herbizarre','numero': '002'},
            {'name': 'Florizarre','numero': '003'},
            {'name': 'Salameche', 'numero': '004'},
            {'name': 'Reptincel', 'numero': '005'},
            {'name': 'Dracaufeu', 'numero': '006'},
            {'name': 'Carapuce', 'numero': '007'},
            {'name': 'Carabaffe', 'numero': '008'},
            {'name': 'Tortank', 'numero': '009'},
            {'name': 'Chenipan', 'numero': '010'},
            {'name': 'Chrysacier', 'numero': '011'},
            {'name': 'Papilusion', 'numero': '012'},
            {'name': 'Roucool', 'numero': '016'},
            {'name': 'Roucoups', 'numero': '017'},
            {'name': 'Roucarnarge', 'numero': '018'},
            {'name': 'Rattata', 'numero': '019'},
            {'name': 'Rattatac', 'numero': '020'},
            {'name': 'Pikachu', 'numero': '025'},
            {'name': 'Raichu', 'numero': '026'},
            {'name': 'Sabelette', 'numero': '027'},
            {'name': 'Sablaireau', 'numero': '028'},
            {'name': 'NidoranF', 'numero': '029'},
            {'name': 'Nidorina', 'numero': '030'},
            {'name': 'Nidoqueen', 'numero': '031'},
            {'name': 'Rondoudou', 'numero': '039'},
            {'name': 'Grodoudou', 'numero': '040'},
            {'name': 'Taupiqueur', 'numero': '050'},
            {'name': 'Triopikeur', 'numero': '051'},
            {'name': 'Psykokwak', 'numero': '054'},
            {'name': 'Akwakwak', 'numero': '055'},
            {'name': 'Ferosinge', 'numero': '056'},
            {'name': 'Colosinge', 'numero': '057'},
            {'name': 'Caninos', 'numero': '058'},
            {'name': 'Arcanin', 'numero': '059'},
            {'name': 'Machoc', 'numero': '066'},
            {'name': 'Machopeur', 'numero': '067'},
            {'name': 'Mackogneur', 'numero': '068'},
            {'name': 'Racaillou', 'numero': '074'},
            {'name': 'Gravalanch', 'numero': '075'},
            {'name': 'Grolem', 'numero': '076'},
            {'name': 'Ponyta', 'numero': '077'},
            {'name': 'Galopa', 'numero': '078'},
            {'name': 'Magneti', 'numero': '081'},
            {'name': 'Magneton', 'numero': '082'},
            {"name": 'Tadmorv',"numero": '088'},
            {'name': 'Grotadmorv','numero': '089'},
            {'name': 'Kokiyas','numero': '090'},
            {'name': 'Crustabri', 'numero': '091'},
            {'name': 'Fantominus', 'numero': '092'},
            {'name': 'Spectrum', 'numero': '093'},
            {'name': 'Ectoplasma', 'numero': '094'},
            {'name': 'Soporifik', 'numero': '096'},
            {'name': 'Hypnomade', 'numero': '097'},
            {'name': 'Osselait', 'numero': '104'},
            {'name': 'Ossatueur', 'numero': '105'},
            {'name': 'Insécateur', 'numero': '123'},
            {'name': 'Magmar', 'numero': '126'},
            {'name': 'Scarabrute', 'numero': '127'},
            {'name': 'Magicarpe', 'numero': '129'},
            {'name': 'Léviator', 'numero': '130'},
            {'name': 'Lokhlass', 'numero': '131'},
            {'name': 'Evoli', 'numero': '133'},
            {'name': 'Aquali', 'numero': '134'},
            {'name': 'Voltali', 'numero': '135'},
            {'name': 'Pyroli', 'numero': '136'},
            {'name': 'Amonita', 'numero': '138'},
            {'name': 'Amonistar', 'numero': '139'},
            {'name': 'Kabuto', 'numero': '140'},
            {'name': 'Kabutops', 'numero': '141'},
            {'name': 'Ptéra', 'numero': '142'},
            {'name': 'Artikodin', 'numero': '144'},
            {'name': 'Electhor', 'numero': '145'},
            {'name': 'Sulfura', 'numero': '146'},
            {'name': 'Minidraco', 'numero': '147'},
            {'name': 'Draco', 'numero': '148'},
            {'name': 'Dracolosse', 'numero': '149'}
        ]

        self.gen2 = [
            {'name': 'Germignon', 'numero': '152'},
            {'name': 'Macronium', 'numero': '153'},
            {'name': 'Meganium', 'numero': '154'},
            {'name': 'Héricendre', 'numero': '155'},
            {'name': 'Feurisson', 'numero': '156'},
            {'name': 'Typhlosion', 'numero': '157'},
            {'name': 'Kainminus', 'numero': '158'},
            {'name': 'Crocodil', 'numero': '159'},
            {'name': 'Aligatueur', 'numero': '160'},
            {'name': 'Pichu', 'numero': '172'},
            {'name': 'Toudoudou', 'numero': '174'},
            {'name': 'Togepi', 'numero': '175'},
            {'name': 'Togetic', 'numero': '176'},
            {'name': 'Natu', 'numero': '177'},
            {'name': 'Xatu', 'numero': '178'},
            {'name': 'Wattouat', 'numero': '179'},
            {'name': 'Lainergie', 'numero': '180'},
            {'name': 'Pharamp', 'numero': '181'},
            {'name': 'Marill', 'numero': '183'},
            {'name': 'Azumarill', 'numero': '184'},
            {'name': 'Tournegrin', 'numero': '191'},
            {'name': 'Héliatronc', 'numero': '192'},
            {'name': 'Mentali', 'numero': '196'},
            {'name': 'Noctali', 'numero': '197'},
            {'name': 'Cornebre', 'numero': '198'},
            {'name': 'Feuforeve', 'numero': '200'},
            {'name': 'Pomdepik', 'numero': '204'},
            {'name': 'Foretress', 'numero': '205'},
            {'name': 'Snubbull', 'numero': '209'},
            {'name': 'Granbull', 'numero': '210'},
            {'name': 'Cizayox', 'numero': '212'},
            {'name': 'Caratroc', 'numero': '213'},
            {'name': 'Marcacrin', 'numero': '220'},
            {'name': 'Cochignon', 'numero': '221'},
            {'name': 'Cadoizo', 'numero': '225'},
            {'name': 'Malosse', 'numero': '228'},
            {'name': 'Demolosse', 'numero': '229'},
            {'name': 'Magby', 'numero': '240'},
            {'name': 'Embrylex', 'numero': '246'},
            {'name': 'Ymphect', 'numero': '247'},
            {'name': 'Tyranocif', 'numero': '248'},
            {'name': 'Lugia', 'numero': '249'},
            {'name': 'Ho-oh', 'numero': '250'}
        ]

        self.gen3 = [
            {'name': 'Arcko','numero': '252'},
            {'name': 'Massko','numero': '253'},
            {'name': 'Jungko','numero': '254'},
            {'name': 'Medhyèna', 'numero': '261'},
            {'name': 'Grahyèna', 'numero': '262'},
            {'name': 'Zigzaton', 'numero': '263'},
            {'name': 'Linéon', 'numero': '264'},
            {'name': 'Nénupiot', 'numero': '270'},
            {'name': 'Lombre', 'numero': '271'},
            {'name': 'Ludicolo', 'numero': '272'},
            {'name': 'Nirondelle', 'numero': '276'},
            {'name': 'Hélédelle', 'numero': '277'},
            {'name': 'Goélise', 'numero': '278'},
            {'name': 'Bekipan', 'numero': '279'},
            {'name': 'Makuhita', 'numero': '296'},
            {'name': 'Hariyama', 'numero': '297'},
            {'name': 'Azurill', 'numero': '298'},
            {'name': 'Ténéfix', 'numero': '302'},
            {'name': 'Mysdibule', 'numero': '302'},
            {'name': 'Galekid', 'numero': '303'},
            {'name': 'Galegon', 'numero': '304'},
            {'name': 'Galeking', 'numero': '305'},
            {'name': 'Méditikka', 'numero': '306'},
            {'name': 'Charmina', 'numero': '307'},
            {'name': 'Posipi', 'numero': '311'},
            {'name': 'Négapi', 'numero': '312'},
            {'name': 'Rosélia', 'numero': '315'},
            {'name': 'Wailmer', 'numero': '320'},
            {'name': 'Wailord', 'numero': '321'},
            {'name': 'Spoink', 'numero': '325'},
            {'name': 'Groret', 'numero': '326'},
            {'name': 'Tylton', 'numero': '333'},
            {'name': 'Altaria', 'numero': '334'},
            {'name': 'Séléroc', 'numero': '337'},
            {'name': 'Solaroc', 'numero': '338'},
            {'name': 'Barpau', 'numero': '349'},
            {'name': 'Milobellus', 'numero': '350'},
            {'name': 'Morphéo', 'numero': '351'},
            {'name': 'Polichombr', 'numero': '353'},
            {'name': 'Branette', 'numero': '354'},
            {'name': 'Skelénox', 'numero': '355'},
            {'name': 'Téraclope', 'numero': '356'},
            {'name': 'Absol', 'numero': '359'},
            {'name': 'Stalgamin', 'numero': '361'},
            {"name": 'Oniglali',"numero": '362'},
            {'name': 'Obalie','numero': '363'},
            {'name': 'Phogleur','numero': '364'},
            {'name': 'Kaimorse', 'numero': '365'},
            {'name': 'Coquiperl', 'numero': '366'},
            {'name': 'Serpang', 'numero': '367'},
            {'name': 'Rosabyss', 'numero': '368'},
            {'name': 'Lovdisc', 'numero': '370'},
            {'name': 'Draby', 'numero': '371'},
            {'name': 'Drackhaus', 'numero': '372'},
            {'name': 'Drattak', 'numero': '373'},
            {'name': 'Terhal', 'numero': '374'},
            {'name': 'Métang', 'numero': '375'},
            {'name': 'Métalosse', 'numero': '376'},
            {'name': 'Latias', 'numero': '380'},
            {'name': 'Latios', 'numero': '381'},
            {'name': 'Kyogre', 'numero': '382'},
            {'name': 'Groudon', 'numero': '383'}
        ]

        self.gen4 = [
            {'name': 'Lixy','numero': '403'},
            {'name': 'Luxio','numero': '404'},
            {'name': 'Luxray','numero': '405'},
            {'name': 'Rozbouton', 'numero': '406'},
            {'name': 'Roserade', 'numero': '407'},
            {'name': 'Apitrini', 'numero': '415'},
            {'name': 'Apireine', 'numero': '416'},
            {'name': 'Baudrive', 'numero': '425'},
            {'name': 'Grodrive', 'numero': '426'},
            {'name': 'Laporeille', 'numero': '427'},
            {'name': 'Lockpin', 'numero': '428'},
            {'name': 'Magirêve', 'numero': '429'},
            {'name': 'Corboss', 'numero': '430'},
            {'name': 'Magnézone', 'numero': '462'},
            {'name': 'Maganon', 'numero': '467'},
            {'name': 'Phyllali', 'numero': '470'},
            {'name': 'Givrali', 'numero': '471'},
            {'name': 'Mammochon', 'numero': '473'},
            {'name': 'Noctunoir', 'numero': '477'},
            {'name': 'Momartik', 'numero': '478'}
        ]

    def get_gen(self, value):
        value = int(value)
        if value == 1:
            G1 = []
            for g1 in self.gen1:
                G1.append(g1.get('name'))
            return ', '.join(G1)
        if value == 2:
            G2 = []
            for g2 in self.gen2:
                G2.append(g2.get('name'))
            return ', '.join(G2)
        if value == 3:
            G3 = []
            for g3 in self.gen3:
                G3.append(g3.get('name'))
            return ', '.join(G3)
        if value == 4:
            G4 = []
            for g4 in self.gen4:
                G4.append(g4.get('name'))
            return ', '.join(G4)

    def get_chroma(self, value):
        for g1 in self.gen1:
            if g1.get('name').title() == value.title():
                return g1

        for g2 in self.gen2:
            if g2.get('name').title() == value.title():
                return g2

        for g3 in self.gen3:
            if g3.get('name').title() == value.title():
                return g3

        for g4 in self.gen4:
            if g4.get('name').title() == value.title():
                return g4
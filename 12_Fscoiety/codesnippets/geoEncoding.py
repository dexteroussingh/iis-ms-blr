from requests import get
city=['A F Station Yelahanka', 'Agram', 'Air Force Hospital', 'Amruthahalli', 'Anandnagar', 'Arabic College', 'Attur', 'Austin Town', 'Banaswadi', 'Bangalore Bazaar', 'Bangalore International Airport', 'Bangalore Sub Foreign Post', 'Bellandur', 'Benson Town', 'Bhattarahalli', 'Bidrahalli', 'BSF Campus Yelahanka', 'Byatarayanapura', 'C.V.Raman Nagar', 'CMM Court Complex', 'CMP Centre And School', 'CRPF Campus Yelahanka', 'Devanagundi', 'Devasandra', 'Doddagubbi', 'Doddanekkundi', 'Domlur', 'Doorvaninagar', 'Dr. Ambedkar Veedhi', 'Dr. Shivarama Karanth Nagar', 'EPIP', 'Fraser Town', 'G.K.V.K.', 'Gunjur', 'H.A. Farm', 'H.A.L II Stage', 'H.K.P. Road', 'Hebbal Kempapura', 'HighCourt', 'Hoodi', 'Horamavu', 'Hulsur Bazaar', 'Indiranagar', 'ISRO Anthariksha Bhavan', 'J.C.Nagar', 'Jakkur', 'Jalavayuvihar', 'Jayamahal Road', 'Jeevanbhimanagar', 'Kadugodi Extention', 'Kadugodi', 'Kalkunte', 'Kalyananagar', 'Kannamangala', 'Kodigehalli', 'Kothanur', 'Krishnarajapuram R S', 'Krishnarajapuram', 'Kundalahalli', 'Legislators Home', 'Lingarajapuram', 'Mahadevapura', 'Mahatma Gandhi Road', 'Marathahalli Colony', 'Maruthi Sevanagar', 'Medimallasandra', 'Mundur', 'Museum Road', 'Muthusandra', 'Naduvathi', 'NAL', 'New Thippasandra', 'P&T Col. Kavalbyrasandra', 'Panathur', 'R T Nagar', 'R.M.V. Extension II Stage', 'Rajanakunte', 'Rajbhavan', 'Ramamurthy Nagar', 'Rameshnagar', 'Richmond Town', 'Sadashivanagar', 'Sahakaranagar P.O', 'Samethanahalli', 'Singanayakanahalli', 'Sivan Chetty Gardens', 'St. Thomas Town', 'Training Command IAF', 'Vartur', 'Vasanthanagar', 'Venkateshapura', 'Vidhana Soudha', 'Vimanapura', 'Virgonagar', 'Viveknagar', 'Whitefield', 'Yelahanka', 'Yelahanka Satellite Town', 'Bangalore', 'Adugodi', 'Agara', 'Anjanapura', 'Ashoknagar', 'B Sk II Stage', 'Banashankari III Stage', 'Banashankari', 'Bangalore Corporation Building', 'Bannerghatta Road', 'Bannerghatta', 'Basavanagudi', 'Begur', 'Bnagalore Viswavidalaya', 'Bolare', 'Bommanahalli', 'Bommasandra Industrial Estate', 'Carmelram', 'Chamrajpet', 'Chandapura', 'Chandapura', 'Chickpet', 'Chikkalasandra', 'Chudenapura', 'Dasarahalli(Srinagar)', 'Deepanjalinagar', 'Dharmaram College', 'Doddakallasandra', 'Electronics City', 'Gaviopuram Extension', 'Girinagar', 'Gottigere', 'Governmemnt Electric Factory', 'Haragadde', 'Hennagara', 'HSR Layout', 'Hulimangala', 'Hulimavu', 'Hulimavu', 'Huskur', 'J P Nagar', 'Jayanagar', 'Jayanagar West', 'Jayangar III Block', 'Jigani', 'JP Nagar III Phase', 'JP Nagar VIII phase', 'Kagalipura', 'Kalkere', 'Kallubalu', 'Kathriguppe', 'Kengeri', 'Konanakunte', 'Koramangala I Block', 'Koramangala', 'Koramangala VI Bk', 'Kumaraswamy Layout', 'Kumbalagodu', 'Kumbalgodu Gollahalli', 'Madhavan Park', 'Madivala', 'Mallathahalli', 'Mavalli', 'Mico Layout', 'Mount St Joseph', 'Muthanallur', 'Nayandahalli', 'Padmanabhnagar', 'Pampamahakavi Road', 'Ragihalli', 'Rajarajeshwarinagar', 'Ramohalli', 'Rv Niketan', 'Sakalavara', 'Sampangiramnagar', 'Shanthinagar', 'Singasandra', 'Somanhalli', "St. John's Medical College", 'State Bank Of Mysore Colony', 'Subramanyapura', 'Sulikere', 'Taralu', 'Tavarekere', 'Thalaghattapura', 'Thataguni', 'Thattekuppe', 'Thyagarajnagar', 'Tilaknagar', 'Tyagrajnagar', 'Udaypura', 'Ullalu Upanagar', 'Wilson Garden', 'Wipro Limited', 'Yelachenahalli', 'Achitnagar', 'Bagalgunte', 'Bangalore City', 'Bangalore Dist Offices Bldg', 'Bapagrama', 'Basaveshwaranagar', 'Byatha', 'Chandra Lay Out', 'Chikkabanavara', 'Chikkabidarkal', 'Gayathrinagar', 'Hampinagar', 'Herohalli', 'Hessarghatta Lake', 'Hessarghatta', 'Industrial Estate', 'Jalahalli East', 'Jalahalli', 'Jalahalli West', 'K H B Colony', 'K. G. Road', 'Kakolu', 'Kamakshipalya', 'Kodigehalli', 'Kodigehalli', 'Laggere', 'Magadi Road', 'Mahalakshmipuram Layout', 'Malleswaram', 'Malleswaram West', 'Mathikere', 'Msrit', 'Nagarbhavi', 'Nagasandra', 'Nandinilayout', 'Nelakadiranahalli', 'Palace Guttahalli', 'Peenya Dasarahalli', 'Peenya I Stage', 'Peenya Small Industries', 'Rajajinagar', 'Rajajinagar IVth Block', 'Science Institute', 'Seshadripuram', 'Shivakote', 'Silvepura', 'Sri Chowdeshwari', 'Srirampuram', 'Swimming Pool Extn', 'Tarabanahalli', 'Vidyaranyapura', 'Vijayanagar East', 'Vijayanagar', 'Viswaneedam', 'Vyalikaval Extn', 'West of Chord Road II stage', 'Yeshwanthpur Bazar', 'Yeswanthpura', 'Abbur', 'Achalu', 'Adarangi', 'Agalakote', 'Ajjanahalli', 'Akkur', 'Akkur', 'Alahalli', 'Alanatha', 'Alurduddanahalli', 'Aluru', 'Ambadahalli', 'Anekal', 'Anjanapura', 'Ankanahalli', 'Anneshwara', 'Antharahalli', 'Aradeshanahalli', 'Arakere', 'Aralalasandra', 'Arallumallige', 'Arasinakunte', 'Arebommnahalli', 'Arudi', 'Attibele', 'Attihalli', 'Attikuppe', 'Attimagere', '', 'Averahalli', 'Bachenahatti', 'Bagalur', 'Baginigere', 'Baktharahalli', 'Banavadi', 'Banavasi', 'Bandikodigehalli', 'Bannikuppe', 'Bannimakodalu', 'Baragenahalli', 'Basettihalli', 'Begur', 'Bendiganahalli', 'Bestamaranahalli', 'Bettahalsur', 'Bettakote', 'Bevur', 'Bevurmandya', 'Bidadi', 'Bidalur', 'Bidaraguppe', 'Bijjahalli', 'Bijjawara', 'Bilagumba', 'Bilagumba', 'Billanakote', 'Biskur', 'Budigere', 'Budihal', 'Byagadadenahalli', 'Bylakere', 'Bylanarasapura', 'Byramangala', 'Chakarabhavi', 'Chakkalur', 'Chakkere', 'Chamarajasagara', 'Channapatna Bazar', 'Channapatna', 'Channarayapatna', 'Cheelur', 'Chikkajala', 'Chikkalahalli', 'Chikkamuduvadi', 'Chikkanahalli', 'Chunchanakuppe', 'Dasanapura', 'Devanahalli', 'Devarahosahalli', 'Dobbespet', 'Dodballapura Bazar', 'Dodballapura', 'Doddabelavangala', 'Doddabele', 'Doddagangawadi', 'Doddagattiganabbe', 'Doddahejjaji', 'Doddajala', 'Doddakabballi', 'Doddamudigere', 'Doddanallala', 'Doddasanne', 'Doddasomanahalli', 'Doddatumkur', 'Dommasandra', 'Ganakal', 'Ganalu', 'Gangonahalli', 'Gantiganahalli', 'Garakahalli', 'GCEC Ramanagara', 'Gejjagaragupppe', 'Girenahalli', 'Gollahalli', 'Gollahalli', 'Gottigehalli', 'Government Silk Farm', 'Gowdagere', 'Guddanahalli', 'Gudemaranahalli', 'Gundamgere', 'Guttalahunase', 'H.Kothanuru', 'Hadonahalli', 'Hagalahalli', 'Hanabe', 'Hanchaguli', 'Handenahalli', 'Harathi', 'Harisandra', 'Harobele', 'Harohalli', 'Harohalli', 'Hasigala', 'Heggadahalli', 'Hegganahalli', 'Heggunda', 'Hejjala', 'Helagahalli', 'Herandyappanahalli', 'Hindaganala', 'Honganur', 'Honnasandra', 'Honnayakanahalli', 'Honniganahalli', 'Horalagallu', 'Hosadurga', 'Hosahalli', 'Hoskote Indl. Area', 'Hoskote', 'Hosur', 'Hulikal', 'Hulikunte', 'Hullegowdanahalli', 'Hullenahalli', 'Hunasamaranahalli', 'Hunasanahalli', 'Hunkunda', 'Huskur', 'Ibasapura', 'Iggalur', 'Ijoor Ramangaram', 'Indalavadi', 'Ittmadu', 'Jadigenahalli', 'Jagadapura', 'Jakkanahalli', 'Jakkasandra', 'Jalamangala', 'Jalige', 'Jodidasarahalli', 'K.Karenahalli', 'K.Satyavara', 'Kabbal', 'Kadabagere', 'Kadahalli', 'Kadalappanahalli', 'Kadanur', 'Kaggala Halli', 'Kailancha', 'Kalari', 'Kallahalli', 'Kallanakupppe', 'Kalludevanahalli', 'Kalya', 'Kambalu', 'Kanakapura Bazar', 'Kanakapura', 'Kanasavadi', 'Kanchugaranahalli', 'Kannamangala', 'Kannamangala', 'Kannur', 'Kanva', 'Karahalli', 'Karikaldoddi', 'Karlamangala', 'Kattigenahalli', 'Kembliganahalli', 'Kempasagara', 'Kithanahalli', 'Kodamballi', 'Kodigehalli', 'Kodihalli', 'Koira', 'Kolagondanahalli', 'Koligere', 'Kollalagatta', 'Kollathur', 'Kolliganahalli', 'Kongadiyappa Road', 'Konnagatta', 'Korati', 'Kottagalu', 'Krishnapuradoddi', 'Kudlur', 'Kudur', 'Kugur', 'Kuluvanahalli', 'Kumbalahalli', 'Kundana', 'Kurupet', 'Kutgal', 'Kyasapura', 'Lakkenahalli', 'Lakkojanahalli', 'Lakkondanahalli', 'Lakkur', 'Lakshmipura', 'Lakshmipura', 'Lalaghatta', 'Madabal', 'Madalakote', 'Madanayakanahalli', 'Madavara', 'Madigondanahalli', 'Magadi', 'Mahadevapura', 'Makali', 'Makali', 'Malgal', 'Mallarabanavadi', 'Mallathahalli', 'Mallligemetlu', 'Malur', 'Manchanabele', 'Manchanayakanahalli', 'Manchegowdanapalya', 'Mandibele', 'Mandigere', 'Mankunda', 'Manne', 'Manniganahalli', 'Maralakunte', 'Maralavadi', 'Marale', 'Marasandra', 'Marchanhalli', 'Marikuppe', 'Marlebekuppe', 'Marsur', 'Mathahalli', 'Mathikere', 'Mayaganahalli', 'Mayasandra', 'Mayasandra', 'Medamaranahalli', 'Melekote', 'Mogenahalli', 'Motagondanahalli', 'Mudugere', 'Mugabala', 'Mullahalli', 'Mylanahalli', 'Mylanayakanhalli', '', 'Nagavara', 'Nandagudi', 'Narasandra', 'Narasipura', 'Narayanapura', 'Narayanapura', 'Nelamangala', 'Nelavagilu', 'Neralur', 'Neralur', 'Neriga', 'Niduvanda', 'Obalapura', 'Purushanahalli', 'Rajaghatta', 'Ramanagaram', 'Rameshwara', 'Rampura', 'Reddihalli', 'Sadahalli', 'Sakkaaregollahalli', 'Samandur', 'Sankighatta', 'Sarjapura', 'Sasalu', 'Sathanur', 'Sathanur', 'Shanumangala', 'Shettihalli', 'Shivagange', 'Shivanahalli', 'Shivanapura', 'Shivanapura', 'Shivapura', 'Sidihoskote', 'Singarajipura', 'Sirigiripura', 'Sogala', 'Soladevanahalli', 'Solur', 'Sondekoppa', 'Sri Subramanyaghati', 'Sugganahalli', 'Sugganahalli', 'Sulebele', 'Sulleri', 'Syakaladevanapura', 'T.Hosahalli', 'Tagachagere', 'Tarahunise', 'Tattekere', 'Tavarekere', 'Tavarekere', 'Teppadabeguru', 'Terubeedi', 'Thaggikuppe', 'Thammanayakanahalli', 'Thimmasandra', 'Thippasandra', 'Tippur', 'Torebekuppe', 'Tubugere', 'Tungani', 'Tyamagondlu', 'Udukunte', 'Uganavadi', 'Uragapura', 'Vagata Agrahara', 'Vanakanahalli', 'Veerapura', 'Veeregowdanadoddi', 'Venkatagirikote', 'Venkatarayanadoddi', 'Vidyanagara', 'Vijayapaura', 'Virupakshipura', 'Vishwanathapura', 'Yadamaranahalli', 'Yadavanahalli', 'Yelekyathanahalli', 'Yeletotadahalli', 'Yeliyur', 'Yennegere', 'Yentiganahalli', 'Yerehalli']
for c in city:
	url="https://atlas.mapmyindia.com/api/places/geocode?address="+c
	r=get(url, headers={"Authorization":"26cc0519-6ca0-4b6e-b0f3-98b8d7d07912"})
	# print(r.json())
	try:
		a=r.json()['copResults']
		lat=a['latitude']
		lo=a['longitude']
		print(c+","+str(lat)+","+str(lo))	
	except:
		pass
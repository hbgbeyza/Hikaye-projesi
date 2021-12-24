import random

title = "spook", "hayalet", "zıt kutuplar", "suit"


story = ("\tSizin duymadığınız ama benim konuştuğum o kadar şey var ki kafamın içi bir film seti gibi.\n"
      "Farklı farklı senaryolar, çekilmeyi bekleyen sahneler, çekildiğinden pişman olunan sahneler...\n"
      "Benim hikayemin de öyle anlatmaya değer pek bir yanı yoktu. Sabah kalkıyor işe gidiyor ve ertesi gün yine aynı şeyi yapıyordum.\n"
      "Taa ki ölene kadar. Ne zamanki dünyada öldüm işte hikayem o zaman başladı.\n"
      "Ben 12 aralık gecesinden itibaren artık bir Hayaletim...\n")

story2 = ("\n\tAkıllı kol saatinden sessizliğe ‘tın’ sesi yayıldı. Süre dolmuştu. Kalem  i kenara koydu elindeki A4\n"
      "kağıdına baktı bu saçmalığı niye kâğıda karaladığına pek de kafa yormadı. ")

possibility1 = ("Kâğıdı şömineye doğru bıraktı ve yanışını izledi.","Cebinden metal işlemeli zipposunu çıkarttı, kâğıdı köşesinden tutuşturup metal tepsinin üzerine bıraktı.", "Kâğıdı parçalara ayırıp şöminenin ateşine bıraktı. ")

story3 = (" Küllere dönen kâğıt rahatlamasına sebep oldu.")

possibility2 = ('\n\tUzun cam duvarın karşısına geçti. Önceden cama kurmuş olduğu zipline halatlarına kendini bağladı.\nKendini boşluğa bıraktığında artık güvenlik gelmeden işini halletmesi için 15 dakikası vardı. \nBalkon kapısından içeri girdi. Yerde yatan birkaç insan vardı. Uyku gazı etkisini göstermişti.', '\n\tUzun cam duvarın önüne geçti. Kolundaki saatin bildirimi uyku gazının etkisinin sona erdiğini söylüyordu. \nElindeki yapışkan eldivenlerle cama tutundu ve bedinin aşağı sarkıttı. Yavaş ve temkinli hareketlerle \n2 kat aşağıdaki odaya indi. Camda dikdörtgen bir alan çizdi. Dirseğini vurdu. Muazzam kırılan camdan içeri girdi.', '\n\tTakım elbisesini düzeltti. Aracına binip partinin yapılacağı malikâneye gitti. Edward Sam adındaki adamın\n gözü gibi sakladığı füze kodlarına bugün veda etmesi gerekecekti. Araçtan inip içeri girdi. \nAslında malikanenin güvenliği gayet iyiydi. Dijital davetiye ve iris taraması ile alıyorlardı. \nGüvenlik her ne kadar iyi olsa da bu şık takımlı hayalet onlardan daha iyiydi. Sistemi heklemiş ve kendi bilgilerini girmişti. \nİçeri girmek gayet kolay olmuştu. Ama zorluk konuklara geçişin yasak olduğu üst kattaki çalışma odasıydı. Edward aynı zamanda \nsilah kaçakçısı olduğundan güvenlik sistemi fazla sıkıydı. Güvenlik odasında harekete duyarlı kırk iki 8k kameralar vardı. Ve daha da önemlisi her \n12 dakikada bir rasgele değişen 12 haneli bir şifre vardı ve şifre güncel olarak Edward’ın telefonuna iletiliyordu. Gerçekten kolay olacaktı(!).\n'
 "Partide biraz vakit öldürdü. Bir bando üsteğmeni ve orkestrasının sahne aldığı bu görsel şölenden etkilenmemişte değildi aslında.  Ve Edward’ın telefonunu ele geçirdi. Edward konuşma yapmak için sahneye çıktığında vakit gelmişti. \nMaskeli garsonlardan birinin kılığına girdi. Merdivenlerden çıktı. Sistem yüzünü tanımlayamazdı zaten bu adam çoktan ölmüştü. \nParmak izi tutucuyu parmağına geçirdi. Parmak izini bardaktan halletmişti. Telefonun touch id’sini açtı. Çıkan 12 haneli rakamı girdi.\nİçerdeydi. ")

story4 = ("\tBilgisayar odasına geçti. Bilgisayara ilerleyip Flaşını taktı. Bir iki klavye tıkırtısı ve hazır. \nEkranda çıkan dans eden hayalet simgesi eşliğinde bilgiler flaşa yüklendi\n"
"\nAyak seslerii...\n"
"\n\tHayalet saatine baktı beklediğinden 10 dakika erken gelmişlerdi. Böylesi daha eğlenceli olacaktı. \nFlaş yüklenirken kaçış yolunu hazırladı cama zipline’ı  kurdu. ")

possibility3 = ('O sırada tam arkasında iki adam gördü. Polislerden biri “ellerini göreyim” dedi. \nHayalet güldü “peki ama ellerimdekiler pek hoşuna gitmeyecek” dedi ve saniyesinde çantadan yarı otomatik pompalı tüfeği çıkartarak ilk konuşanı adamı, \nardından yanındakini vurdu. Arkasında beliren polise tüfeğin kabzasıyla önce kafasının soluna, ardından sağına iki darbe indirdi. Arkasına geçen yeni \nadama dönüp yumruk attı kabzayı kafasına vurdu. Kendini toparlayan az önceki adam ona tekme savurdu. Tekme midesine gelmişti. Arkasından boynuna dolanan \nadama kendi kolunun altın ateş etti. Adam yere serildi. Diğer adama kabzayı tekrar geçirdi ve başını masaya vurdu. İki adam mı? Hayalet için hiçbir şeydi.' , 'Kapının ardına saklandı içeriye “kaldır ellerini” diyerek giren güvenliğe üzülmeden edemedi. Kapının ardından \nçıkıp adamın elindeki silaha vurdu. Güvenlik hızlı davranarak yumruğunu salladı lakin hayalet daha hızlıydı. Yumruğu \nyakalayıp adamın elini ters büktü. “a tabi ellerim havada olmalıydı dimi? Pardon” diyerek adamın elini bıraktı\n ve ellerini kaldırdı. Adamın burnuna kafa attı adam geriye doğru birkaç adım atmıştı ki dizine tekme attı adam yere düştü, sırada \nikinci tekme geldi “hala ellerim hava da mı olsun güvenlik beycim?” üçüncü tekme... o sırada içeriye doğru peş peşe adamlar koştu. \nMermi sesleri artık her yerdeydi. Bu ses birçok insanı rahatsız edebilirdi. Ama hayaletin çok hoşuna gidiyordu. O zaten hiç normal olmamıştı ki.')

story5 = "\nAdamların arkası durunca bilgisayara baktı biraz daha vakit lazımdı. Kapıdan içeri kapı kadar bir adam girdi."

possibility4 = '\nİri adam “Benedict Ryan tahmin ettiğimden erken sahalara döndün” diyerek hayalete baktı. “oo ajan Bach beni tahminimden geç buldunuz” dedi.\n -	Sana sürpriz hazırlıyordum\n -	Ahh evet kalbim kırık, biliyorsunuz. Cenaze törenime gelmediniz özellikle sizi beklemiştim oysaki.\n -	Gerçek cenazene hazırlık yapmak varken sahtesiyle vakit harcamak istemedim.\n', 'İri adam “Hayır ama Ben, bu kadar kolay elime düşmemelisin?” diyerek güldü. Bu iri yarı kocaman adam hayaleti tanıyordu. Hatta ona gerçek ismi olan \nBenedict’in kısaltmasıyla seslenmeye bayılırdı. \n- Ajan Bach seni gördüğüme hiç sevinmedim var ya. Bu yumurta kafayı görmesem de cidden olur. \n- Cenazene gelemedim kusuruma bakmadın dimi? \n- Yok canım bende seninkine gelmeyi planlamıyordum zaten\n'

story6 = '\tBu adam kocamandı tek kolundaki kas kütlesi hayaletin üst gövdesinden bile büyük olabilirdi. Bu adamla yumruk yumruğa dövüşmek kesinlikle can acıtıcıydı \nhayalet bunu birçok kez tatmıştı, öyle ki bazen silahtan çıkan merminin bile ona işlemeyeceğini düşünürdü. Ajan Bach silahını çıkarttı. İkili arasında kalan \nmasalarda mermi delikleri oluştu bazı monitörler kullanılmaz hale gelirken camlar tuzlara özenmişti. Benedict “seni özlemişim sevgilim” diye bağırdı. Ajan buna \nBenedict’in tam başının yanından geçen mermi ile cevap verdi. Bu çok yakındı. '

story6_ = ' \nMermiler bittiğinde Benedict “hala berbat bir nişancısın” dedi. Ajan güldü “sen öyle san Ben!” diyerek balkonu işaret etti. Zipline kaçışı iptal olmuştu. \nBenedict içinden sövse de belli etmedi. Bilgisayardan gelen bildirim sesi. Dikkatleri dağıttı. Flaş hazırdı. İkisi de bilgisayara yöneldi.'

possibility5 = 'Benedict elini uzatmıştı ki Bach onun eline vurdu. Benedict adamın boynunu kolunun arasına sıkıştırdı. Bach Benedict’i kavrayıp “kilo mu verdin sen?” diyerek \nduvara fırlattı. Duvarda resmen Benedict’in portresi çıkmıştı. Yerde karnını tutarak güldü. “Keşke kol kaslarına gösterdiğin bu özeni birazda beynine \ngösterseydin. Kim bilir belki de zeki olurdun, ne dersin?” diye sordu. Sürekli birbirlerine ölümcül darbeler indirip karşılık verdiler. Ağır çekim ve arkada \nbiraz müzik agresif bir tango resmi çizebilirdi ', 'işte beklenen kavga başlamıştı. Mermilerden ziyade yumruklar uçuştuğunda daha güzel sanatsal tablolar oluşuyordu. Ajan “Ben, sanırım burnun yamulmuş, \nizninle düzeltiyorum!” diyerek yumruk atacakken Benedict tutu “çek şu patilerini” dedi.', 'bir, iki, üç Bach duvara çarptığı Benedict’ e peş peşe yumruklar indirdi. “Kum torbasına paran yetmiyor herhâlde. İşte lanet ajan maaşı” dedi nefes nefese. \nKafa attı yumruk sırası Benedict’e geçmişti. İkisinin de ağzı burnu kan olmuştu. '

story7 = '\n\tBenedict polisin tekinden kaptığı kelepçeyi kaşla göz arasında Bach’a takmayı başardı. Bilgisayara \ngiderken Bach’ın bilerek önüne serdiği ayağına takıldı. Bach bacaklarının arasına aldığı \nBenedict’in boğazını sıkıştırdı. Ben nefes alamıyordu. “Lanet herif” diye bağırdı. Bach güldü '

possibility6 = '“biliyor musun yüzüne bu renk çok yakışıyor. Mor ve kırmızı karışımı. Sanki son nefes rengi gibi ne dersin?” diye sordu. “Erken seviniyorsun, daha ölmedim!” diye cevap verdi.', '“son nefesini de mi bana harcıyorsun? Bu kadar umursama beni ölümün daha eğlenceli oluyor” dedi. Benedict “şekerini elinden aldığım çocuk kadar safsın!” dedi.', '“bakalım senin o çok övündüğün ceviz kafan ne kadar sağlammış?” dedi. Benedict “senin içi çürük yumurta kafandan sağlamdır” diye karşılık verdi.'

story8 = 'Sonra gülüp kelebeği adamın bacağına üç kere sapladı. Bacaklar acıyla gevşedi. “Seni alça....” Benedict Bach’ın küfürünü parmağı ile susturdu. '

possibility7 = "Aman, şşt sakın kimse uyanmasın, gizlice ayrılalım; çocuklar duymasın", "aa ne kadar ayıp görüşmeyeli iyice terbiyesiz oldun sen", "RTÜK var sayın ajan kendinize gelin", "ayıp oluyor ama"

story9 = 'dedi. Ve gülerek bilgisayara gitti.  Flaşı aldı. Bach elindeki kelepçeden kurtulmaya \nçalışıyordu “ölmemiş olmana seviniyorum.” Diye bağırdı. Benedict balkona koştu karşı binaya kanca makinasını kullanarak kanca attı. \nGitmeden arkasını dönüp seslendi'

possibility8 = '"görüşürüz hayatım(!)"', 'giderim, alışığım gitmelere sen bir daha görmemeye', '"sıfatını bir daha görmemek dileğiyle"' , '"beni fazla özleme yoksa acından ölürsün ve bu hiç hoşuma gitmez. Seni öldürme şerefi bana ait"\n', '"özle beni koca adam"' , '"bir dahaki karşılaşmamıza kadar sakın ölme o işi ben halledeceğim"' , '"şimdilik bay bay", "hoşça kal iki gözüm"', '"seni özlemeyeceğim"'

story10 = 'diyerek büyük bir kahkaha attı ve kendini balkondan aşağı bıraktı bir süre sonra karşı binanın çatısında \nbelirdi ve çatıların üzerinde koşarak gözden kayboldu.'

print((random.choice(title)))
print(story, story2)
print((random.choice(possibility1)), (story3))
print((random.choice(possibility2)))
print(story4)
print((random.choice(possibility3)), story5)
print((random.choice(possibility4)))
print(story6, story6_)
print((random.choice(possibility5)), story7)
print((random.choice(possibility6)))
print(story8)
print((random.choice(possibility7)), story9,(random.choice(possibility8)), story10)



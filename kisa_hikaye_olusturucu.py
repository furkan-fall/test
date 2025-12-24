import colorama
banner_color = colorama.Fore.LIGHTRED_EX
print(banner_color+f"""
      
██╗  ██╗██╗██╗  ██╗ █████╗ ██╗   ██╗███████╗     ██████╗ ██╗     ██╗   ██╗████████╗██╗   ██╗██████╗ ██╗   ██╗ ██████╗██╗   ██╗    ██╗   ██╗██████╗     ██████╗ 
██║  ██║██║██║ ██╔╝██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔═══██╗██║     ██║   ██║╚══██╔══╝██║   ██║██╔══██╗██║   ██║██╔════╝██║   ██║    ██║   ██║╚════██╗   ██╔═████╗
███████║██║█████╔╝ ███████║ ╚████╔╝ █████╗      ██║   ██║██║     ██║   ██║   ██║   ██║   ██║██████╔╝██║   ██║██║     ██║   ██║    ██║   ██║ █████╔╝   ██║██╔██║
██╔══██║██║██╔═██╗ ██╔══██║  ╚██╔╝  ██╔══╝      ██║   ██║██║     ██║   ██║   ██║   ██║   ██║██╔══██╗██║   ██║██║     ██║   ██║    ╚██╗ ██╔╝██╔═══╝    ████╔╝██║
██║  ██║██║██║  ██╗██║  ██║   ██║   ███████╗    ╚██████╔╝███████╗╚██████╔╝   ██║   ╚██████╔╝██║  ██║╚██████╔╝╚██████╗╚██████╔╝     ╚████╔╝ ███████╗██╗╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝       ╚═══╝  ╚══════╝╚═╝ ╚═════╝ 
                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                             

""")
bas_rol_karakterinin_rengi = colorama.Fore.LIGHTYELLOW_EX
olaylarin_geciti_sehirin_rengi = colorama.Fore.MAGENTA
bas_rol_karakterinin_adi = input(bas_rol_karakterinin_rengi+"Lütfen baş rol karakterinin adını giriniz -> ")
olaylarin_geciti_sehir = input(olaylarin_geciti_sehirin_rengi+"Olayların geçtiği şehri giriniz -> ")
metin_rengi = colorama.Fore.WHITE


#Hikaye İçeriği
print(metin_rengi+f"""
{bas_rol_karakterinin_adi}, sabah erkenden uyanıp {olaylarin_geciti_sehir} sokaklarında yürümeye başladı.\n
Güneş yeni doğuyordu ve hava hafif serindi.Küçük bir kafe bulup sıcak bir çay içti.Birden dışarıda bir köpek havlamaya başladı.\n
Merakla dışarı çıkıp köpeğin yanına gitti.Köpek ona dostça baktı ve kuyruğunu salladı.\n
{bas_rol_karakterinin_adi}, köpeğin aç olabileceğini düşündü.Hemen bir fırına gidip biraz ekmek aldı.\n
Köpeğe uzattığında köpek hızla yedi.Bu olay {bas_rol_karakterinin_adi}'i mutlu etti.\n
Günün geri kalanında şehrin güzel yerlerini keşfetti. \n
{bas_rol_karakterinin_adi}, {olaylarin_geciti_sehir}'in ne kadar güzel olduğunu düşündü.\n
Akşam olunca eve dönmek için yürümeye başladı.Yolda eski bir arkadaşını gördü.\n
Arkadaşıyla kahve içip sohbet etti.Sonra eve dönerken gökyüzüne baktı.\n
Yıldızlar parlıyordu ve {bas_rol_karakterinin_adi} huzur doluydu.\n""")
input("Çıkmak için herhangi bir tuşa basınınız......")

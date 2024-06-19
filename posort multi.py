import polib
#Put .po files into the same folder with script
#German
po_de = polib.pofile('loca-de.po', encoding = 'utf-8-sig')
po_de.sort()
po_de.save('sorted loca-de.po')

#French
po_fr = polib.pofile('loca-fr.po', encoding = 'utf-8-sig')
po_fr.sort()
po_fr.save('sorted loca-fr.po')

#Spanish
po_es = polib.pofile('loca-esp.po', encoding = 'utf-8-sig')
po_es.sort()
po_es.save('sorted loca-esp.po')

#Italian
po_it = polib.pofile('loca-it.po', encoding = 'utf-8-sig')
po_it.sort()
po_it.save('sorted loca-it.po')

#Portuguese Brazil
po_pt = polib.pofile('loca-pt.po', encoding = 'utf-8-sig')
po_pt.sort()
po_pt.save('sorted loca-pt.po')

#Russian
po_ru = polib.pofile('loca-rus.po', encoding = 'utf-8-sig')
po_ru.sort()
po_ru.save('sorted loca-rus.po')

#Turkish
po_tur = polib.pofile('loca-tur.po', encoding = 'utf-8-sig')
po_tur.sort()
po_tur.save('sorted loca-tur.po')

#Chinese Simplified
po_zh = polib.pofile('loca-zh.po', encoding = 'utf-8-sig')
po_zh.sort()
po_zh.save('sorted loca-zh.po')
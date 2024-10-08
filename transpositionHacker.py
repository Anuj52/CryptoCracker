import detectEnglish, transpositionDecrypt

def main():
     # You might want to copy & paste this text from the source code at
    # http://invpy.com/transpositionHacker.py
    myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption')
    else:
        print(hackedMessage)

def hackTransposition(message):
     print("Hacking...")
     
     for key in range(1,len(message)):
         print("Trying key #%s..." % key)
         decryptedText = transpositionDecrypt.decryptMessage(key,message)
         #print("DEBUG: %s" % decryptedText)
         if detectEnglish.isEnglish(decryptedText):
             print('\nPossible encryption hack')
             print('Key %s: %s\n' %(key,decryptedText[:100]))
             print('Enter D for done or ENTER to continue hacking.')
             response = input('>')

             if response.strip().upper().startswith('D'):
                 return decryptedText
     return None

if __name__ == '__main__':
    main()
                 
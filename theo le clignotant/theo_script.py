from random import randrange as r
from time import sleep as ts
import os
import requests

ascii_art = "ooooooddooodddddddddddddddddddddxdddxxxxdoccc:::::;;;;;;;;;;;;coxkxdoc:;'...',,;;::::,....,;;;;;,,,,;coooooooooooooooodxocclc'.,:c::::;,,;,,''.............................';:lo:clllllodOXWWMMMMMMMMMMMMMMMMMWMWNWWMMMMWNXXNNNWNK0XWWMMWWWMMMMMMMMMMMMMMMMWNKOxl;,:oxO0KNWMMMMMMMWN0Oxdoolllccccc:::::::;;;" \
"oooooooooooooooddddddddddddddddddddddddddoc:::::;;;;;;;;;;;:::loxxxddddoc;,,:loolc::cc:'..............:looooooooooooldxdl:;;;;;;::::::;;;,'.................................':ccccc::clcldOOxdkkO0KXXXNNNNNNNNNNNNNXXXXKKKK00OOOkkO0kxxxxxxxxxxxxxxxxxxxxxxoc:;,'.',;:cldk0KXXNNNXX0kxdoolllcccc::::::::;;;;" \
"oooooooooooooooooodddddddddddddddddddddddoc::::;;;;;;;;;;;::cllodddooxO0Oxdoodxxxxdxxdo:...............,looooooooooooddoo:;;:::;;::c:,''....................................','':c;;;;:cclloolc;'',;;::::ccccccoxdc:::;;,,,,'''',:c;.................''...........',,;;:cloddxxxxdxxdoollllccccc:::::::::;;;" \
"ddddddoooooooooooooooodddddddddddddddddddoc:;,,,;;,,,,,;;;:::looddddddk00OOkxxxxkkxxkkxo:...............'clloooooooddllolc::::::;;;:,'..........................................,,;::;;:cc::lodl;,,,;;;;;;;;::;::;;;;;;;;;;,,,,,''''''............''...............'''',,;;::cc::cooollllccccc:::::::::::;;;" \
"ddddddoodooooooooooooooooddddoollllllccccc:;,,',,,''''',,,;;cldddoodxkOO00Okxxxxkkxxdxkkxl;...............:llooooooooollc::;::;,,,,'..............................................';::;;:::::cddl:::::::cc:cccccccccc:::::;;;;;;,,,,'''.............................'',,;;;,,,,,',colllcccccc:::::::::::;;;;" \
"0K0kdolllccccc:c:::cccccllodddoc;,'''....',,,''','''''''',;:odkOOkxdddxkOOOkxxxxkkkxoloxOOdl,..............;llooooollccc::;::;'''.',...............................................';::;,;::cclddolcc::cccccccccccccccccc::::;;;,,,,'''........'..................',,,;;::::::::;,:llccccccc::::::::;;;;;;;;" \
"dk0XX0koc:;;;;;;;;;;;;::::cccloooc;''....',,,''',,,,,,,;:cldkO00000OkxxkkkkxxddxxkOxoccldkOkd:'.............'cloollc:::c::;;,.....,,'...............',,,,,,''',''...................';:;,,,;cccloooc::;::::cccccccccccccc:::::;;;;,,,,,''''.',,'.......................',;:clollccclcccccclc;,,,,,,,'''''..." \
"::cox0XKOdc::;:::::::::::cccccccllc:::;:::::;,,;:ccccclodxkOO000000000OOOkkxxdddxkkkd:,:loxkkxl;..............:llc::cc:::;,'.....,'''.........';cldxkkkkkxddoodooooooolcc:,'.........',;,',;:cclocclccclllooooooooddoooolllccc::::;;;;;;,,,,:;'.......................'';:cloolccccclccllldc'..............." \
":ccccldxxdooollllllllllllllllllllllllllllllllldxO0000OO000KKK000000000OOkkxxdddddxOOkc'';clodkkdc,............'cc:;::;;;,,'''...''''......,:lxk0KXNNNNNNNNNXXXXXNNNNNXXXKKOxlc:,......',,',;:cclooooooloxdddddddddddddddoooooollccc:::;;,,,;:,........................',;;:clllcccccclllloxc'..............." \
"oolllooodddddddddddddddooooddooooooooooooooodk0XNNNNNNXXXXXXXKK000000OOkkxxdddooddk00o...';cloxkkdc,..........,;,',,,,'.',,'.....'''''.,cdk0XNNWWWWWMMMMMMMMMMMMMMMMMMWWWWNNX0kxl:,....',,,;:cccok0XXK0KOxkkkkkkOOOOOOOOkkkkxxxddoooolllllcll,...................''''',;;;:cllllllccclllloxc'..............." \
"xdddooollooodddxxddddddddddddddddoooooooolcc:cldk0XNNNNXXXXXXKKK000OOOkkxdddooooodxk00d,...';cldxkxd:'.......','',;,''''','........',:lx0XNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNXKOxc,....,;:col:oOXN0OXWNXXNNNNNNNNNNWWWNWWNNNNNNNXXXNNXNNNXk;................''',,,;;;::ccllllolc;,,:llcldc................" \
"kkxxxddooolllllooddxxxddddddddddddooollcc:,'....',:ldk0XXXXXKKK00OOOkkxxdoooolllloddddO0d,...';codxkxo:.....,,',,'..';,'...........;lx0XNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNXK0xl;...,:ldockX0kk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMWXNWMMMMMWx,'.............',,,;;;:::ccloooooolc;;,,ccccld:................" \
"OOOOkkxxddoollcccccloodxxxdddddddol:;,,'''............,:lxO0K000OOkxxddolllllcccclddolldk0d;...':codxxdl,..',,''..'.'.............:x0XNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNXXKOd:..':oooxXN00NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXWMMMMMWk;'..........',,;:::::::ccllooddoolc::,';llccoxc................" \
"XKK0OOkkxxddoollcc:::::clollcc::;,........................';cdxkOkxddolcc::::::::clooolllokOx;...,:lodxxdc,;,,,''...............'lOXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNNXXK0ko;,oxllOXKKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMWWWNKo,.........',;:ccc;;:cclllooddooollll:;cllccokc................" \
"MWWNXKK0OOkxxddolccc::;;;,'...................................';coddolc::;;;;;:ccclllolollloxOx:...,:loddolc:,,...............'cOXNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNNNNXK00Oxl;,;:oddONMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNNXXO:........',;colol::cloooloooooolllllc:cclcclxc.'.............." \
"MMMMMWWNNXK0Okxddolccc::;;,'..........''''........................';ccc:;,,;;:cllooooooooollloxOkc..';cc:;:lc;'.............,o0NWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWNNNXKK00Ox:;:::co0WWNXWMMMMMMMMMMMMMMMMMMMMWWMMWWWWNNXXXKK00d,.......',;clloc;;:ldddolllllllllllcc:cl:;cd:................" \
"MMMMMMMMMMWWNK0Okxoollc::;;,,''......''''............................,:cccllllooooooooooooollooodkkl,,;'.'::;'...........,cxKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNNNNNNXKK000ko;,;:cdkkKNWNWMWWWWWWWNNNXXK000Oxxxxdodkkkxxxdxdddl,.....',,;:cccc:clcldolcc:cclllccccc::;,:dOc.'.............." \
"WMMMMMMMMMMMMMWNX0Okdolc:;,''..........................................;cloooooooooooooooooooooooodkkd;.',,'...........;oOXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNNNNNNNNXXXK0K0d:::cooldKNKNWWWWWWWWNNNNNXKkldxooldxdkKKKKKK0Oxl:'....'',;:ccccccodllol:;;;::ccccccccc:,,lkO:.'.............." \
"WWWWWWWWMMMMMMMMMWNKkdl:;;,''...........................................,:lodddooddoooooooooooooooooddc'.............:dOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNNNNNNNNNNNNXKK00xc:;:c::dKXNWWMMMMMMMMMMMWX0OO000OKXKXNNNKOxl:'......'',,;:llllcccc::cc:;;;;;::::cccc:;:cokO:.'.............." \
"MMWWWWNNNNNWWMMMMMMN0dl:;;,''............................................,:ldddddddddddddddddoooooooooc'.''........'d0XNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWNNNNNNNNNNNNNNXXK0Okd:,,,'';cd0XWMMMMMMMMMMMNKNWNWMWKKNNNWWKd:;;,'.....,;:;;:clooloolcccc:;,,;;;;;;;::c:;:lodkO:.'.'............" \
"MMMMMMMMWN0O0XNNWWNXOoc:;;,''..............................................';:ccc:::::::;;;;;;;;;,'';:c;,''.......'dKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWNNNNNNNNNXXXK0kdc;,''';::oOWMMMMMMMWWNNKKXKKK00kx0NWWNkdkOkdlccdxxdoolcccclloooooolc:;,,;;;;;;;;:;;;,codOk:.''''''........." \
"MMMMMMMMMNkookO0KK0kdc:;;,,''...................................................''''..'''..........';:;,..........o0XNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNNNNNNNNXXXKKOx:,,,,',;coONMMMMMMMWNKK000000000OkkOO0KXXKOkxkOOxdooooollccclooooolc:;,,,;;;;;;;,,;;:oddOk;.''''''........." \
"MMMMMMMMMNkccdkO00kdl:;;,,,,''''''.............................................':loolcloo:','..;c:;cc,...........ckKNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNNNNNNNXXK0kdl;;,,,'',:oxONMMMMMMMMMMMMMMMMN0d:'...cKXkolodxxdoooooollllllclllollc:;,,,,'''''.',,;coddOk;.'.............." \
"MMMMMMMMMNk:;lxOO0Oxl:;,,,,'''''''''............................................;okkxdk00dcc;;clccll;......''...,d0XNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWNNNNXXK0koc::;,'.'',cdxkXWWWMMMMMMMMMMNOl'......,odlcoolllc::::::ccccllcccclllc::;,'..........;ldddOk,................" \
"MMMMMMMMMWO:,lxO000Odc;,,''''''..................................................cdkOOOKKxooooc;;;::,....,,,'...:xKXNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWNNNXXK0Okdc;;,....';:lx0NNNWMMMMMMMWOc'.........,okxo::cc:::ccc::cccccccccccc:::;;'.....',;:ldxxddOk,......'''......." \
"MMMMMMMMMW0c,lk0KXXX0d:,''......................................................'lk0XXXXX0dccddl:;cl;.',;,,'...'cxKXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWNNNXK0Okxl:;,....',';dxk0OOK0KK0OOx,..,clodol:;oOxolooddoodddoccllllllcc::::::::;,''';coooddddxdxOx,.....':oc......." \
"NWMMMMMMMMXl,ckKKXNNKkc,........................................................,oOKXNNNX0dlloxxkOko:;;'.''...',cxKXNNWWMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWNNNNNNNNNNXX0Okkxc,........'loloocccclc::;.'lkOOOkxdooxxdddoc:;;,,;;'..':ll::ccc:ccccc:;',lddoollodxxxdxOx'.....'lxc.;ll;.." \
"lodxkO0KXNXd,:kKXNNX0x:...........................................................cxkxollox00OkkkOkdc,...',,,'',:x0XNNWWMMMMMMWWWWWWWWWWWWNNNNNNNWWWWWWWWWWWWWWWWWWNNNNNNNXXXXXXKKKKKXXXXXXXXK0kkd:'........'cocldodocoooolcoOK0xl::cloddc:;;;::::::;,,'.',:c:'.';:ccccc:;,,,,;:ccodddxxx0d'......ld,:O0dlc:" \
"c:;;;;::cll:':kKXNNXOo,............................................................,o0Kxoodddddddxkd:...',;;,''':d0XXNNWWWWNNNXKKKK000000000KKKKXXXXNNNXXXXNNNNXXXXKKKKK0OOOkkxxdddddxxkOOO00K0kxd:'........':lccooOKKXXXXXNXkddl:cloddc;:ldxxxddddooollc;'.':,......',;:cc;..,:loddddxxx0d.......:::O0doolc" \
"XK0Okkkkxdoc;:kKKXNX0d:.............................................................'d0kkkdx0Odoodkd:.',,,;;,'.':d0XXNNX00OOkxdollccc:::::ccldxkOO0KKKKKKKKKKKKKKK0kkkxdoolc::;,,,,,,,;;:ccloxkkxo:'.........:lclolxNMMMMMMMMN0dlokkxl;:oxxdxxdddoollllcccc;'...........',;;'...';loddxxx0d......':cloolc:;;" \
"MMMMMMMMMWN0l;xKXNNWNKx:,............................................................,xO0KKKK0xxxdkkl,,,,;;,,'..;dKXK0xocc:::;,''.........',,,;clodxO0000KKKK0000Okdllc:;;,,'..............',;cloo:..........;lcccoONMMMMWNXK0x:;:lo:'lkxxxddddoooollllllccc:,....,:,......'....'....':ld0o......';coc,'''.." \
"MMMMMMMMMMMWx;dXNWWWWWKkxl;...........................................................;ONNNNNNWWWWWW0c;;;;',,'..,dKKxl::;'''''''...........'',,,;cloxOOO0KKKK00Okxdlc:;,,,,''.........''......'';c:'.........;c::cxXWMMNxc;;,,;'....'oOxxddoooooooollllllllcc:....cOl,,,'...............;Oo.......,lOx:,;:::" \
"MMMMMMMMMMMWO:dXWWMMMWX0Odc'...........................................................;0WMMMMMMMMMMXo::;;'',...,xXOc;,''',;;:cccccc:;;;;;;;;;:::cloxkOO0KXXKK0Okxolc::;;;;;;;,,;;;:::::;,,''''',;c,.........;c:::dK000o.....,odol,'lkddolloodoooolllllllllccc,...cOc'::;,,'.............::........cOo;,:llc" \
"MMMMMMMMMMMMKloKWMMMMMN0Odc'............................................................'OWMMMMMMMMMKlc;;:,''...'kXd:;;;::cllooooollc::;;;;;;::cclodxOO0KXNNXXK0kxolc::;,,,,,,,,;;::cccccc:::;,,',:,.........;::::c:;;'....:lxxdlxxodolclodddddooollllllllcccc;...lk,.:c:::;,,,.'.................':l:',;:c:" \
"MMMMMMMMMMMMNkxKNWMMMMN0ko:...............................................................kWWMMMMMMMO::;.',''...'OKdcclllooollcc:::;,,''''.'',,;:codk0KKNNWWWNXKOxol:;,'.....''',,,;;,;;::ccc::;;,:;.........,lxkl,lOkc:coONMMWNK0kolcloddddddooollllllllccccc;....'..;cccc:::,';,........'.........;:,,,,,," \
"MMMMMMMMMMMMMXk0NWWMMMWNKkc................................................................kWWMMMMMWk,;;........;0Kxooddooc;;;;;,''.........'''',:ldk0KXNWWMMWWNKko:,'............'''',,,,,;::cc::c:.........':l::0WMMWWMMMMMMNK0xooodxdoloddooolclllllcllclcc:.......;ccccccc;.';..,:'..o:................." \
"MMMMMMMMMMMMWKxONWWMMMMWXOc'...............................................................'kWMMMMMNd,''.'......cKKOxxxdl;,,,'..........';,'.',;:coxOKXNWMMMMMWWN0d;'''...'.............',,',;ccccl:.........';'.dNMMMMMMMMMMNK0xldxxkxolloooool;,;cllcllllccl:.......;ccccccc:'.;'.',...;;................." \
"MMMMMMMMMMMMW0ooKNKkKMWNKkc'...........................................................',...'OWMMMMXo'''''......lXX0Okdl;''...,:,......':oo:'';clodOKXNWWMMMMMMWWXkc,'...,:,.......':c;....'',:cllo:..........,..dWMMMMMMMMWKkOklokkkxdooddoool:,,;clllllccccc;.......;cccccccc;.';'....................',;," \
"MMMMMMMMMMMMWx;c0KdlKWWNKx:'...........................................................'xkl,.;KMMMMXo,,''......'xNK0kxoc;;;;;;:lc,,,',;;:c:::coooxOKXNWWMMMMMMMWWN0dc;,''',,'''...';c:;'....',:clloc.......''.,'.dWMMMMMMMMNkdxdoxkkxxddddoooolc;;:cllllc::ccc,......':ccccclccc,.',........................" \
"kkxxxkO000KX0l;;:dx0NWWXOo,.............................................................cXNKl.:KMMMXl,,,'......;ONX0OkxxxkOkxxdodddoolllllllodxxk0XNNWWWMMMMMMMWWNXOxl:;;;;;:ccc::c::::::cc::::clodl'......'',,';OMMMMMMMMMNd,.,xOkxxxddoooooooolclollllc:;:c:.......;::ccccclcl:'.'..................,;...." \
"kkkkxddl:coxdlcokKNNWWWKx:'..............................................................xWWNo.:KMMXl',,......'cKNNXKK0000OkxddoooollllloodxkkOKXNNWWWMMMMMMMMMMWNXK0kdl::::::::ccccccccccclllllodxd;......',:c,:0MMMMMMMMMNK0ockkxxxdddooooooollclollllc;;;:,......';:::cccclllc:'..................,:;...." \
"XKKK0OxxxxkOxc:lOKXXNWNKd;...............................................................'dOOx;.,dOk:.',.....',dXWNNXXXKKK0OkxxddddxxxxkOOO0KXXNNWWWWMMMMMMMMMMMWNXK00Okxdoollllccccccccllllloooodkkc....'',;cl,cKMMMWMMMWN00Kkxkkxxddddoooooollllollllcc;;;;.......::ccccccclllcl;''................:c,...." \
"NKKKK0KNMMMWKl,;xKXNNWNKd;.................................................................,::,....;;.',.....,:ONWNWNNNNNXXXKKKK00000KKKKXXNNNWWWWWWMMMMMMMMMMMMWWNXK0000OOkkxxxdddddddoddddddxxdxkOd,..';:::l:.:KMMMMWNNXOdkKKOkxddoooooooooollooolllccc:;;'.......''',;:ccclllllc,'...............,c:'.,;," \
"NK0000KNMMMMXo';d0XNNWNKd;.................................................................,cll:...';,,,,,'';,cKWWWWWWWWWWWNNNNNNNNNNNNNNWWWWWWWWMMMMMMMMMMMMMMMMWWNXKKKK00000OOkxkkkkkkkkkkkkkkkkOOk:.':clccl:.cNMMN0xddo;;OXOkxxddoooooollllooolollc:::::,......;;,,'...'',;:llllc:,.'............;c,.;:;'" \
"NK0000KNMMMMNd;ck0XNNWN0o,..................................................................,cll:...';;;::,;:;oKNNWWWWWWWWWWWWWWWWWWMMWWWWWMWWWWWWWWMMMMMMMMMMMMMMWNXK00KKKKKK0OOOkxkO00OOOOOOOkkOO0Ol,;::ccco:.oWNKkddOKO;;KKkxxxddooooolllllooolllc::::;,......;:;::::::;;,'',;:cll:,;'..........,;,',:,'." \
"000KXXXWMMMMNx::d0XNWWNOo'...................................................................;looc'..,clc;,::;dKNNWWWWWMMMMMMMMMMMMMMMMMMWWWWNNNNNNWWMMMMMMMMMMMMMWNNKOkO00KKKKKXKK000000000OOOOOO0OOo;;;:cllo,'OWKO0KXN0;.l0Oxxxddoooollllllooooolc::;;;'......,;;;;:::::cccccc:;;:cccc,..........,,.';,..." \
",;lXWWMMMMMMNk;':kKNWWXOl....................................................................'coddc,.,oxc,;cccxKNNNNNWWWMMMMMMMMMMMMMMMWWWNNXK00KNNWMMMMMMMMMMMMMWWNNKOxddk0KKXXXXXXXKKKK0000000000Oko;;;;cldc'lNNK0KXKx:;cdkkxxddddoollllooooollllc:;;;'......,;;:;;;:::::::cccllc:::cc,..........'..',...." \
"..'dWMMMMMMMNk:.;kKXNNXOc.....................................................................,cdxdl;;dOo;,cddkKXNNNNNWWWWMMMMMMMMMWWWWWNNX0OkOXWWMMMMMMMMMMMMMMWWNNXXK0dcoxO0KXXXXXXXXKKKK000000OOOko:,,;cod:'xMWNXNOclxxddkkxxxddooolooooollllccc:,,,'......';;;;;;;::::::::ccllllc:::;.............'....." \
"doccOWWMMMMMWO:.,kKXNNXkc......................................................................,cdkOo:d0Oo;cdxk0KXXNNNWWWWMMMMMMMWWWNNNXK0OkxkKWMMWWWWWWMMWWWWWWWNXXXKKXKxlodkO0KKKKXXXXK00KK00OOOOkxo;',:odd;'kWMMWO:ckOxxkkxxxddooooddolc::;;;:::;''......',,;;:;;;;:::::::cccllllll:;;..................." \
"00OddO000000Oo;';kXXXXKk:.......................................................................'cdxdld0KKOdooxOKKXXNNWWWWWWWWWWWNNNNXKK0Okkk0WWWWXKKKKXXNNXXXXXXKKOkkxOKKxoodxkO00KKKKKKKKKK00OOkkxdl;;ldddo''xKXNO:cO0xdxkkkxxdoooddol:,''....',,'......'',,,;;:::::::::::cccclllllllc:..................." \
"c::lkx;....';,..;d0KK0ko,.........................................................................;dOOk0XNX0Oxdk0KKXXNNWWWWWWNNNNNXXKK0OOkkxkKNNX0OkxxkkOOOOkkkkkkdoolodkOkddddxkkO00000000000OOkkxdoc:lxkxxc..lddc',oxl;:xkxxxdddxdoc:::;;;:;,'..............',;;:;;::::::ccccllllllllcc;',,..............." \
":;''lo;'..,:::;;codddoc,...........................................................................cxOkOKKK00KkxOKKXXNNNNNNNNNXXXXKK00OOOOkdkK0koc:;,,;:loddooooolc;,;:cloxxxdddxxkOOOOOOOOOOOOkkxxdo::oxxxkd;.......''.'lkkxxxxdoc;,,,,;;::c::;........''''..'',,;;;;:::::cccllllllllollodxd,.......,:,...." \
":::,,;:c:,,:cccclodddo:'...........................................................................,oxdokKKKK0kdk0KKXXXXXXXXXXXKKK000OO0KKKKXKkdc::c::::ccllc:ccc:,,,;;:coxkkkxxxxkkkkkkOkkkkkkkxddol;;oxxxOOx;....,;ckKOkxxxxdl:;;:cc:,,;;;;:::::;...'',;;;;:;;,'',,;;;:::cccllllllooolllc;.........,;....." \
";,,;'.;loo:lxxolc:;;,'..............................................................................;coodO0KKKkodO0KKXXXXXKKXKK0OO00000KXNNNNKOOkxoooooollc::;:::;;;;::ccok00OOOkkxxxxxxxxkkkxxxddolc;:odooc';;'':llox0X0kxxdl:;:loolc;'';:lollloloolll:::;:lllllc:;;;;::ccccccclllolcclll:,,'...,,........." \
";..,'..,ldc;;;,'.....................................................................................;ooxO00Okdclxk0KKKKKKKKKK0OOO000KXXNNNNNX0OOOkxdllllc:::::::::;,,;:clk0000OOOkkxxxxxxxxxxdddoll:,;:;;,..,;;lO0OOkOOkxdoc::lool:,''';cllllcllllloolclllcc:clllllllloolccccccccccllcccloooocc:cllc;;'...." \
"'..,cllokOl..........................................................................................:OKKkx00Oxc:okOKKKKK0KK00OOO000XNNNNNNNNXK0Okxxxdolcc::c:;;::::;;,;;cx0000OOOOkkxxdddddddddolcc:'...',..'..dNN0kkkkxdolllolc;'..';:ccccccccllllcc::ccc::;:cllllllllll::clcccc:::cc:::clllllllc:;;;'...." \
"xdddxxxxxd;...........................................................................................cxxloxxdol:lxkO0KKKK000000KKXXXNNXXNNNXK00Okxxxddolccclc:cc::::;;:cldO0Okkxxkxxdddddddddoollc::clc:lc'.'..o0xdOOkxdlllcc:,'',;:cc:::::::::cc:::::::::c;;:ccccllllcc:::clccc:::;;::;;;cccccccc;'......." \
"kdl:;,,'''............................................................................................,:lddoc;''';odkO00K00000KKKKKKKKK0KXXXK0OOOOOkkxxxxdooooooolllcccoddxOOkxxddddooodddddooollcc;;lkKKX0xoc,....lNN0koc:;,''',;::::;;;;;;;;;;;;;;;:::::::;;;:::cllllcc:::ccccc::;;;;;;;;;;::::::;,......." \
".................................................................................................................;lodkO0000000KKK0OkkkOO0000KKK000OOkxxxddddddoolllcclloddxkkxdooooolllodddoolllc:c:,':oodk0KXKd;..lKxldd:,,''',''''...'''',,,,,;;;;:ccc:;,;;,,;::clllc::::::ccl:;;;,,;;;,,'',,;,'.........." \
"...............................................................................................................:dl:ldxkOOOOO0000OkxdoodxxkOO0Okkdooolooolooollcc::::::::::clllccccccllloddoolllcc:::'..:llcoOXNWNOl:;.lK0o;..........'',,;;;;::ccclllc;'..',,,,;:clllc::;;;;;:::;;,,'',,,'....'''..........." \
".............................................................................................................:xko;,lddxkkkOOOOOkxddollllloddolc::;::::::ccc::;;;,,'''''''''''',;;::cllllooollcccc::;....',,:ox0XWWWNK0XMNklc,.........',;;:::ccc::,'......'',,,;:ccc:;,,'''',,,,'''........................." \
"...........................................................................................................,dkdc;,;coodxxxkkOOOkdollcc:,,,,,''''..'''''',,,'................',;:::::cclooollc::::::;'......';cdk0XWMMMMMWNXKkc'...............................'',,,'.......'''.............................." \
"..........................................................................................................l0Oo:;;:cccloodxxxkOkxollcccllccc:ccclooooollcccccccc::::;;:::::::clloollcccllollc::::;;;;;;,,''.....,ckXWWMMMMMMMWXx'............................................................................" \
".......................................''...............................................................;kKOdlccccc:;:llododxkxxoccloodxxddodddkO00Okkkkkdoodddolllllllllllodddxddolcclllcc:::::;;;;;::;;;cc,.....:d0XNWWWMMMMW0c....'''..................................................'................." \
"........................................',','.....',''.................................................l00xooddoc;'..'clolldddxdoccoxxkkkkkkxdddxxxxxkxxxdddddddoollccccclooddxxddolcccllc:::;;;,,,;:::::cdkxl,.....':ld0NWWMMMMNx;',,,,''................................................''................" \
".....................................................................................................,kKOdooxkxo,..;cddlllloddoollodxxkkkkkkxdddooooolllllllcccc::::::cclloooddddolllcccc:;;;:;,'',;;::cloxOOOkc'........:xKWWMMMWNkl;;;;,,'.............................................'''................" \
"....................................................'''.............................................c0Kxdxkkxdl:;lONWN0xlclooolclodddxxxxxxxdddollc::;;;,,,,,,,,,;;::ccclllooooooollc:::::;;:;,;,'',;:codxO0K0K0x;.........,dKWWWMMMNx:;;;,,''...........................................'''...''..........." \
"...............................................'''.',,,,,'.........................................dXKkkO0kxocoxxkKWWWKdcccclolcllooddxxddxdddoollc:;,,,'..'..'',,;;:cclllloooooolcc::::;;;;,';:,..';:codkO0XXXXXOl'.........;dKWWMMMW0c;;,,,,''''''''''''''........................'''''''''..'............" \
"....................................................''''..........................................dNNXKXXXKKKKXOodKN0d:..:l::lcccccloodddddddodoooolcc:::;',,,;;::cccclllloooooollc:;;::;,,'';cc,.....';codk0XNNNNXx;..........:kXWMMMWKl,;;;,,,,,,,,,,,;,,,,'''''...............''.''''',,,,..'............" \
".................................................................................................lNWWWWWWNNWWWWKdo0Oc.....oo;:cc:cclooodddddddoooodooooolc:::;:cclllllllooooooolc:::;,;,'''';:::,.........';cdkOKNWN0l.........'cdOXWMMWO:;;;;;;;;;;;;;;;;;;;;,,,'''............',,,,',,',,,;'.''..........." \
"................................................................................................:XMWMMMMWNXNWWWXxlol......cxo:;,;::ccclodxxdddxxdxxxxxxxddolllllooolloooddddddolc;;,,'.',,,;::::,.............',ckNWWKd,.......,lclxKWMMWx:;;;;;;:::::::::::;;;,,,''''..........,;;;,,,,'',,;,'',..........." \
"...............................................................................................'0MMMMMMMWWWWWN0l,'........;xxoc;',,;:cclooddddxxxxxxxxxxxddoooooooooooddxxddddol:,,,'..,,,;;:::;;...............',dXWWNO;......':cclkXWMMNd;;;;:::::::::::::;;;;,,,,''''.........;::;;,,,,,,,,,','.........." \
"...............................................................................................xWMMMMMMMMWNKkl,............oxdoc:;'.'',:looodddddodooooodddooooollclloddddooolc;,'...',;;;;;::;;;..............,l;'oKNWN0c..',,..,;lOKXWMMKl;::::::::::c:::::;;,,,,,''''.'........::::;;,,,,',,'''.........." \
"...............'..............................................................................;KMMMMMMMWN0l,...............lxdolc::,'..':llloolllccccclllllllllcc::cccllllc:::;'...';;,;;;:::;;:;........,.....oX0c'lOKNWNKKXNKd;',ckKKXWMNd;:::::::::::::::::;;,,,,'''.'''........;:::;;;,,'''..'.........." \
"...............'............................................................................';kWMMMMWN0xl'.................:xxdoolcc:,'..,;:c:::::::,,;::::::::;;;;:::::;;,''....',;;;;;;;;:;:::;'.......;'....oNWKl'cONWMMMMWWXOddk0NWNWMWOlc::;;::;;:::;;:::::;;;;,,,''''........';:::;;;,''...',........." \
".......................................................................................;:cloxKWMMMMWOc.....................,oxxdoollc::,'..'''',,,,,'..',,,;,,;;,,,,,,,,''.....',;;;;;,,;;:::::;;'.......,;.;,.lNWXOcoXWMMMMMWWWNNWNNWMMMMMKx0KOxdol:;;;;,,;;;;:::::;;;;,,''.......',;;::::;,,....,'........" \
"................'................................................................',;;:llccclxXMMMMMK;........',;;...........cdxddoooolcc:;'.......'''.......................,,,,;;;;;;;;;:::::;;,'.......,:.ck:lKWXKXWMMMMMMMMWMMWWNNWMMMMM0;;0WMWNXKOxol:,,,,;;;;::;;:;,,''.........',;;:::;;'...',........" \
"................'..................................................................,clccccllxNMMMMM0,.......':odl'..........'lddddddoollc:::;,'..........................'',;;;;;;::;;;;:::::;;;,'.......;c.l0doKWWWWMMMMMMMWWWMWWNXNWMMMMMX:.'dNMMMMMMWNXOxl:;,,,,,,,;;,'............',;;::::,...','......." \
"................'.................................................................'colccccclkNMMMMWK;......;okOkl'...........:oddddddoooolccc:::;,'....................',,;;;;;;;;;;;;;:::::;;;,,....'...cc.lKkokKNWWMMMMMMWWWWWWNKKWWWWMWMWd...:0WMMMMMMMMMWXOdc,,,,,,,,...............',,,;;;,..'''......." \
"................'................................................................,clccccccclONMMMMWO,....'ck0K0kc.....'......'coooddoooooolcccccc:;;,,''''',,'....'''',,,;;;;;;;;;;:::::;;::;;;,'....,..'o,.c0O;'oOKNWWWWWWWWWWNXXXNWWWMMWWMKc...'oKWMMMMMMMMMMWNOd:,,,,,'',,................'',..''........" \
"................''.......................................................,c;..'',loc::ccclcoOWWMMMXk;...;d0KKK0k:'............';;;;;:ccclllllllcccccc::;;;;;;;;;;,,,,,;;;;;;;;;;;;::::::;::;;;,'.....,..cl...cx;.'lk0KXNNNWWWWNXNNNWWMMMMMWWNx;....,kNWWWWMMMMMMMWWKo;,''..''''..............',,'..........." \
"................''....................................................;xKXx;..';lllc:ccccccoKWMMMWKO:..:xKXXXK0x:,,.........''........';:ccllllllllllcccc:::;;:::;;;;;;;;,;;,,;;;;;;:::;;;;;;,......',.:x;.'ck0l..,okO0XNNNNNNNWWNNWMMMMWWWWWO:,....,kNNNNNNNWWMWWWWNk:,,,'''',,,,,,'''...'',,,'............" \
"................,'.................................................,o0NMNd,..';llccccccccccdXMMMMNOk:.lOKXNNXK0x::c.........:c,..........,;::clllllllcllllcccc:cc::;;,;,'''......',,;;;,'...........'.,o;','lKNKd:,cdkOKNWWWNNWWXKNWWMMMWWWWMXl,,'...'kWMWWWNNWNNWWWWWKxc::;;::;;;;;;;;;;;;;,'.....'........" \
".............',,'................................................:kNMMMNd,..',clc:ccccccc:ckNMMMMNKOldKXNNNNXK0d;:o;........,oc'...........,;::cccccccccllllcccc::;;,'...............................;l'.,'.dXWWNKxloxk0KNNNWWNK0XNWWMMMMMMMMNd,,,'....xWMMMMMMWWNNWWWWW0l;;;;;;;;;;;;;;,,''......''........" \
"..........',,,,'...............................................:ONMMMMNd,.'',clc::::::::::cOWMMMMWWN0KXNNNNNNKOo'.od,.'...,.'co;............',;:::::::::ccllcc::;,'................................':o:.....xNWWWWW0ddkO0KK0KX0k0NWNWWMMMMMMMWO;,,,'....dNMMMMMMMMWWWNNWWXd,...................''''''......." \
"...........',,'..............................................;kNMMMMMNd,..',cllc::::::::::cOWMMMMWWWNXXNNNWWNKOc.,oOl,;,..,'.;cc,'............,;;:::::::;;;:::;,'...............................';cllc'.....dXWWMWWWKdokOXNXK0xkXWWNNWWMMMMMMMKc,,,,'....oNMMMMMMMMMMMWWWWNOc.................',',,,,......." \
"...........................................................'xNMMMMMMNx,..',clc:::::;::::::c0WMMMMMWWNNXNNNWWNXk,'clOkccc'.'.';:c:;,'...........',;;;::::;,'',,'..............................';cloc;,,......;0WWWWWWW0ookOKNN0xkXWNXNWWMMMMMMMNd,,,,'.....cXMMMMMMMMMMMMMWWWXkdollcccc:;......'''''''......." \
"......................,;'.................................lXMMMMMWMNx,...':c::;;;;;;:::::;lKMMMMMWWWWWNXNNNWNXx,:llO0dodc;:,';;:c:;,.............,,;;;;::;;,,''...........................,:lool;...........:KWWWWWWNXkcokOXX0OO0NXKXWWWMMMMMMWk;,,'','....cXMMMMMMMMMMMMMMWWNKOkkkkkxd:.....,,,''''''......" \
"....................'','................................'xNMMMMMMWWk,....;c:;;;,,,;;;;;;;,oXMWMMMWNNWWWNNNWWNXd:dockKkddl;::.',,:;,''.............'',,,,;;;,,''.....'''''....'.....''..,codoc:;...........'oKWWWWWWNNKOl;lk0KKXKOKX0KNMMMMMMMMMKc''''''.....lXWWMMMMMMMMMMMMMWN0kkkkkxl,....',,''''........." \
"...................''..................................;0WMMMMMMMMK:....;c::;;;;;;:;;;;;;;dXMWWMMWNXNNNWWWWWNKolxo:o0kcc:,',...';;,'................'',,,,,,,''...';:;;;,..''...,:llcldxdc;'.......'.....l0XNWWWWWNXKOko:;o0KXNN0OKXXWMMMMMMMMMWd'.'''''.....lXWWMMMMMMMMMMMWWWXOkkkxo:'..''................" \
"....................'.................................:KMMMMMMMMMXl....,c::;;;;;:::;;;;;;;oKWMMMWWWWWWNNWNNXX0odkc,;xx:,;'......',''.................''',,'''''...;:::;,..'...,coxxxOOxl;.....'...'....'xKXNNWWWWWNK0Okdc;:xKNWWXO0NWMMMMMMMMMMWx,'''''',.....oNWWWMMMMMMMMMWWWWXOxxdl,....................." \
".....................................................:XMMMMMMMMMWx'...'::;;;;;;;:;;;;,;;;,:kWMWMMWMWWWWNNNXXX0xkk:.'lkc','.......''....................'''''''...';;;;,..'...,clodx0Odc'....'','''....cOKXXXNWWWWWX0Okkkdc:ckXWWWK0NMMMMMMMMMMMWx,'''...''.....xNWWWMMMMMMMMMWWWNKkxdc......',,''..........." \
"....................................................,0MMMMMMMMMWO,....:c;;;;;;;;;;;;;;;;,,,c0WWMMMMWWWWNNNNNN0xOO:..;xo'''.......................................',,,'..'...,cllldOxl;.....,::,,'...:kKXXNNNNNWWWNK0KKKK0xlcoOXNWNNWMMMMMMMMWWNNO:''''...''....,OWWWWMMMMMMMMWWWWN0xdc'.......',,,,,,,;;,..." \
"....................''''''''....'''.................xWMMMMMMMMMKc....,::;,;,,,;;;;;;;;;,,,,'lXWWMMMMMWWWXXXXXOkOd;..'lo'.........................................'''.......,:cccdOd:'....';c:,'...'o0XXWWWWWWWWWNK0KXXXXXKkold0XWWMMMMMMMMMWNWNXXk,''''.........;0WWWWMMMMMMWWWWWWXOdc'....................." \
"..........................''''',,,,,'..............oNMMMMMMMMMWd....'::;,,;;;;;;;;;;;;,,,,,.'xWWWMMMMMMWNXXNKkOOc....;o,..................................................',:::okl,.....,ld;.'...:x0KXNWWWWWWWWNK0O0000XNNXOdox0NMMMMMMMMMWNNWWWWKc.'''..........lXNNWWWWMMMWWWWWNWXxc'....................." \
"...........................'',,;;,,,,'............lNMMMMMMMMMW0;....,:;;;;;;;;;;,;;;;,,,,,,..;KWWMMMMMMMWNXX0xOXO:....c;...................................................',,lxc'....';:cl,....lk00KXNWWWWWWNXK000KKXNWWWWN0kOXWMMMMMMMMWWWWMMMMNd'.''...........kNNNWWWWWWWWWWWWWN0l'.......,,............" \
".........................'',,;;;;;;;,,'..........cXWMMMMMMMMMNl.....;;;;;;;;;;,,;;,,,,,,,,,...lXWWWMMMMMMWWN0k0XXk,...,;.....................................................;o:......;;':;....ck0KKKXWWWWNNXK000KXNNWWWWWWWWNWWWMMMMMMMMWMMMMMMMWx,..............:0NWWWWWNXXNWWWWNNXx,........'............" \
"........................',;;;::::::;,'..........,0WWWWMMMMMMWO,....,:;;;,,,,,,,,,,,,,,,,,,'....xNXXWMMMMMMMMWNNNNXx'...,.....................................................:;......,lc;,...'cxOKKXNNWWNNXKK0KKXNWWWWMMMMMWWWWWWMMMMMMMMMMMMMMMMWk,...............oKXNWWNNXXXNWWWNNN0c...............''''''" \
".....................',;;::::::::::::,..........oNWWWWMMMMMMXc....':;;,'',,,,,,,,,,,,,,,,'......dKKXWMMMMMMMMMMMWWNk;..'....................................................,;'......'::....,cdOKXXXNNNXKKKKXNNWWWWWMMMMMMMWWWMWMMMMMMMMMMMMMMMMMW0:...............;OXXNNXXXXXNWWWNXNNx'...................." \
"'..................',;:::cc:ccccccccc:;........;KWWMMMMMMMMWk'....,;,,,,,,,,,,,,,,,,,,,'''.......oo:OMMMMMMMMMMMMMMWXk:'....................................................;,.............;ldkO0XXXNXXXXNNWWWWWMMMMMMMMMMMWNWMMMMMMMMMMMMMMMWWWWWNo'...............lKXXX00KKXXNWWNXXNKl...................." \
"'................',;::ccccccccccclllll:'.......kWMMMMMMMMMMXc.....;,',,,,,,,,,,,,,,,''''''........;,oXMMMMMMMMMMMMMMWWNx................................':cc;'..............;,...........';ldk0KXNNNNWWWWWWWWWWMMMMMMMMMMMMWNWWMMMMMWWNXK0kO0Oxxdxxc................'kKKKKXXK0O0XNNXXXN0:..................." \
",.............'',;::ccccccllllllooooolc,......lNMMMMMMMMMMWO'....',.',;,,,'',,,,,,,,,''''.........xOkKMMMMMMMMMMMMMMMWWNk;.............';c:'......''',;cdddol:'............,c;..........,:ldk0KXNNNNWWWWWMMMMMMMMMMMMMMMMMMWWWWWWNX0xooc:c:cdc''',,..................cOOxxk0OxOKXXXXXNNXx,.................." \
",...........',,;::cccllllllllooooooollc;.....'OWWMMMMMMMMWNo.....'.',,,,,'''',',,,,''''''........:0KOOXWMMMMMMMWMMMMMMMMWXkoooodxkOOkxkkkd;'''''';lxkkkxkOOOkdc:,'.........;c:'.......';cloxO0KXNNNWWWWMMMMMMMMMMMMMMMMMMMMMWN0xdoc:;;;;::,....'.......'..............cllloooxOKXXXXKXXNKl.................." \
";.........',;;:::cclllllllooooolccccccc;.....oWMMMMMMMWNKOd'.......,,,,''''''''','''''''.........lO0xcoKWWWNX0KNWMMMMMMMMMMMWNNWWWWWWWWNXKxlcllldO00000OkO00Okxdoc;'.......'cc:,..........',;:cloodx0KKNWWMMMMMMMMMMWWWNXXKOxo:;;;,'....,:,............................,:llldk0KKXXXKKXNNk;................." \
":....'',,,;;:::cccllllloooddddo;......''....;KMMMMMMMWNOoc;.......',''''''',,'''''''''''........lkx0Oc:x00Od:';oddxk0XNWMMMMMMMMMMWWWWWWWWWNXXKK00KKKK0OOO00OOkdl;'.........;:;,,'''',,,,,;,,,;;;;;;;:clddxxxkkkOOkkdoolc::::::::,......'';:'..........................:clodkO0KKXXXKKXNNKl'................" \
":,'',;;;;;:::cccclllooddddddddd;............xWMMMMMMWNKkdo;......',,'''''''''''''''''''........,O0dxkocxkxddooc:;,;;:cox0NWWWWNX0kxkkkkkxkkkOOkdooddddddddddddlc:..........,::::cccccllllllllolllccccccllllccccccc::::cccccc::::c:;,...',:cc,..........................oxxkkOO0KKXXKKKXXNNk;.'''''.........." \
"c;,',;;:::cccclllooddxxxxxxdc;c:..,,'......:XMMMMMMWN0kxdo,......''''''''''''''''.'''''........dNX0Od:o0OkkO000OkddoooooodkOkxdoc::ccllllllllllllllllllllllllllcc'.........:clloooooooloooooolllcllloodooooooooooooooooooolcc:::c:::;'..;ccc,..........................d000OO000KXXKKKKXNNKo''''............" \
"c;,;;:::ccclllooddxxxxxxxdoc;'''..........'OWMMMMMWNKOOkdl'........''.'''''''''''''''''........kWN0KOldXKOkOKNNNXK0Okkxdoollllllloooooooddoddooooooooooooooooooll:........'looodddooooooollcccclloddddddddddddddddddddddoolccc::ccccc;';clc,;;.........................oKKK00O00KXXK00KXNNXk:''............." \
"l:::::cccllloodxxxkxxdoc:,................lNMMMMMWWNXKOxol,..........'''''''''''''''''........;KWWKOxokNNKOkOKXNNNXK0OOkxdolccccllloooddddddddddddddddddddddoooooc........'loodddxxxxxdoolllllodddxxddddddddddddddddddddoollcc:::::cc:,,:l:,:c'........................lXXXK000KKKXK00KXNNNKo,''............" \
"lc::cccllloddxxxdoc;,................,....OWWMMMMWNXOkxdod;..........'''''''''''''''''........dWWWN0dcxNNXKOkO0XXNNXXK0Okxdolcc:::cclloooodooooooooooooooooooooooc...'.'..'llooddxxxkkkkkkkkkkxxxxxxxxdxddddddddddddddoooollcc::::::::;,::;:::;........................c0XKKK00KKKKK0OKXNNXXx;''............" \
"cc:cclllooool:;'..........,;::;,'...:c,..:XMWMMMWWNK00OkO0l...........'''''''''''''''........;KWWWX0OdkNWNXKOOOOKXXXXKK0Okxddolccc::::cccllllllllllllllcccccllllcc'..,,'..'cllooddxkO0KXXXXXK0OOkkkkxxxxxxxxxddddddooooooollcc::::::::;,:::;:l;........................lO0KXKK00KKKK0O0XNNNX0l''''.........." \
"cccclllc:,'........';:loxkkkkxdoc;';cc;.'kWMWWWMWWNK0OO0XNd............'''...'''''''.........dWWWWNkoloXWWNXK0OOO0KXXXK0Okkxdddoollcc::::ccccllloooooooooollllcc::,..',,..'loodxxkkO0KXXNNNNNXXXKK00OOOkkkkkkkkkxxxdoooooolllcc::c:::;;,:c;,cl;........................oO0KKXK00KKK0OO0XNNXXXx;','''........" \
":c:clo:.........,ldxkkkkkkkkkxxdo:,;::,.cNMMMWMMWNXK000XNWk...................'.''''........'0WNNNNKxlcOWNNXXKK0OO0KXXK0Okkxxdddddoolcc::::::cclloooooooooooooooll;........lodxkOO00000KXNNNWNNNNXXKK000OOOOkkkkkkxdooddooolllcccccc::;;c:;ldl,.......................'dO0KKXKK00KK0OO0XXXK0KOc','''''''...."

c = 0
colors = ['\033[97m','\033[96m','\033[95m','\033[94m','\033[93m','\033[92m','\033[91m']
music = ""
while 1:
	print("\033[1m"+colors[c]+ascii_art)
	c += 1
	if c == len(colors):
		c = 0
	ts(0.1)
	os.system('clear')

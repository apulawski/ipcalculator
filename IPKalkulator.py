#-*- coding: utf-8 -*-
import os, sys, string

''' Funkcja IP oddziela adres IP z wprowadzonych przez użytkownika danych '''
def IP (adres):
	adresIP=adres[0:adres.find('/')]
	return adresIP

''' Funkja maska_bit oddziela maskę z wprowadzonych przez użytkownika danych'''
def maska_bit (adres):
	maska=adres[(adres.find('/')+1):len(str(adres))]
	return maska

def mask_bin:
    pass

def testowa(wartosc):
    pass

''' Funkcja zamienia adres IP na postać binarną '''
def IP_bin (adres):
	i=0
	tab=[]
	znak=''
	adres=adres+'.'
	
	''' Dzieli podany adres dziesiętny na cztery i każdą część dodaje do listy tab '''
	
	while i<len(adres):
		
		if adres[i:i+1]!='.':
			znak=znak+adres[i:i+1]			
		else:
			tab.append(znak)
			znak=''
		
		i=i+1
		
	''' Pobiera z listy tab każdą wartość dziesiętną i zamienia na postać binarną  '''	
	
	i=0
	znak=''
	while i<4:
		j=7
		while j>0
			
			if ((2**j)>int(tab[i])):
				znak=znak+'0'
			elif ((2**j)<int(tab[i])):
				int(tab[i])=(int(tab[i])-(2**j))   
				znak=znak+'1'
			elif ((2**j)==int(tab[i])):
				znak=znak+'1'
							
			j=j-1
		
		i=i+1
		
		
		
		
		
		
		
wybor=True

while wybor:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '*********************************************************'
	print '*                                                       *'
	print '*                      IP Kalkulator                    *'
	print '*                                                       *'
	print '*********************************************************'
	print ''
	print 'Proszę wybrać sposób wprowadzenia adresu IP i maski sieci'
	print '1 - Skrucona wersja: X.X.X.X/Y'
	print '2 - Pełna wersja: X.X.X.X/Y.Y.Y.Y'
	print '3 - Koniec'
	
	try:
		wyb_opcji=int(raw_input("Wybrano opcję: "))
		
		if wyb_opcji==1:
			wybor=False

			''' Użytkownik podaje adres IP oraz maskę sieci w skróconej postaci - X.X.X.X/Y
				wprowadzone dane przypisane są do zmiennej o nazwie fulladres
			'''
			print ''
			fulladres=str(raw_input("Podaj adres IP i maskę sieci w postaci skróconej: "))
			
			adresIP=IP(fulladres)
			maska=maska_bit(fulladres)
			
			print adresIP
			
			IP_bin(adresIP)
			
										
			
		elif wyb_opcji==2:
			print 'Wybrałeś wartość - 2'
			wybor=False
		elif wyb_opcji==3:
			print 'Wybrałeś wartość - 3'
			wybor=False
		else:
			print ''
							
	except ValueError:
		print ''
				
	except KeyboardInterrupt:
		print ''
				
	except EOFError:
		print ''
		








		


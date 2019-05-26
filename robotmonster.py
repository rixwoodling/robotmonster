#!/usr/bin/python
# coding: utf-8

import random, os

def play_game():

	p_health = 20
	m_health = 20
	
	while True:
#player 1
		p_roll = random.randint(0, 2)

		os.system('clear')

		if p_roll == 2:
			m_health = m_health - p_roll
			if m_health <= 0:
				print "\n\t" + "You deliver a POWERSTRIKE!"
				print "\n\t" + "You kill Robot-Monster!"
				return
			elif m_health > 0:    
				print '\n\t' + "You deliver a POWERSTRIKE!"
				print '\n\t' + "Your health is %s." % p_health
				print '\t' + "Robot-Monster's health is %s." % m_health
				raw_input('\t' + 'Press any key to defend...')
		elif p_roll == 1:
			m_health = m_health - p_roll
			if m_health <= 0:
				print "\n\t" + "You strike!"
				print "\n\t" + "You kill Robot-Monster!"
				return
			elif p_roll > 0:     
				print "\n\t" + "You strike!"
				print "\n\t" + 'Your health is %s.' % p_health
				print "\t" + 'Robot-Monster\'s health is %s.' % m_health
				raw_input("\t" + "Press any key to defend...")
		elif p_roll == 0:
			print "\n\t" + "You missed!"
			print "\n\t" + 'Your health is still %s.' % p_health
			print "\t" + 'Robot-Monster\'s health is %s.' % m_health
			raw_input("\t" + "Press any key to defend...")
#switch message        

		os.system('clear')    

		print "\n\t" + "Robot-Monster moves in for an attack--"
		raw_input("\t" + "Press any key to block...")
#player 2
		os.system('clear')

		m_roll = random.randint(0, 2)
		if m_roll == 2:
			p_health = p_health - m_roll
			if p_health <= 0:
				print "\n\t" + "Robot-Monster POWERSTRIKES! -2"
				print "\n\t" + "Robot-Monster destroys you!"
				return
			elif p_health > 0:    
				print "\n\t" + "Robot-Monster POWERSTRIKES! -2"
				print "\n\t" + 'Your health is %s.' % p_health
				print "\t" + 'Robot-Monster\'s health is %s.' % m_health
				raw_input("\t" + "Press any key to attack...")
		elif m_roll == 1:
			p_health = p_health - m_roll
			if p_health <= 0:
				print "\n\t" + "Robot-Monster hits you! -1"
				print "\n\t" + "Robot-Monster defeats you!"
				return
			elif m_roll > 0:     
				print "\n\t" + "Robot-Monster hits you! -1"
				print "\n\t" + 'Your health is %s.' % p_health
				print "\t" + 'Robot-Monster\'s health is %s.' % m_health
				raw_input("\t" + "Press any key to attack...")
		elif m_roll == 0:
			print "\n\t" + "Robot-Monster misses!"
			print "\n\t" + 'Your health is still %s.' % p_health
			print "\t" + 'Robot-Monster\'s health is %s.' % m_health
			raw_input("\t" + "Press any key to attack...")
		else:
			print "brokun."                  

def main():

	os.system('clear')

	print '\n\t' + 'Fight Robot-Monster to the death!'
	raw_input("\n\t" + "Press any key to continue...")

	os.system('clear')

	print '\n\t' + 'You and Robot-Monster face-off--'
	print '\t' + 'People scream in the street as a city burns--'
	raw_input("\n\t" + "Press any key to attack...")

	while True:    
		play_game()

		play_again = raw_input('\n' + 'Play again? y/n: ') == 'y'
		if not play_again:
			return  # Leave main

main()

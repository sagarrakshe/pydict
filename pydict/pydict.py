"""
/* Copyright (c) pydict 2012, Sagar Rakshe <sagarrakshe2@gmail.com>  
** 
** Permission to use, copy, modify, and/or distribute this software for  
** any purpose with or without fee is hereby granted, provided that the  
** above copyright notice and this permission notice appear in all copies.  
**  
** THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL  
** WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED  
** WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR  
** BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES  
** OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,  
** WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,  
** ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS  
** SOFTWARE.  
*/ 
"""

import mechanize
import urllib2
import color
import parser
import pronounce
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

htmlParsedPage = ''
browser = mechanize.Browser()


def get_parsed_page(keyword):
	global htmlParsedPage, browser
	url = 'http://www.thefreedictionary.com/' + str(keyword)
	page = browser.open(url)
	htmlParsedPage = page.read()
	return htmlParsedPage


def search(keyword, repeat, style):
	global htmlParsedPage
	
	query = keyword

	if len(query):
		color.print_line('---'*45)
		color.print_heading('*\t'*4+"The Free Online Dictionary, Thesaurus and Encyclopedia\t"
			+'\t'+'*\t'*5)
		color.print_line('---'*45)
		color.print_word(query.upper()+'\n')

		try:
			htmlParsedPage = get_parsed_page(keyword)

			#parse to find the meaning
			soupPage = BeautifulSoup(htmlParsedPage)
			div = soupPage.findAll('div', attrs = {'id': 'MainTxt'})
			meaning = div[0].findAll('div', attrs = {'class':'ds-list'})
			if meaning == "":
				meaning = div[0].findAll('div', attrs = {'class' : 'ds-single'})

			for i in range(len(meaning)):
			    color.print_meaning('\t'+parser.strip_tags(str(meaning[i]))+'\n')
		except:
			color.print_error('Keyword not found in the Dictionary')

		color.print_line('---'*45)
		color.print_heading('\t'*6+'sagarrakshe2@gmail.com')
		color.print_line('---'*45)

		speak(keyword, repeat, style)

	else:
		color.print_error('Empty Keyword!')

def speak(keyword, repeat, style):
	global htmlParsedPage, browser

	pronouce_style = ['normal', 'us', 'uk', '']
	if repeat >0 and len(keyword) and any(style in item for item in pronouce_style):
		if htmlParsedPage == '':
			htmlParsedPage = get_parsed_page(keyword)

		soupPage = BeautifulSoup(htmlParsedPage)
		htmlParsedPage = ''
		div = soupPage.findAll('div', attrs = {'id': 'MainTxt'})	


		try:
			if style.lower() == 'normal' or style.lower() == '':
				mean_sound = str(parser.strip_tags(str(div[0].findAll('script')[0]))).split('"')[1]
				sound_url = 'http://img.tfd.com/hm/mp3/' + mean_sound +'.mp3'
			
			elif style.lower() == 'uk':
				sample = soupPage.findAll('td', attrs = {'id': 'MainTitle'})
				mean_sound = str(parser.strip_tags(str(sample[0])).split("'")[3])
				sound_url = 'http://img2.tfd.com/pron/mp3/' + mean_sound + '.mp3'

			elif style.lower() == 'us':
				sample = soupPage.findAll('td', attrs = {'id': 'MainTitle'})
				mean_sound = str(parser.strip_tags(str(sample[0])).split("'")[1])
				sound_url = 'http://img2.tfd.com/pron/mp3/' + mean_sound + '.mp3'

			sound_path = browser.retrieve(sound_url)
			pronounce.play(sound_path[0], repeat)
		except:
			color.print_error('Pronouciation not found!\nTry with different style.')

		
	elif repeat:
		color.print_error('Empty Keyword or Unknown Style!')	

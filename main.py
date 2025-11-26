"""
This file is my main and is responsible to importing all my functions and also handling
the parameters in the CLI.
"""

from stats import basic_counts, top_k_words, word_length, sentence_statistics
from rule_based import remove_stopwords, regex_tokenizer

def main():
	text = "Chapter 1 – The Boy Who Lived. Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. Mr. Dursley made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs. Dursley was thin and blonde and had twice the usual amount of neck, which came in very useful as she spent so much of her time spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere. Mrs Dursley had a sister called Lily Potter. She and her husband James Potter had a son called Harry Potter. They lived far from the Dursleys and did not speak to them much. They did not get along. One day, a man appeared outside of the Dursleys house. He was tall, thin, and very old, judging by the silver of his hair and beard, which were both long enough to tuck into his belt. He was wearing long robes, a purple cloak that swept the ground, and highheeled, buckled boots. His blue eyes were light, bright, and sparkling behind half-moon spectacles and his nose was very long and crooked, as though it had been broken at least twice. This man's name was Albus Dumbledore."
	
	print("Original text ---> ", text)	

	print("")
	print("<<<<<<<<<<<<<<< BASIC CHARACTERS, WORDS, AND SENTENCES STATISTICS >>>>>>>>>>>>>>>")
	
	print("")

	num_chars, num_words, num_sent = basic_counts(text)
	print("Basic Counts --->")
	print("Number of characters: ", num_chars)
	print("Number of words: ", num_words)
	print("Number of sentences: ", num_sent)
	
	print("")

	print("Word Statistics --->")
	k = int(input("Enter your k value: "))
	k_words = top_k_words(text, k)
	print("Top K most frequent words: ", k_words)
	longest_word, shortest_word, average_word_len = word_length(text)
	print("Longest word: ", longest_word)
	print("Shorted word: ", shortest_word)
	print("Average word length: ", average_word_len)
	
	print("")

	print("Sentence Statistics --->")
	longest_sentence, shortest_sentence, average_sentence_count = sentence_statistics(text)
	print("Longest sentence: ", longest_sentence)
	print("Shortest sentence: ", shortest_sentence)
	print("Average word count for all sentences: ", average_sentence_count)

	print("")
	print("<<<<<<<<<<<<<<< STOP WORDS, REGEX, RULE-BASED  >>>>>>>>>>>>>>>")
	
	print("")
	
	tokens_no_stopwords = remove_stopwords(text)
	print("Naive tokens: ", tokens_no_stopwords)
	
	print("")
	
	regex_tokens = regex_tokenizer(text)
	print("Regex tokens: ", regex_tokens)

if __name__ == "__main__":
	main()

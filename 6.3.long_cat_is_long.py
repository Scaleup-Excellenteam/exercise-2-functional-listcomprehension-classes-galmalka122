def count_words(text):
  """
  Count the number of appearence for each word in a text
  
  Args:
      text (str): The text string to be counted

  Returns:
      dict: A dictionary where each key is the word and the value is 
            The number of apearence in the text
  """
  filtered_text = ''.join(word.lower() 
                          for word in text
                          if word.isalpha() or word.isspace())
  
  words_and_length = {word: len(word) for word in filtered_text.split()}
  
  return words_and_length
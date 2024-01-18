def count_words(text):
  """
  Count the number of appearances for each word in a text
  
  Args:
      text (str): The text string to be counted

  Returns:
      dict: A dictionary where each key is the word and the value is 
            The number of appearances in the text
  """
  filtered_text = ''.join(char.lower() 
                          for char in text
                          if char.isalpha() or char.isspace())
  
  words_and_length = {word: len(word) for word in filtered_text.split()}
  
  return words_and_length

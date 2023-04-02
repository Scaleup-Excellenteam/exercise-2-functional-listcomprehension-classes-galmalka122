class PostOffice:
  """
  A Post Office class. Allows users to message each other.
  
  Args:
      usernames (list): Users for which we should create PO Boxes.

  Attributes:
      message_id (int): Incremental id of the last message sent.
      boxes (dict): Users' inboxes.
  """

  def __init__(self, usernames):
      self.message_id = 0
      self.boxes = {user: [] for user in usernames}
      
  def send_message(self, sender, recipient, message_body, urgent=False):
      """
      Send a message to a recipient.

      Args:
          sender (str): The message sender's username.
          recipient (str): The message recipient's username.
          message_body (str): The body of the message.
          urgent (bool, optional): The urgency of the message.
                                  Urgent messages appear first.

      Returns:
          int: The message ID, auto incremented number.

      Raises:
          KeyError: If the recipient does not exist.

      Examples:
          After creating a PO box and sending a messages,
          the recipient should have 1 message in the
          inbox.

          >>> po_box = PostOffice(['a', 'b'])
          >>> message_id = po_box.send_message('a', 'b', 'Hello!')
          >>> len(po_box.boxes['b'])
          1
          >>> message_id
          1
      """
      user_box = self.boxes[recipient]
      self.message_id = self.message_id + 1
      message_details = {
          'id': self.message_id,
          'body': message_body,
          'sender': sender,
      }
      if urgent:
          user_box.insert(0, message_details)
      else:
          user_box.append(message_details)
      return self.message_id
    
  def add_user(self, username):
    """
    Adds user to PO Boxes if the user does not exist.
    
    Args:
      username (str): The user to add to PO Boxes.
    """
    if username not in self.boxes.keys():
      self.boxes.update({username: []})
      
  def delete_user(self, username):
    """
    Removes user from PO Boxes.
  
    Args:
      username (str): The user to remove from PO Boxes.
      
    Raises:
        KeyError: If the user does not exist.
    """
    self.boxes.pop(username)
    
  def read_inbox(self, username, n = -1):
    """Get the first n messages from user's box.

      Args:
          username (str): The user of the message box.
          n (int): The number of messages to get. if Missing,
                   Return all messages within inbox 

      Returns:
          list: The first n messages in user's box.

      Raises:
          KeyError: If the recipient does not exist.

      Examples:
          After creating a PO box and reciving messages,
          the recipient should get the n first messages.
          
          >>> po_box = PostOffice(['a', 'b'])
          >>> po_box.send_message('a', 'b', 'Hello')
          >>> po_box.send_message('a', 'b', 'World')
          >>> po_box.send_message('a', 'b', '!')
          >>> po_box.read_inbox('b', 2)
          [{'id': 1, 'body': 'Hello', 'sender': 'a'},
           {'id': 2, 'body': 'World', 'sender': 'a'}]
    """
    user_box = self.boxes[username]
    messages = [user_box[i] for i in range(len(user_box)) if i < n or n == -1]
    return messages
  
  def search_inbox(self, username, substring):
    """
    Get all messages from user's box contains the substring.

    Args:
        username (str): The user of the message box.
        substring (str): The substring that should 
                        Be found in the message body.

    Returns:
        list: All messages containing substring in the body.

    Raises:
        KeyError: If the recipient does not exist.
        TypeError: If the substring is not type(str).
        
    Examples:
        After creating a PO box and reciving letters,
        the recipient should get the messages contains substring.
        
        >>> po_box = PostOffice(['a', 'b'])
        >>> po_box.send_message('a', 'b', 'Hello')
        >>> po_box.send_message('a', 'b', 'World')
        >>> po_box.send_message('a', 'b', '!')
        >>> po_box.search_inbox('b', 'l')
        [{'id': 1, 'body': 'Hello', 'sender': 'a'},
         {'id': 2, 'body': 'World', 'sender': 'a'}]
        >>> po_box.search_inbox('b', '!')
        [{'id': 3, 'body': '!', 'sender': 'a'}]
    """
    user_box = self.boxes[username]
    messages = substring != '' and [message for message in user_box if message['body'].find(substring) != -1]
    return messages
class Save:

   def __init__(self, stream, c, m, msg, title, artist, thumb, length, info):
      self.stream = stream
      self.client = c
      self.message = m
      self.msg = msg
      self.title = title
      self.artist = artist
      self.thumb = thumb
      self.length = length
      self.info = info

   def getSteams(self):
      return self.stream



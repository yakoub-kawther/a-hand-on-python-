def album(artist , albumName ,number=None):
  """" display name and album's name"""
  person={'artis name':artist , 'his album':albumName }

  if number is not None :
    person['song number']=number
  
  return person


print(album(albumName='let it happend',artist='Tame Impala'))
print(album(albumName='idk',artist='v' ,number=5))
from twitter import *
import ngram_Twitter

Markov_Text=ngram_Twitter.print_twitter("hp1.txt",2, 3)

CONSUMER_KEY= "2MGfzHA72F1EtMaxuQX2g"
CONSUMER_SECRET= "ncMrp3puJiYrD6vvwVnozFh1RZXL0Zvia06vWB5Vxo"

oauth_token="49141146-o8b98EJfFAXuYBkelmREEdQ79dXLxdCTrhArXJFWk"
oauth_secret= "DmpXvgWP5VxmrCsVFQYHEkfbyKZnhUwPCY32FHrB5Sw"

t= Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))


t.statuses.update(
    status= Markov_Text)
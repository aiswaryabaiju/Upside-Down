import moodevalyoutube
import moodevalspotify
import moodevalgif

def listA(keyword, limit):
	video = moodevalyoutube.mood_eval_youtube(keyword, limit)
	gif = moodevalgif.mood_eval_gif(keyword, limit)
	spt = moodevalspotify.spotify_api(keyword, limit)
	#TODO: fix limit on spotify
	sptLst = spt.get_random_song()

	listb = video+gif+sptLst
	return listb

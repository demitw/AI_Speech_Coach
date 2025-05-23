FILLERS = ['um', 'uh', 'like', 'you know', 'so', 'actually']

def count_filler_words(transcript):
    words = transcript.lower().split()
    return sum(words.count(f) for f in FILLERS)

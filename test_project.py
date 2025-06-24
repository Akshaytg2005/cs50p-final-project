from project import fetch_headlines, analyse_sentiments, print_summary

def test_fetch_headlines():
    headlines=fetch_headlines("AI", 5)
    assert isinstance(headlines, list)
    assert all(isinstance(h, str) for h in headlines)



def test_fetch_headlines_limit():
    headlines=fetch_headlines("AI", 5)
    assert len(headlines)<=5


def test_analyse_sentiments():
    headlines=["Gold price rise", "Market crashes"]
    sentiments=analyse_sentiments(headlines)
    assert len(sentiments)==2
    assert all(isinstance(s,float) for s in sentiments)

def test_analyse_sentiments_empty():
    sentiments=analyse_sentiments([])
    assert sentiments==[]

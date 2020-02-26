
def querysorted(query):
    query=[i for i in query.split()]
    k=['wikipedia','who',"is","to",'according']
    for i in k:
        if i in query:
            query.remove(i)

    return " ".join(query)
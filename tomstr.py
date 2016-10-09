def getnumin(content):
    return ''.join(c for c in content if c.isdigit())

def getin(content,start,end):
    s=content.find(start)
    e=content.find(end,s+len(start))
    return content[s+len(start):e]

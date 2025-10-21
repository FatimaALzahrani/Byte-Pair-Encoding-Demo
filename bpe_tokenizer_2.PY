from collections import Counter

def byte_pair_encoding(corpus, num_merges):
    tokens = list(corpus)
    vocab = set(tokens) 
    
    for _ in range(num_merges):
        pairs = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]
        
        if not pairs:
            break
        
        pair_counts = Counter(pairs)
        most_frequent = pair_counts.most_common(1)[0][0]  # (tL, tR)
        
        new_token = ''.join(most_frequent)
        vocab.add(new_token)
        
        i = 0
        new_tokens = []
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i+1]) == most_frequent:
                new_tokens.append(new_token)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        tokens = new_tokens
    
    return vocab, tokens


corpus = "set new new renew reset renew"
vocab, encoded = byte_pair_encoding(corpus, num_merges=5)

print("Final Vocabulary:", vocab)
print("Encoded Corpus:", encoded)




# _________________________________________________

from collections import Counter
def bpe(c,k):
    t,V=list(c),set(c)
    for _ in range(k):
        if not (p:=Counter(zip(t,t[1:]))):break
        a,b=p.most_common(1)[0][0];n=a+b;V|={n}
        i,u=0,[]
        while i<len(t):
            if i<len(t)-1 and (t[i],t[i+1])==(a,b):u+=[n];i+=2
            else:u+=[t[i]];i+=1
        t=u
    return V,t

print(bpe("set new new renew reset renew",5))

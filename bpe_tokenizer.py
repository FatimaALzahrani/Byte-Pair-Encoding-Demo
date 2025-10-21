# اول شيء نقسم كل كلمة لحروف 
# نحسب مرات ظهور كل حرف 
# ________ لوب _____________
# بعدين نسوي ازواج كل حرفين جنب بعض 
# نحسب كل زوجين كم مره تكرروا 
# اللي لهم اعلى عدد تكرارات نضيفهم للستتنا وندمجهم في كل مكان
# نعيد لكل الازواج نفس الشيء لين ترجع الكلمات نفس البداية

from collections import defaultdict

def byte_pair_encoding(courps):
    words = courps.split()
    corpus = [list("_" + word) for word in words]
    # courps = [token for tokencorpus[0][1:])
    vocab = set(char for word in corpus for char in word)

    merge_operations = []

    while True:
        pairs = defaultdict(int)
        for word in corpus:
            for i in range(len(word) - 1):
                pair = (word[i], word[i + 1])
                pairs[pair] += 1

        if not pairs:
            break

        most_common = max(pairs, key=pairs.get)
        count = pairs[most_common]
        merge_operations.append((most_common, count))

        print(f"Merging: {' '.join(most_common)} → {''.join(most_common)} (count {count})")

        new_corpus = []
        for word in corpus:
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == most_common:
                    new_word.append("".join(most_common))
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_corpus.append(new_word)
        corpus = new_corpus

        vocab.add("".join(most_common))

        print("Updated Corpus:")
        for word in corpus:
            print(" ", " ".join(word))
        print("Updated Vocabulary:", sorted(vocab))
        print("-" * 40)

        if count < 2:
            break

    print("Final Tokenized Corpus:")
    for word in corpus:
        print(" ", " ".join(word))

    print("\nLearned Merge Operations:")
    for op, cnt in merge_operations:
        print(f"  {' '.join(op)} → {''.join(op)} (count {cnt})")

    return vocab

print(byte_pair_encoding("set new new renew reset renew"))
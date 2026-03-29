
def precision_at_k(recommended, relevant, k=5):
    recommended_k = recommended[:k]
    return len(set(recommended_k) & set(relevant)) / k  
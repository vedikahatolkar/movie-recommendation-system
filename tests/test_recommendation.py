from src.recommendation_model import Recommender

def test():

    model = Recommender()

    result = model.recommend("Toy Story (1995)")

    assert isinstance(result, list)

    print("Test passed!")

if __name__ == "__main__":
    test()
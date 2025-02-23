from library.models import Review


class ServicesReview:
    @staticmethod
    def calculate_average_rating(book_id):
        reviews = Review.objects.filter(book_id=book_id)

        if not reviews.exists():
            return None

        average_rating = sum(review.rating for review in reviews) / reviews.count()
        return average_rating

    @staticmethod
    def is_popular(book_id, threshold=4.5):
        average_rating = ServicesReview.calculate_average_rating(book_id)

        if average_rating is None:
            return None

        return average_rating > threshold

from simpletransformers.classification import ClassificationModel


class TurkishTextClassificationModel:
    def __init__(self):
        self.model = ClassificationModel('bert', './model', num_labels=7, use_cuda=False, args={"use_multiprocessing": False})
        self.categories = ['siyaset', 'dunya', 'ekonomi', 'kultur', 'saglik', 'spor', 'teknoloji']

    def classify_text(self, text: str):
        prediction = self.model.predict([text])
        predicted_category = prediction[0][0]
        print(prediction)
        print(type(prediction))
        print("---")
        
        print(predicted_category)
        print(self.categories[predicted_category])
        return {"category": self.categories[predicted_category]}

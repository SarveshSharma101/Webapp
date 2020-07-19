from fastai.vision import load_learner, open_image

def load_model():
	l = load_learner(path="C:\\Users\\LENOVO\\Desktop\\1stwebapp\\Model", file = 'my1stmodel.pkl')
	return l

def get_image(path):

	return open_image(path)
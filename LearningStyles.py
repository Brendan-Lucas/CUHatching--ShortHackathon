

class LearningStyles(self):

  def __init__learningStyles(self, Auditory=0.25, Visual=0.25, Kinestetic=0.25, Pace=5, Social=0.25):
      self.auditory = Auditory
      self.visual = Visual
      self.kinestetic = Kinestetic
      self.pace = Pace
      self.social = Social
      self.test_score = -100

  def set_test_score(self, test_score):
      self.test_score = test_score

  def get_test_score(self):
      return self.test_score

  def compare(self, learning_style):
      compare_list = []
      compare_list.append(self.auditory - learning_style.auditory)
      compare_list.append(self.visual - learning_style.visual)
      compare_list.append(self.kinestetic - learning_style.kinestetic)
      compare_list.append(self.pace - learning_style.social)
      compare_list.append(self.social -learning_style.social)
      return compare_list

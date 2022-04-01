import warnings

# modelop.score
def action(datum):
  print("action datum:", flush=True)
  print(datum, flush=True)
  warnings.warn("called via warnings.warn", category=UserWarning)
  yield {
    "foo": 1,
    "bar": "score"
  }

def action_raise(datum):
  print("action datum:", flush=True)
  print(datum, flush=True)
  raise UserWarning("this was 'raised'")
  yield {
    "foo": 1,
    "bar": "score"
  }

def action_exception(datum):
  print("action datum:", flush=True)
  print(datum, flush=True)
  raise Exception("this was 'raised'")
  yield {
    "foo": 1,
    "bar": "score"
  }

# modelop.metrics
def metrics(datum):
  print("metrics_one datum:", flush=True)
  print(datum, flush=True)
  warnings.warn("called via warnings.warn", category=UserWarning)
  yield {
    "foo": 1,
    "bar": "test result"
  }

def metrics_raise(datum):
  print("metrics_one datum:", flush=True)
  print(datum, flush=True)
  raise UserWarning("this was 'raised'")
  yield {
    "foo": 1,
    "bar": "test result"
  }

def metrics_exception(datum):
  print("metrics_one datum:", flush=True)
  print(datum, flush=True)
  raise Exception("this was 'raised'")
  yield {
    "foo": 1,
    "bar": "test result"
  }

# modelop.train
def train(datum):
  print("train_one datum:", flush=True)
  print(datum, flush=True)
  warnings.warn("called via warnings.warn", category=UserWarning)
  datum.to_json("outputDir/training-out.json", orient="records", lines=True)

def train_raise(datum):
  print("train_one datum:", flush=True)
  print(datum, flush=True)
  raise UserWarning("this was 'raised'")
  datum.to_json("outputDir/training-out.json", orient="records", lines=True)

def train_exception(datum):
  print("train_one datum:", flush=True)
  print(datum, flush=True)
  raise Exception("this was 'raised'")
  datum.to_json("outputDir/training-out.json", orient="records", lines=True)
